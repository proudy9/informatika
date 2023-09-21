from math import *
# def task1(x, y, z):
#     a = (sinh(x) - sinh(y)) / (cosh(x) + cosh(y))
#     b = (sin(x))**2 + (cos(z))**2 + log(e**(-z) + e**(-9))
#     return a, b
# print(f'Задание 1:\nзначения a и b:{task1(x=int(input("Введите значение x: ")), y=int(input("Введите значение y: ")), z=int(input("Введите значение z: ")))}')

# def task2(x):
#     a = -3
#     b = -1
#     return a * (((x**b + x) / 3 ) - (x**b)**(1/4))
# print(f'Проверка 2 задания:\n{task2(5)}, {task2(9)}, {task2(17)}')

# def task3(x):
#     return sinh(x**(1/3)) + cosh(x**(1/3))
# print(f'Проверка 3 задания:\n{task3(5)}, {task3(9)}, {task3(17)}')

# def task4(r, h):
#     Нахождение стороны через радиус
#     a = 2*r
#     return (4 * a) * h
# print(f'Проверка задания 4:\n{task(4, 8)}, {task5(5, 9)}, {task5(45, 70)}')

# def task5(m1, v1, m2, v2, m3):
#     # Расчет общей импульсной массы
#     total_impulse_mass = m1 + m2
#
#     # Расчет общей импульсной скорости
#     total_impulse_velocity = (m1 * v1 + m2 * v2) / total_impulse_mass
#
#     # Расчет скорости третьего осколка
#     v3 = total_impulse_velocity * total_impulse_mass / (total_impulse_mass + m3)
#     return v3
# # Ввод данных
# m1 = float(input("Введите массу первого осколка (кг): "))
# v1 = float(input("Введите скорость первого осколка (м/с): "))
# m2 = float(input("Введите массу второго осколка (кг): "))
# v2 = float(input("Введите скорость второго осколка (м/с): "))
# m3 = float(input("Введите массу третьего осколка (кг): "))
#
# # Вычисление скорости третьего осколка
# v3 = task5(m1, v1, m2, v2, m3)
#
# # Вывод результата
# print("Скорость третьего осколка: ", v3, "м/с")

# def task6(cylinder_volume):
#     # Радиус цилиндра
#     r = sqrt(cylinder_volume / (pi * 2))
#
#     # Высота призмы
#     prism_height = r * 2
#
#     # Площадь основания призмы
#     prism_base_area = pi * r ** 2
#
#     # Объем призмы
#     prism_volume = prism_base_area * prism_height
#
#     return prism_volume
#
#
# # Ввод объема цилиндра
# cylinder_volume = float(input("Введите объем цилиндра (м^3): "))
#
# # Вычисление объема призмы
# prism_volume = task6(cylinder_volume)
#
# # Вывод результата
# print("Задание 6:\nОбъем призмы: ", prism_volume, "м^3")

# def task7(x1, x2):
#     distance = abs(x2 - x1)
#     return distance
#
# # Ввод координат точек
# x1 = float(input("Введите координату x1: "))
# x2 = float(input("Введите координату x2: "))
#
# # Вычисление расстояния
# distance = task7(x1, x2)
# print("Расстояние между точками:", distance)

# def task8(m, r, F):
#     # Перевод силы трения из кН в Н
#     F = F * 1000
#
#     # Расчет максимальной скорости
#     v = sqrt((F * r) / m)
#     return v
#
# # Ввод данных
# m = float(input("Введите массу автомобиля (кг): "))
# r = float(input("Введите радиус поворота (м): "))
# F = float(input("Введите максимальную силу трения (кН): "))
#
# # Вычисление максимальной скорости
# maximum_speed = task8(m, r, F)
# print("Наибольшая скорость автомобиля на повороте без заноса:", maximum_speed, "м/с")

# def task9(yuan, commission):
#     # Комиссия в процентах
#     commission1 = yuan_amount * commission / 100
#
#     # Сумма после вычета комиссии
#     converted_amount = yuan_amount - commission1
#
#     # Конвертация из юаней в доллары
#     dollar_amount = converted_amount / 8.5  # Предполагаемый курс обмена
#
#     # Округление суммы до 2 знаков после запятой
#     rounded_amount = round(dollar_amount, 2)
#
#     return rounded_amount
#
# yuan_amount = float(input("Введите сумму в юанях: "))
# commission_rate = float(input("Введите комиссию в процентах: "))
#
# # Конвертация в доллары с учетом комиссии и округление
# dollar_amount = task9(yuan_amount, commission_rate)
# print("Сумма в долларах:", dollar_amount)
