#1.
# import math

# length = float(input('Enter the length from the center to a vertex:\000'))
# s = 2*length*math.sin(math.pi/5)
# Area = 5 *s *s /(4*math.tan(math.pi/5))
# print('The area of the pentagon is\000%.2f'%Area)


#2.
# import math
# latitude1,longitude1 = input('Enter point 1 (latitude and longitude) in degress:\000').split(',')
# latitude2,longitude2 = input('Enter point 2 (latitude and longitude) in degress:\000').split(',')

# latitude1_hu = math.radians(float(latitude1))                 #把输入的经维度转换为弧度制
# longitude1_hu = math.radians(float(longitude1))
# latitude2_hu = math.radians(float(latitude2))
# longitude2_hu = math.radians(float(longitude2))
# print(latitude1_hu,latitude2_hu,longitude1_hu,longitude2_hu)
# radius = 6371.01
# d = radius*math.acos((math.sin(latitude1_hu)*math.sin(latitude2_hu))+(math.cos(latitude1_hu)*math.cos(latitude2_hu)*math.cos((longitude1_hu-longitude2_hu))))
# #print(str(math.sin(latitude1_hu),str(math.sin(latitude2_hu)),str(math.cos(latitude1_hu)),str(math.cos(latitude2_hu)),str(math.cos(longitude1_hu-longitude2_hu)))
# print('The distance bttween the two points is\000'+str(d)+'\000km')


#3.
# import math

# side = float(input('Enter the side:\000'))
# Area = (5*side*side)/(4*math.tan(math.pi/5))

# print('The area of the pentagon is\000'+str(Area))


#4
# import math
# number = int(input('Enter the number of sides:\000'))
# side = float(input('Enter the side:\000'))

# Area = (number*side*side)/(4*math.tan(math.pi/number))
# print('The area of the polygon is\000'+str(Area))


#5
# number=int(input('Enter an ASCII code:\000'))
# print('The character is\000'+chr(number))


#6
# name = input('Enter employee\'s name:\000\000')
# number = int(input('Enter number of hours worked in a week:\000\000'))
# pay = float(input('Enter hourly pay rate:\000\000'))
# federal = float(input('Enter federal tax withholding rate:\000\000'))
# state = float(input('Enter state tax withholding rate:\000\000'))

# print('Employee Name:\000'+name)
# print('Hours worked:\000%.1f'%(float(number)))
# print('Pay Rate:\000$'+str(pay))
# print('Gross Pay:\000$'+str(number*pay))
# print('Deductions:\n\000Federal Withholding(20.0%):\000$'+str(number*pay*0.2)+'\n\000State Withholding(9.0%):\000$'+
#         str(number*pay*0.09)+'\n\000Total Deduction:\000$%.2f'%((number*pay*0.2)+(number*pay*0.09)))
# print('Net Pay:\000$%.2f'%(((number*pay)-((number*pay*0.2)+(number*pay*0.09)))))



#7
# number = input('Enter an integer:')
# print(number[::-1])



#8
import hashlib
m = hashlib.md5()
test = input('请输入加密文本：')
m.update(bytes(test,encoding='utf8'))
with open('passwd.txt','w')as file:
    file.write(m.hexdigest())
