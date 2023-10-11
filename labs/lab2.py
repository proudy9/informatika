def is_perfect_square(num):
    if num < 0:
        return False
    sqrt = isqrt(num)
    return sqrt ** 2 == num

def is_less_than(num, limit):
    return num < limit

while True:
    user_input = input('Введите число для продолжения проверки или "exit" для выхода')
    if user_input.lower() == "exit":
        break

    try:
        number = float(user_input)
        print(f'Число {number} является квадратом целого числа {is_perfect_square(number)}')
