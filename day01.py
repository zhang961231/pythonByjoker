1.
celsius摄氏温度 Fahrenheit华氏温度
celsius = float(input('亲，请输入一个摄氏温度哦😘：>>'))
fahrenheit = (9 / 5) * celsius + 32
print("亲，转换的华氏温度为：%.1f" % fahrenheit)

2.
area底面积 radius半径 volume体积 Π=3.14
length = float(input("请输入一个高度：>>"))
radius = float(input("请输入一个半径：>>"))
area = radius * radius * 3.14
volume = area * length
print("圆柱体的底面积为：%.4f" % area)
print("圆柱体的体积为：%.4f" % volume)

3.
metre米 feet英尺
feet = float(input('请输入一个英尺数：>>'))
metre = feet * 0.305
print("%0.1f英尺数为%0.4f米" % (feet,metre))

4.
M是按千克计的水量，温度为摄氏温度，热量Q以焦耳计
M = float(input('请输入水的量：>>'))
initialTmperature = float(input('请输入初始温度:>>'))
finalTmperature = float(input('请输入最终温度:>>'))
Q = M * (finalTmperature - initialTmperature) * 4184
print("最终需要的能量为：%.1f" % Q)

5.
lixi利息 chae差额 nianlilv年利率
chae = float(input("请输入差额:>>"))
nianlilv =float(input("请输入年利率:>>"))
lixi = chae * (nianlilv / 1200)
print("要付的利息：%.5f" % lixi)

6.
V0为初始速度，V1为末速度，t为以秒为单位速度变化所占用的时间，a为平均加速度
V0 = float(input("请输入初始速度:>>"))
V1 = float(input("请输入末速度:>>"))
t = float(input("请输入占用的时间:>>"))
a = (V1 - V0) / t
print("平均加速度为：%.4f" % a)

7.

a = float(input("请输入存款数:>>"))
one = a * (1 + 0.00417)
two = (a + one)(1 + 0.00417)
three = (a + two)(1 + 0.00417)
four = (a + three)(1 + 0.00417)
five = (a + four)(1 + 0.00417)
six = (a + five)(1 + 0.00417)
print("六个月后，账户总额为：%.2f" % six)

8.

num = int(input("请输入1-1000的一个整数:>>"))
ge = int(num / 100)
shi = int(num / 10 % 10)
bai = int(num % 10)
sum = ge + shi + bai 
print("各位数字之和：" ,sum)