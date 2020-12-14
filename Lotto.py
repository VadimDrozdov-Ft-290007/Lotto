# -*- coding: utf-8 -*-
import random

# Бесконечный цикл для огранизации работы программы
while True:
    
    # Обработка ошибок при вводе N (числа бочонков)
    try:
        N = int(input('Введите натуральное число N - число бочонков: '))
    except ValueError:
        print('Вы ввели неверный символ! Попробуйте ещё раз.')
        continue
    if N < 1:
        print('Вы должны ввести натуральное число! Попробуйте ещё раз.')
        continue
    
    memory = [] # Список для хранения вытащенных бочонков
    for i in range(1, N+1):
        enter = input('Нажмите Enter, чтобы вытащить бочонок из мешка...')

        # Бесконечный цикл для отбора бочонков, которые пользователь ещё не вытаскивал
        while True:
            replay = 0 # Переменная, содержащая информацию о повторе бочонка
            number = random.randint(1, N)
            for row in memory:
                if number == row:
                    replay = 1
                    break
            if replay == 1: continue
            memory.append(number)
            print('Вы вытащили бочонок с номером', number)
            break
        
    print('\nВы вытащили все бочонки!', '\nНажмите Enter, если хотите закрыть программу, введите любой символ, если хотите начать заново.', sep = '\n')
    change = input('>>')
    if change == '': break