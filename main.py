#!/usr/bin/env python
# TaskFramework - APScheduler
from apscheduler.schedulers.blocking import BlockingScheduler

# tools
import tools.local_data as local_data
import tools.log as log

# hotUpdate libs
import hot_update
import sys

# works
import works.domain as domain


def dojob():
    # 创建调度器：BlockingScheduler
    scheduler = BlockingScheduler()
    # 添加任务,时间间隔1S
    scheduler.add_job(domain.update, 'interval', seconds=3, id='test_job2')
    scheduler.start()


def init():

    hot_update.start()

    if 'server_ip' not in local_data.getData():
        local_data.setValue('server_ip', '127.0.0.1:3001')

    if len(sys.argv) > 1:
        kvps = dict()
        for i in range(1, len(sys.argv)):
            arg = sys.argv[i]
            if '=' in arg:
                kvp = arg.split('=')
                log.debug(f'parse arg: {arg} => key:{kvp[0]} value:{kvp[1]}')
                kvps[kvp[0]] = kvp[1]
            else:
                log.error(f'arg format error: {arg}')
        if len(kvps.keys()) > 0:
            local_data.setValue('runAppParams', kvps)


if __name__ == "__main__":
    init()
    dojob()
