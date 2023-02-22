# a = 4
# b = 6
#
# one = (a - b) * (a + b)
# print(one)
# one = a**2 - 2*a*b +b**2
# print(one)
# one = a**2+2*a*b+b**2
# print(one)
# one = a**3-3*a**2*b+3*a*b**2-b**3
# print(one)
# one = a**3 + 3 * a**2 * b + 3 * a * b**2 - b**3
# print(one)
# one = (a + b)*(a**2 - a*b + b**2)
# print(one)
# one = (a - b)*(a**2 - a*b + b**2)
# print(one)
import math
from functools import reduce

#---------------


#
# a = 3
# b = 4
# c = 5
#
# f1 = a*a
# f2 = a+c
# f3 = f2 ** 2
# g1 = f1 + f3
# print("g1: ", g1)
# h1 = 10*b
# h2 = g1 / h1
#
# j1 = c ^ 2
# j2 = a*j1
# j3 = 4 * j2
#
# k1 = h2 - j3
# print( k1)
#
# er = -1/2
# finish = k1**er
# print(finish)


#--------------
# print(math.log(4, 2))
# p= []
# l = 0
# count = 3
# for i in range(count):
#   p.append(float(input()))
# for i in range(len(p)):
#     l += p[i]*math.log(p[i], 2)
#
# print(-(round(l, 4)))

num = 0.1
while num <= 0.3:
    num+=0.1
    print(num)

num = round(num,1)
print(num)
