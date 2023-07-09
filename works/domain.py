import sys
import tools.log as log
from imp import reload

# hotUpdate modules
import works.Test as Test

inst = Test.Class1()

def update():

    # 可以热更
    Test.print2("测试")

    # 可以热更
    inst.plain_func()

    # 可以热更
    inst.class_func()

    # 可以热更
    Test.Class1.static_func()

    # 可以热更
    print(f"普通成员变量数据: {inst.v}")
