# Консоль, куда будет выводиться ход игры.
# Размер поля предполагается равным 3x3, 9 клеток, массив
#   0  1  2
# 0 00 10 20
# 1 01 10 21
# 2 02 12 22

# предлложить выбрать кем игарет пользователь
# ход компьютера зависит от ходов игрока и расположения символов на поле
# отображать каждый ход на поле, не удаляя предыдущее значение, дополняя
# за счет чего значение в клетках будет изменяться?
# предлагать ввести ход
# Ход вводится координатами x y
# проверять входит ли координата в поле
# проверять занята ли клетка
# поле закончилось "ничья"
# победная комбинация выпала у игрока "победа"
# победная комбинация выпала у компа "проиграл"


from random import randint

VERTICAL = ('0', '1', '2')


def role():
    choice = input('Кем будешь играть? (x, 0): ')
    while choice not in ('x', '0'):
        print('Такого нет. Выбери еще раз')
        choice = input('Кем будете играть? Игрок ходит первым (x, 0): ')
    return choice


def horizontal(field):
    print(' ', '0', '1', '2')
    for y, v in enumerate(VERTICAL):
        print(v, ' '.join(field[y]))


def game_field(field):
    count = 0
    for y in range(3):
        if ' ' in field[y]:
            count += 1
    print("Count: " + str(count))
    return count == 0


def user_step(field):
    n_x, n_y = 0, 0
    while True:
        coordinats_x = input('Введи координату x: ')
        coordinats_y = input('Введи координату y: ')
        y = coordinats_y
        x = coordinats_x
        # x gorizont y vertical

        if int(x) not in (0, 1, 2) or y not in VERTICAL:
            print('Координаты вне поля (допустимые символы 0, 1, 2)')
            continue

        n_x, n_y = int(x), VERTICAL.index(y)
        if field[n_y][n_x] == ' ':
            break
        else:
            print('Клетка уже занята')

    return n_x, n_y


def role_opponents(step):
    return '0' if step == 'x' else 'x'


def end_game(step, field):

    opponents_step = role_opponents(step)

    # проверка строк
    for y in range(3):
        if opponents_step not in field[y] and ' ' not in field[y]:
            return True

    # проверка колонки
    for x in range(3):
        column = [field[0][x], field[1][x], field[2][x]]
        if opponents_step not in column and ' ' not in column:
            return True

    # проверка диагоналей
    diagonal = [field[0][0], field[1][1], field[2][2]]
    if opponents_step not in diagonal and ' ' not in diagonal:
        return True
    diagonal = [field[0][2], field[1][1], field[2][0]]

    if opponents_step not in diagonal and ' ' not in diagonal:
        return True
    return False


def computer_step(field):
    # opponents_step = role_opponents(step)
    check = computer
    for i in range(2):
        # проверка строк
        for y in range(3):
            if field[y].count(check) == 2 and ' ' in field[y]:
                return y, field[y].index(' ')

        # проверка колонки
        for x in range(3):
            column = [field[0][x], field[1][x], field[2][x]]
            if column.count(check) == 2 and ' ' in column:
                return column.index(' '), x

        diagonal = [field[0][0], field[1][1], field[2][2]]

        if diagonal.count(check) == 2 and ' ' in diagonal:
            return diagonal.index(' '), diagonal.index(' ')

        diagonal = [field[0][2], field[1][1], field[2][0]]

        if diagonal.count(check) == 2 and ' ' in diagonal:
            if diagonal.index(' ') == 0:
                return 0, 2
            if diagonal.index(' ') == 1:
                return 1, 1
            if diagonal.index(' ') == 2:
                return 2, 0
        check = choice
    angles = [field[0][0], field[2][0], field[0][2], field[2][2]]
    if field[1][1] == choice and ' ' in angles:
        pair_values = [(0, 0), (2, 0), (0, 2), (2, 2)]
        return pair_values[randint(0, angles.count(' ') - 1)]

    x, y = randint(0, 2), randint(0, 2)
    while field[y][x] != ' ':
        x, y = randint(0, 2), randint(0, 2)
    return x, y


field = [
    [' ' for x in range(3)] for y in range(3)
]

choice = role()
computer = role_opponents(choice)

while True:
    horizontal(field)
    x, y = user_step(field)
    field[y][x] = choice
    if end_game(choice, field):
        print('ПОБЕДА')
        break

    if game_field(field):
        print('НИЧЬЯ')
        break

    y, x = computer_step(field)
    field[y][x] = computer
    if end_game(computer, field):
        print('ТЫ ПРОИГРАЛ')
        break
