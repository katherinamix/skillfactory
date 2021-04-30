import numpy as np

number = np.random.randint(1, 101)  # загадали число
print ("Загадано число от 1 до 100")


def score_game(game_core):
    """Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число"""
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, 101, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return score


def game_core_v2(number):
    """Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток"""
    count = 1
    predict = np.random.randint(1, 101)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count  # выход из цикла, если угадали


def game_core_v3(number):
    """Решаем методом деления отрезка пополам"""
    count = 1
    # находим середину из возможного диапазона - предполагаемое значение
    predict = 100 // 2
    while number != predict:
        count += 1
        if number > predict:
            """Если загаданное число больше величины половины отрезка,
            то его значение находится в промежутке от предполагаемого значения до самого загаданного числа"""
            predict = int((predict + 1 + number) // 2)
        elif number < predict:
            """Если загаданное число меньше величины половины отрезка, 
            то его значение находится в промежутке от 1 до предполагаемого значения"""
            predict = int((predict - 1) // 2)
    return count  # выход из цикла, если угадали


# Проверяем
score_game(game_core_v2)
score_game(game_core_v3)
