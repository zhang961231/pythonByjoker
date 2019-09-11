#1.

# x = 1
# num_zheng = 0
# num_fu = 0
# sum_ = 0
# number = 0
# average = 0
# while x != 0:
#     x = int(input('Enter ana integer ,the input ends if it is 0:'))
#     if x > 0:
#         num_zheng += 1
#     elif x < 0:
#         num_fu += 1
#     elif x==0:
#         print('共输入了%d个数，正数%d个，负数%d个，总和为%d，平均数为%.2f'%(number,num_zheng,num_fu,sum_,average))
#         break
#     sum_ += x
#     number = num_zheng + num_fu
#     average = float(sum_/number)

#2.
# money = 10000
# sum_ = 0
# for i in range(1,14):
#     money = money + money * 0.05
#     if i == 10 :
#         print('十年之后的学费为：%.2f'%money)
#     elif i>=10:
#         sum_ += money
# print('十年后大学四年的总学费为:%.2f'%sum_)

#3.
# x = 1
# num_zheng = 0
# num_fu = 0
# sum_ = 0
# number = 0
# average = 0
# while x != 0:
#     x = int(input('Enter ana integer ,the input ends if it is 0:'))
#     if x > 0:
#         num_zheng += 1
#     elif x < 0:
#         num_fu += 1
#     elif x==0:
#         print('共输入了%d个数，正数%d个，负数%d个，总和为%d，平均数为%.2f'%(number,num_zheng,num_fu,sum_,average))
#         break
#     sum_ += x
#     number = num_zheng + num_fu
#     average = float(sum_/number)

#4.
# number = 0
# for i in range(100,1000):
#     if i % 5==0 and i % 6==0:
#         print(i,end='\000')
#         number += 1
#         if number % 10 == 0:
#             print('\n')

#5.
# num1 = 0
# num2 = 0
# while num1*num1<=12000:
#     num1+=1
#     if num1*num1>12000:
#         print('n的平方大于12000的最小整数n为:%d'%num1)
#         break
# while num2*num2*num2<12000:
#     num2+=1
#     if num2*num2*num2>=12000:
#         print('n的三次方小于12000的最大整数为%d'%num2)
#         break

#7.
# sum_left = 0
# sum_right = 0
# for i in range(1,50001):
#     sum_left += (1/i)
# print('从左向右计算数列和结果为:',sum_left)
# for i in range(50001,1,-1):
#     sum_right += (1/i)
# print('从右向左计算数列和结果为:',sum_right)

#8.
# sum_ = 0
# for i in range(3,100,2):
#     sum_ += (i-2)/i
# print('数列的和为：',sum_)

#9
# for i in range(10000,110000,10000):
#     pi = 0
#     for j in range(1,i+1):
#         pi += 4 * ((-1)**(1+j)/(2*j-1))
#     print('当i=%d时，π的近似值为：%f'%(i,pi))

#10
# for i in range(1,10000):
#     num = 0
#     for j in range(1,i):
#         if i % j == 0:
#             num += j
#     if num == i:
#         print('10000以下的完全数有%d'%num)

#11
list_ = []
for i in range(1,8):
    for j in range(1,8):
        if i != j and sorted([i,j]) not in list_:
            list_.append([i,j])
print('The total number of all combinations is %d'%len(list_))



