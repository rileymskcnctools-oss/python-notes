# 定义一个变量
PI = 3.14159

# 定义函数 1：打招呼
def say_hello(name):
    """这是一个打印问候语的函数"""
    print(f"你好, {name}！欢迎学习 Python 模块。")

# 定义函数 2：计算圆面积
def circle_area(radius):
    """输入半径，返回圆的面积"""
    area = PI * (radius ** 2)
    return area

# 注意：通常模块里只放定义，不放直接运行的代码
