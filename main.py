import tools  # 导入整个 tools 模块

# 使用：模块名.函数名()
tools.say_hello("小明")

# 使用：模块名.变量名
r = 5
area = tools.circle_area(r)
print(f"半径为 {r} 的圆面积是: {area}")

print("圆周率是:", tools.PI)