# imports
import time
from random import *
from time import *

# variables
balance = 0
name = None


# first "HI" functions
def get_money():
    global balance
    balance += 15000
    return balance


def start():
    get_money()
    print('Приветствую вас в моем анти-луз-мани казино!\n\n')
    sleep(1.5)
    print(
          'Вы получили ваш первый деп\n'
          f'Ваш баланс составляет = {balance} руб\n'
          'Желаю удачи и не играть в настоящие лохотроны:)\n')


def check_balance():
    global balance
    answer = f'Ваш баланс составляет {balance} руб'
    return answer


# Games
def random_multiplier():
    multiplier = randint(1, 100)
    print(f'Ваш множитель равен = {multiplier}x')
    return multiplier


def roulette():
    sleep(3)
    global balance
    attempt = 1000

    answer = input('Игра - Рулетка\n'
                   f'Цена игры - {attempt}\n'
                   'Нажмите [enter], если хотите продолжить :)\n'
                   'Напишите любой символ, если хотите выйти :(\n')

    if answer != '':
        return None

    while True:
        sleep(1)
        balance -= attempt
        chance = randint(1, 100)
        prize = None
        if chance <= 70:
            prize = randint(1, 1000)
            print('Вы проиграли.\n'
                  f'Ваш выигрыш составил {prize} руб\n')
        if 70 < chance < 90:
            prize = randint(1000, 50000)
            print('Вы выиграли!\n'
                  f'Ваш выигрыш составил {prize} руб\n')
        if 90 <= chance <= 99:
            prize = randint(50000, 200_000)
            print('Вы сорвали большой куш!\n'
                  f'Ваш выигрыш составил {prize} руб\n')
        if chance == 100:
            prize = 1_000_000
            print('JACKPOT\n')
            print(f'Ваш выигрыш составил {prize} руб\n')
        balance += prize

        sleep(3)
        again = input('Хотите сыграть еще?\n'
                      f'{check_balance()}\n'
                      'Нажмите [enter], если хотите продолжить :)\n'
                      'Напишите любой символ, если хотите выйти :(\n')
        if again != '':
            break


start()
roulette()
