ArifmOrGeom = int(input("0 - арифметиеская прогрессия / 1 - геометрическая"))
FormulaOrCicle = int(input("0 - формула / 1 - цикл"))

firstNumber = int(input("Первое число"))
raznoct = int(input("Разность"))
lastNumber = int(input("Последнее число"))
num = firstNumber

#------Arifm------
if ArifmOrGeom == 0:

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