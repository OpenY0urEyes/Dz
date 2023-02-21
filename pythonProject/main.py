a = int(input())
b = float(input())
c = str(input())
d = complex(input())
ee = bool(input())


print(f"тип данных : {type(a)} используется  для целых чисел")
print(f"тип данных : {type(b)} используется  для для чисел с плавающей запятой")
print(f"тип данных : {type(c)} используется  для строк текста")
print(f"тип данных : {type(d)} используется  для комлпексных чисел")
print(f"тип данных : {type(ee)} используется  для истинных и ложных выражений")

#------------------

print("int - 2 147 483 647")
print("float - 1.8 * 10 в 308 степени")

#------------------

text = "я люблю динамическую типизацию"

print(len(text.encode('utf-8')))
print(len(text.encode('utf-16')))
print(len(text.encode('utf-32')))
print(len(text.encode('cp1251')))

