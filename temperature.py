#!/usr/bin/env python3

#计算10个数的平均值
N=10
sum=0
count=0
print('请输入10个数字: ')
while count < N:
    number = float(input())
    sum=sum + number
    count = count + 1
average = sum / 10
print('N = {},Sum = {}'.format(N,sum))
print('average={:.2f}'.format(average))

