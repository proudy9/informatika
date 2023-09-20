from math import *

def task1(x, y, z):
    a = (sinh(x) - sinh(y)) / (cosh(x) + cosh(y))
    b = (sin(x))**2 + (cos(z))**2 + log(e**(-z) + e**(-9))
    return a, b
print(f'Задание 1:\nзначения a и b:{task1(x=int(input("Введите значение x: ")), y=int(input("Введите значение y: ")), z=int(input("Введите значение z: ")))}')
