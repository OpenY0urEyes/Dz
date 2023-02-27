import math
import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
#
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

#
# d = b**2 - 4*a*c
# print(math.sqrt(d))
#
# if d < 0:
#     print("Нет корней")
# elif d == 0:
#     x = -(b/2*a)
#     print("x = ", x)
# else:
#     x_1 = (-b + math.sqrt(d))/(2*a)
#     x_2 = (-b - math.sqrt(d))/(2*a)
#     print("Первый X = ",x_1)
#     print("Второй X = ",x_2)
"""
x = []
y = []
count = int(input("введите количество x"))
for i in range(0, count):
    x.append(float(input()))

print(x)
for i in range(len(x)):
    y.append(((a*x[i])**2) + (b*x[i]) + c)

print("y = ", y)

fig, ax = plt.subplots()  # Create a figure containing a single axes.
ax.plot(x, [1, 4, 2, 3])  # Plot some data on the axes.

plt.show()"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = x**2 + 2*x + 2

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
