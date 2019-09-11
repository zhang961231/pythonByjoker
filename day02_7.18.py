#1.
# import math

# num1,num2,num3 = input('Enter a,b,c:').split(',')

# panbie = (float(num2)*float(num2))-(4*float(num1)*float(num3))
# if panbie >0:
#     x1 = (-float(num2)+math.sqrt(panbie))/2*float(num1)
#     x2 = (-float(num2)-math.sqrt(panbie))/2*float(num1)
#     print('The roots are %.6f and %.6f'%(x1,x2))
# elif panbie == 0:
#     x1 = (-float(num2)+math.sqrt(panbie))/2*float(num1)
#     print('The root is %.2f'%(x1))
# elif panbie <0:
#     print('The equation has no real roots')


#2.
# import random
# num1 = random.randint(0,100)
# num2 = random.randint(0,100)

# sum_ = int(input('请输入猜测数字：'))
# if sum_ == num1+num2:
#     print('True')
# else:
#     print('False')

#3.
# day = int(input('Enter today\'s day:'))
# number = int(input('Enter the number of days elapsed since today:'))
# day_list=['Sunday','Monday','Tuesday','Wednesday','Thursday','Firday','Saturday']
# sum_ = day+number
# zhou = sum_ % 7
# print('Today is\000'+day_list[day]+'\000and the future day is\000'+day_list[zhou])

#4.
# num1,num2,num3 = input('请输入三个数：').split(',')
# num1 = float(num1)
# num2 = float(num2)
# num3 = float(num3)
# if num1 > num2:
#     if num1 > num3:
#         if num2 > num3:
#             print(num3,num2,num1)
#         else:
#             print(num2,num3,num1)
#     else:
#         print(num2,num1,num3)
# else:
#     if num1 > num3:
#         print(num3,num1,num2)
#     elif num2 > num3:
#         print(num1,num3,num2)
#     else:
#         print(num1,num2,num3)


#5.
# weight1,price1 = input('Enter weight price for package 1:\000').split(',')
# weight2,price2 = input('Enter weight price for package 2:\000').split(',')

# num1 = float(price1)/float(weight1)
# num2 = float(price2)/float(weight2)
# if num1 < num2:
#     print('Package 1 has the better price.')
# else:
#     print('Package 2 has the better price.')


#6.
# year = input('请输入年份：')
# mouth = input('请输入月份：')
# list_mouth1 = ['1','3','5','7','8','10','12']
# list_mouth2 = ['4','6','9','11']
# if int(year)%4 == 0:
#     if mouth in list_mouth1:
#         print(year+'\000年\000'+mouth+'月有31天。')
#     elif mouth in list_mouth2:
#         print(year+'\000年\000'+mouth+'月有30天。')
#     else:
#         print(year+'\000年\000'+mouth+'月有29天。')
# else:
#     if mouth in list_mouth1:
#         print(year+'\000年\000'+mouth+'月有31天。')
#     elif mouth in list_mouth2:
#         print(year+'\000年\000'+mouth+'月有30天。')
#     else:
#         print(year+'\000年\000'+mouth+'月有28天。')



#7.
# import random
# ser = random.choice(['正','反'])
# ser1 = input('请输入猜测值：')
# if ser == ser1:
#     print('猜测正确')
# else:
#     print('猜测错误')

#8.
# import random

# ser = random.randint(0,2)
# print(ser)
# ser1 = input('scissor(0),rock(1),paper(2)')
# if ser == ser1:
#     if ser == 0 and ser1== '0':
#         print('The computer is scissor,You are scissor too.It is a draw')
#     elif ser == 1 and ser1 == '1':
#         print('The computer is rock,You are rock too.It is a draw')
#     else:
#         print('The computer is paper,You are paper too.It is a draw')
# elif ser == 1 and ser1 == '0':
#     print(ser)
#     print('The computer is rock,You are scissor.You lost')
# elif ser == 0 and ser1 == '2':
#     print(ser)
#     print('The computer is scissor,You are paper.You lost')
# elif ser == 2 and ser1 == '1':
#     print(ser)
#     print('The computer is paper,You are rock.You lost')
# else:
#     print('You won')


#9.
# year = int(input('Enter year:(e.g.,2008):\000'))
# mouth = int(input('Enter month:1-12:'))
# day = int(input('Enter the day of the month:1-31:'))
# list_d = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Firday']
# if mouth == 1:
#     mouth = 13
#     year -=1
#     yearOC = year % 100
#     century = year // 100
#     wek=int(day + 26 * (mouth + 1)//10 + yearOC + yearOC/4 + century/4 + 5*century) % 7
#     print('Day of the week is\000'+list_d[wek])
# elif mouth == 2:
#     mouth = 14
#     year -=1
#     yearOC = year % 100
#     century = year // 100
#     wek=int(day + 26 * (mouth + 1)//10 + yearOC + yearOC/4 + century/4 + 5*century) % 7
#     print('Day of the week is\000'+list_d[wek])
# else:
#     yearOC = year % 100
#     century = year / 100
#     wek=int(day + 26 * (mouth + 1)//10 + yearOC + yearOC/4 + century/4 + 5*century) % 7
#     print('Day of the week is\000'+list_d[wek])



#10.
# import random
# number = ['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
# flower = ['Plum','Heart','block','Spade']

# choice1 = random.choice(['Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King'])
# choice2 = random.choice(['Plum','Heart','block','Spade'])

# print('The card you picked is the\000'+choice1+'\000of\000'+choice2)


#11.
# integer = input("Enter a three-digit integer:")

# if integer == integer[::-1]:
#     print(integer+'\000is a palindrome')
# else:
#     print(integer+'\000is not a palindrome')

#12.
n1,n2,n3 = input('Enter three edges:').split(',')
n1 = float(n1)
n2 = float(n2)
n3 = float(n3)
if n1 + n2 < n3:
    print('输入错误')
elif n1 + n3 < n2:
    print('输入错误')
elif n2 + n3 < n1:
    print('输入错误')
elif n1 + n2 == n3:
    print('输入错误')
elif n1 + n3 == n2:
    print('输入错误')
elif n2 + n3 == n1:
    print('输入错误')
else :
    number = n1 + n2 + n3
    print('The perimeter is\000'+str(number))


