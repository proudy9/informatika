# Вариант №33
# Задание 1
from math import *
def task1():
    def is_perfect_square(num):
        a = num
        sqrt = isqrt(a)
        return sqrt ** 2 == a

    def is_less_than(num, limit):
        return num < limit

    while True:
        number = int(input('Введите число для проверки: '))
        if number < 0:
            print('Проверка не пройдена, введите число > 0')
            continue
        limitt = int(input('Введите лимит: '))
        if (is_perfect_square(number) and is_less_than(number, limitt)) == True:
            print('Проверка прошла успешно!')
        else:
            print('Проверка не пройдена!')

task1()
# Задание 2
from math import *
import matplotlib.pyplot as plt

def task2():
    a = int(input('Введите начало диапазона: '))
    b = int(input('Введите конец диапазона: '))
    x_znach = []
    y_znach = []

    def func(a, b):
        x = a
        while x <= b+0.00001:
            if x >= 0:
                result_1 = 2 * (e ** (x))
                y_znach.append(result_1)
            if x < 0:
                result_2 = 2 - ((x) ** 3)
                y_znach.append(result_2)
            x_znach.append(x)
            x += 1
        return x_znach, y_znach
    print(func(a, b))
    plt.plot(x_znach, y_znach)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('График функции')
    plt.grid(True)
    plt.show()

task2()
# Задание 3
def task3():
    def number_in_new_numeral_system(number, base):
        new_numeral_system = ""

        while number > 0:
            remainder = number % base
            if remainder < 10:
                new_numeral_system += str(remainder)
            else:
                new_numeral_system += chr(remainder - 10 + ord('A'))
            number //= base

        return new_numeral_system[::-1]

    num = int(input('Введите число: '))
    system = int(input('Введите основание: '))
    print(f'Число в другой системе счисления: {number_in_new_numeral_system(num, system)}')

task3()
# Задание 4
def left_figure(x, y):
    one = (x >= -1) and (y <= 5) and (y >= 1.5*x + 2)
    two = ((x + 1)**2 + (y - 1)**2 <= 4) and (y <= -1*x + 2) and (y >= -0.25*x + 0.5)
    three = ((x + 1)**2 + (y - 1)**2 <= 4) and (y <= -1 * x - 1)
    four = (y <= -3*x - 1) and (y >= -1.5*x - 2.5)
    if one or two or three or four:
        return True

def right_figure(x, y):
    one = ((x - 4)**2 + (y + 1)**2 <= 4) and (y <= 3*x-5) and (y >= -3*x+13) and (y >= -0.5*x+2)
    two = (y <= -0.5*x + 2) and ((x - 4)**2 + (y + 1)**2 <= 4) and (y <= 2*x-8) and (y >= -x + 1)
    three = ((x - 4)**2 + (y + 1)**2 >= 4) and (y <= -2*x + 11) and (y >= x - 10) and (y >= -0.5*x -2.5) and (y <= x - 7)
    if one or two or three:
        return True

def task4(x ,y):
    if right_figure(x, y) == True:
        print('Точка попала в правую фигуру!')
    elif left_figure(x, y) == True:
        print('Точка попала в левую фигуру!')
    else:
        print('Точка не попала ни в одну из фигур!')

x = int(input("Введите X: "))
y = int(input("Введите Y: "))

print(task4(x, y))

# Задание 5
# Функция для определения последней цифры числа
def task5():

    # Функция для определения последней цифры
    def last(digit_3):
        return digit_3 % 10

    # Функция для проверки нечетности числа
    def nechet(digit_3):
        if digit_3 % 2 != 0:
            return True
        else:
            return False

    # Запрос ввода трех чисел
    digit_1 = int(input("Введите первое число: "))
    digit_2 = int(input("Введите второе число: "))
    digit_3 = int(input("Введите третье число: "))

    # Вычисление суммы последних цифр
    summ = last(digit_1) + last(digit_2) + last(digit_3)

    # Проверка нечетности суммы последних цифр
    if nechet(summ):
        # Если сумма нечетная, проверяем нечетность последней цифры суммы
        if nechet(last(summ)):
            print("Сумма последних цифр чисел", digit_1, digit_2, digit_3, "является нечетной, и последняя цифра суммы также нечетная.")
        else:
            print("Сумма последних цифр чисел", digit_1, digit_2, digit_3, "является нечетной, но последняя цифра суммы - четная.")
    else:
        print("Сумма последних цифр чисел", digit_1, digit_2, digit_3, "является четной.")

task5()
# Задание 6
def task6():
    def is_happy(number):
        number_str = str(number).zfill(6)
        first_half = list(map(int, number_str[:3]))
        second_half = list(map(int, number_str[3:]))
        if sum(first_half) == sum(second_half):
            return print(f'Ваш билет под номером {number} является счастливым!')
        else:
            return print(f'Ваш билет под номером {number} является несчастливым!')

    print(is_happy(int(input('Введите номер билета: '))))
task6()
# Задание 8
import math

def task8(x, epsilon):
    sum = 0
    term = x
    sign = -1
    factorial = 1

    i = 0
    while abs(term) >= epsilon:
        sum += term
        term *= x**2 / ((2*i+2)*(2*i+3))
        term *= sign
        term /= factorial
        sign *= -1
        factorial += 2
        i += 1

    return sum

x = int(input('Введите значение x: '))  # Значение x
epsilon = 1e-6  # Заданная точность

series_sum = task8(x, epsilon)
print("Сумма ряда:", series_sum)
# Задание 9
def task9():
    def task9_1():
        result = 0
        for i in range(1, 9):
            for j in range(1, i+1):
                result += (j + 2*i)**2
        return result

    def task9_2():
        result = 1
        for i in range(1, 4):
            for j in range(i, 2*i+1):
                result *= j
        return result

    def task9_3():
        result = 1
        for i in range(1, 9):
            inner_sum = 0
            for j in range(i, 2*i):
                inner_sum += sum(2*j - 3*(i - 0.5*k) for k in range(i+j, 2*(i+j)+1))
            result *= inner_sum
        return result
    print(f'1) {task9_1()}, 2) {task9_2()}, 3) {task9_3()}')

task9()
# Задание 10
import math
def task10():
    def sin_3(x, epsilon):
        result = 0  # Инициализируем переменную для хранения результата
        term = 1  # Инициализируем переменную для текущего члена ряда
        i = 1  # Инициализируем переменную для счетчика итераций

        while abs(term) > epsilon:  # Пока абсолютное значение текущего члена больше заданной погрешности
            result += term  # Прибавляем текущий член к результату
            term = ((-1) ** (i+1)) * ((3 ** (2*i + 1) - 3) / math.factorial(2*i + 1)) * (x ** (2*i + 1))  # Вычисляем новый член ряда
            i += 1  # Увеличиваем счетчик итераций

        return (1/4) * result  # Возвращаем приближенное значение функции sin^3(x)

    x = int(input('Введите x: '))  # Задаем значение x
    epsilon = 1e-6  # Задаем заданную погрешность

    sin3 = sin_3(x, epsilon)  # Вычисляем приближенное значение функции sin^3(x)
    exact_value = math.sin(x) ** 3  # Вычисляем точное значение функции sin^3(x)

    print("Приближенное значение функции sin^3(x):", sin3)  # Выводим приближенное значение
    print("Точное значение функции sin^3(x):", exact_value)  # Выводим точное значение
    print("Разница между точным и приближенным значением:", abs(sin3 - exact_value))  # Выводим разницу между приближенным и точным значениями

task10()
