

def print2(text):
    print("更新后: " + text)


class Class1:
    v = 123

    def plain_func(self):  # 普通方法
        print(f"plain_func {Class1.v}")

    @classmethod
    def class_func(cls):  # 类方法
        print(f"class_func {Class1.v}")

    @staticmethod
    def static_func():    # 静态方法
        print(f"static_func {Class1.v}")
