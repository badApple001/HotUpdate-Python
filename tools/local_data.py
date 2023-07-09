r"""
    脚本的主要功能就是数据本地化

    你只需要负责访问和修改数据 不需要关心保存的问题

    读取的性能和普通变量一样高效 同时它还能持久化存储在本地 在下次程序启动的时候 你可以获取最后一次修改的值
    
    你可以通过 local_data.getData() 访问所有的数据 字典类型

    你可以直接调用 local_data.getData()['Key'] = value 来新增或者修改任何类型数据

    你也可以直接调用 local_data.setValue("key",anyValue) 来修改或者添加数据
"""
__version__ = '1.0.2'
__author__ = 'Geek7 <isysprey@foxmail.com>'

import json
import os
import time
import atexit
import tools.md5Helper as md5Helper
import tools.log as log
import tools.AES as AES

userpath = os.path.expanduser('~')
temppath = os.path.join(userpath, 'AppData/Local/Temp')
__binDir = os.path.join(temppath, md5Helper.string_to_md5(
    os.path.basename(os.getcwd())))
__localDataPath = os.path.join(__binDir, md5Helper.string_to_md5('data.json'))
__data = {}
__inited = False


def __init():
    global __data, __inited

    if not os.path.exists(__binDir):
        os.mkdir(__binDir)

    if os.path.exists(__localDataPath):
        with open(__localDataPath, 'r+') as fp:
            __data = json.loads(AES.decrypt(fp.read()))
            fp.close()
    if 'created_at' not in __data.keys():
        __data['created_at'] = __getTimeString()
    __inited = True


def __tryInit():
    if not __inited:
        __init()


def __getTimeString():
    now = int(time.time())
    timeArray = time.localtime(now)
    return time.strftime("%Y-%m-%d %H:%M:%S", timeArray)


@atexit.register
def __save():
    if type(__data) != dict:
        log.debug(
            "local_data._data is null. please do not modify the dictionary itself")
        return
    try:
        __writeData2File()
    except:
        log.debug('failed to write local_data to the local. Procedure')
        log.print_exc()
        try:
            log.debug('try to roll back the data')
            runtime_data = __data.copy()
            __init()
            for k, v in runtime_data.items():
                __data[k] = v
            __writeData2File()
        except:
            log.debug("It's hopeless to recover the data.")
            log.print_exc()


def __writeData2File():
    with open(__localDataPath, 'w+') as fp:
        __data['updated_at'] = __getTimeString()
        jsonstr = json.dumps(__data, sort_keys=True,
                 indent=4, separators=(',', ':'))
        fp.write(AES.encrypt(jsonstr))
        fp.close()


def getData() -> dict:
    __tryInit()
    return __data


def setValue(key: str, value):
    getData()[key] = value


__tryInit()
