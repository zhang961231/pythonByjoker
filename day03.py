#1.
# i = 0
# j = 0
# def getPentagonalNumber():
#     global i
#     global j
#     for i in range(1,100):
#         j += 1
#         number = i*(3*i-1)/2
#         print(int(number),end='\000')
#         if j%10==0:
#             print('\n')
    
# getPentagonalNumber()


#2.
# word = input('请输入整数：')
# j = len(word)
# list_num = []
# def main1(word):
#     global j
#     global list_num
#     for i in range(len(word)):
#         a=int(word)%10
#         word = str(int(word)//10)
#         list_num.append(a)
#         j -= 1
#         if j==0:
#             sum_ = sum(list_num)
#             print(sum_)

# main1(word)



#3.
# def displaySortedNumbers(num1,num2,num3):
#     num1 = float(num1)
#     num2 = float(num2)
#     num3 = float(num3)
#     if num1 > num2:
#         if num1 > num3:
#             if num2 > num3:
#                 print('The sorted numbers are:%.2f %.2f %.2f'%(num3,num2,num1))
#             else:
#                 print('The sorted numbers are:%.2f %.2f %.2f'%(num2,num3,num1))
#         else:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num2,num1,num3))
#     else:
#         if num1 > num3:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num3,num1,num2))
#         elif num2 > num3:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num1,num3,num2))
#         else:
#             print('The sorted numbers are:%.2f %.2f %.2f'%(num1,num2,num3))

# num1,num2,num3 = input('Enter three numbers:').split(',')
# displaySortedNumbers(num1,num2,num3)


#5.
# j = 0
# def printChars(ch1,ch2,numberPerLine):
#     global j
#     num1 = ord(ch1)
#     num2 = ord(ch2)
#     for i in range(num1,num2+1):
#         print(chr(i),end='\000')
#         j += 1
#         if j % int(numberPerLine) == 0:
#             print('\n')

# ch1,ch2,numberPerLine = input('请输入指定字符和个数：').split(',')
# printChars(ch1,ch2,numberPerLine)


#6.
# def numberOfDaysInYear(year):
#     for i in range(year,year+11):
#         if (i%4 == 0 and i%100!=0) or (i%100==0 and i%400==0):
#             day = 366
#         else:
#             day = 365
#         print('%s年有%d天'%(i,day))

# numberOfDaysInYear(2010)


#7.
# import math

# def distance(x1,y1,x2,y2):
#     h = math.sqrt((x1-x2)**2+(y1-y2)**2)
#     print('两点间距离为：%f'%h)

# distance(1,2,3,4)


#8.
# def mei(A):
#     for i in range(3,A):
#         a = A%1
#         if a == 0:
#             return(-1)
#             break
#     else:
#         return A
# for p in range(1,32):
#     A = (2**p)-1
#     s1 = mei(A)
#     if A == s1:
#         print(p,A)


#9.
# import time
# def main():
#     localtime = time.asctime(time.localtime(time.time()))
#     print("Current date and time is :", localtime)
# main()

#10.
import random

def panduan():
    num1 = random.randint(1,7)
    num2 = random.randint(1,7)
    if num1 + num2 == 2 or num1 + num2 == 3 or num1 + num2 == 12:
        print('You rolled %d + %d = %d \nYou lose'%(num1,num2,num1+num2))
    elif num1 + num2 == 7 or num1 + num2 == 11:
        print('You rolled %d + %d = %d \nYou win'%(num1,num2,num1+num2))
    else:
        point = num1 + num2
        print('You rolled %d + %d = %d '%(num1,num2,num1+num2))
        print('point is %d'%point)
        num1 = random.randint(1,7)
        num2 = random.randint(1,7)
        if num1 + num2 == point:
            print('point is %d'%point)-['']
            print('You rolled %d + %d = %d \nYou win '%(num1,num2,num1+num2))
        elif  num1 + num2 == 7:
            print('point is %d'%point)
            print('You rolled %d + %d = %d \nYou lose'%(num1,num2,num1+num2))

panduan()
