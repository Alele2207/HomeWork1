import numpy as np

def game_core_v3(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    count = 0
    predict_number = 50 #предположим, что загаданное число равно половине
    step = predict_number/2
    while count < 20:
        if number > predict_number:
            predict_number = int(predict_number)+int(step)
            if step > 1:
                step = int(step/2)
            else:
                step = 1
            count += 1
        elif number < predict_number:
            predict_number = int(predict_number)-int(step)
            if step > 1:
                step = int(step/2)
            else:
                step = 1
            count += 1
        else:
            return count

game_core_v3()

def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls)) # находим среднее количество попыток

    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)

# RUN
score_game(game_core_v3)
