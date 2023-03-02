ArifmOrGeom = int(input("0 - арифметиеская прогрессия / 1 - геометрическая"))
FormulaOrCicle = int(input("0 - формула / 1 - цикл"))

firstNumber = int(input("Первое число"))
raznoct = int(input("Разность"))
lastNumber = int(input("Последнее число"))
num = firstNumber

#------Arifm------
if ArifmOrGeom == 0:

<<<<<<< HEAD
    if FormulaOrCicle == 0:
            #---Formula---
        while firstNumber < lastNumber:
            firstNumber += raznoct
            print(firstNumber)
    elif FormulaOrCicle == 1:
    #---Cicle---
        for i in range(firstNumber, lastNumber, raznoct):
            print(i)
elif ArifmOrGeom == 1:
    if FormulaOrCicle == 0:
            #---Formula---
        while firstNumber < lastNumber:
            firstNumber *= raznoct
            print(firstNumber)
    elif FormulaOrCicle == 1:
            #---Cicle---
        for i in range(firstNumber, lastNumber):
            if num < i:
                num *= raznoct
                print(num)
=======
print("y = ", y)

fig, ax = plt.subplots() 
ax.plot(x, [1, 4, 2, 3]) 

plt.show()"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = x**2 + 2*x + 2

fig, ax = plt.subplots()
ax.plot(x, y)
plt.show()
>>>>>>> 3fa26c1680db4d3f661b02a79a2edb8fb431c8e9
