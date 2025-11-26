
# 文件名: my_calc.py (注意：这一行会被 %%writefile 写入文件)

def add(x, y):
    """相加"""
    return x + y

def subtract(x, y):
    """相减"""
    return x - y

def multiply(x, y):
    """相乘"""
    return x * y

def divide(x, y):
    """相除 (带有除以0的检查)"""
    if y == 0:
        return "错误：除数不能为0"
    return x / y

# 运行 Cell 后，你会在输出看到 "Writing my_calc.py"
