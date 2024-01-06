import os
import random
import string

def print_char_list(array):
    for char in array:
        print(char, end=' ')

def task1():
    def proverka1(array, symbol):
        if symbol in array:
            print(f"Символ '{symbol}' входит в последовательность.")
        else:
            print(f"Символ '{symbol}' не входит в последовательность.")

    def proverka2(array, first_symbol, second_symbol):
        count_pairs = sum(1 for i in range(len(array) - 1) if array[i] == first_symbol and array[i + 1] == second_symbol)
        print(f"Количество пар символов '{first_symbol}{second_symbol}': {count_pairs}.")

    def proverka3(array):
        count_pairs = sum(1 for i in range(len(array) - 1) if array[i] == array[i + 1])
        print(f"Количество пар соседствующих одинаковых символов: {count_pairs}.")

    def proverka4(array):
        for i in range(1, len(array) - 2):
            if array[i] == array[i + 1] and array[i + 2] == array[i + 3]:
                print("Существуют такие i и j, что условие proverka4 выполняется.")
                return
        print("Условие proverka4 не выполняется.")

    def proverka5(array):
        count_spaces = sum(1 for char in array if char.isspace())
        print(f"Количество пробелов в массиве: {count_spaces}.")

    n = int(input("Введите количество элементов в массиве: "))
    char_array = [input(f"Введите символ {i + 1}: ") for i in range(n)]
    print_char_list(char_array)

    proverka1(char_array, input("Введите символ для проверки (proverka1): "))
    proverka2(char_array, input("Введите первый символ для проверки (proverka2): "), input("Введите второй символ для проверки (proverka2): "))
    proverka3(char_array)
    proverka4(char_array)
    proverka5(char_array)

def task3():
    keyword = "stop"  # Заданное ключевое слово
    file_path = "F:/laba/Lab 3/data/output.txt"  # Путь к файлу для записи

    while True:
        print("Введите текст:")
        user_input = input()  # Запрос ввода строки от пользователя

        if user_input.lower() == keyword:  # Проверка на ключевое слово
            print("Программа завершена.")
            break

        with open(file_path, "a") as file:  # Открытие файла на дозапись
            file.write(user_input + "\n")  # Запись строки в файл
def task5():
    n = int(input("Введите количество строк: "))

    with open('data/output_task5.txt', 'w') as file:
        print("Введите текст:")
        for i in range(n):
            text = input()
            file.write(text + '\n')

def task7():
    # Шаг 1: Ввод массива расширений файлов
    extensions = input("Введите расширения файлов через пробел: ").split()

    # Шаг 2: Создание директорий
    for extension in extensions:
        os.makedirs(extension, exist_ok=True)

    # Шаг 3: Создание файлов
    for _ in range(10):
        # Генерация случайного имени файла
        filename = ''.join(random.choices(string.ascii_lowercase, k=5))
        # Генерация случайного расширения файла из массива
        extension = random.choice(extensions)
        # Создание файла
        open(f"{filename}.{extension}", 'w').close()

    # Шаг 4: Вывод списка файлов
    files = os.listdir()
    print("Список файлов:")
    for file in files:
        print(file)

    # Шаг 5: Ожидание нажатия клавиши
    input("Нажмите любую клавишу для переноса файлов ...")

    # Шаг 6: Перенос файлов в соответствующие директории
    for file in files:
        if '.' in file:
            extension = file.split('.')[-1]
            if extension in extensions:
                os.rename(file, os.path.join(extension, file))

def print_string_list(array):
    for element in array:
        print(element)

def get_string_array_from_console():
    array = []
    for _ in range(10):
        element = input("Введите элемент массива: ")
        array.append(element)
    return array

def proverka(array1, array2):
    for i in range(len(array1)):
        if array1[i] in array2:
            array1[i] += " ✔"
        else:
            array1[i] += " (not found)"

def task4():
    # Шаг 1: Задание массива строк
    array = [
        "website1",
        "app2",
        "social_network3",
        "term1",
        "website2",
        "app1",
        "social_network1",
        "term2",
        "website3",
        "app3"
    ]

    # Шаг 2: Получение массива строк с консоли
    user_array = get_string_array_from_console()

    # Шаг 3: Проверка и модификация массива
    proverka(user_array, array)

    # Шаг 4: Вывод модифицированного массива
    print_string_list(user_array)
