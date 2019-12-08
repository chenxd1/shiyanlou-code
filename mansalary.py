#!/usr/bin/env python3
basic_salary = 1500
bonus_rate = 200
commission_rate = 0.02
number = int(input('相机数量: '))
price = float(input('相机单价: '))
bonus = number * bonus_rate
commission = number * price * commission_rate
salary = basic_salary + number * bonus_rate + number * price * commission_rate
print('Bonus      ={:10.2f}'.format(bonus))
print('Commission ={:10.2f}'.format(commission))
print('Salary     ={:10.2f}'.format(salary))

