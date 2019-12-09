#!/usr/bin/env python3
row = int(input('Enter the number of rows: '))
n   = row
while n >= 0: 
    x = ' ' * (row - n) + '*' * n
    print(x)
    n -= 1
  
