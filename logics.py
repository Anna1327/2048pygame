import random
import pygame

SIZE_BLOCK = 110
MARGIN = 10


def block_coordinates():
    d = []
    k = 55
    z = 160
    for i in range(k, 416, 120):
        for j in range(z, 521, 120):
            d.append([i,j])
    return d

print(block_coordinates())




def pretty_print(mas):
    print('-' * 10)
    for _ in mas:
        print(*_)
    print('-' * 10)


def get_number_from_index(i, j):
    return i * 4 + j + 1


def get_index_from_number(num):
    '''
    функция обратного преобразования:
    по значению получаем координаты элемента на плоскости

    :return:
    '''

    num -= 1
    x, y = num // 4, num % 4
    return x, y


def get_empty_list(mas):
    '''
    функция прямого преобразования:
    по координатам элемента на плоскости получаем значение
    :return:
    '''

    empty = []
    for i in range(4):
        for j in range(4):
            if mas[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


def insert_2_or_4(mas, x, y):
    '''
        функция вставляет 2 или 4 в наш массив
        :return:
        '''
    if random.random() <= 0.75:
        mas[x][y] = 2
    else:
        mas[x][y] = 4
    return mas


def is_zero_in_mas(mas):
    '''
            функция проверяет, есть ли в массиве незаполненная клетка
            :return:
            '''
    for row in mas:
        if 0 in row:
            return True
    return False


def print_mas_on_screen(mas):
    pass


def convert_item_to_string(mas):
    k = []
    for i in range(4):
        for j in range(4):
            d = str(mas[i][j])
            k.append(d)
    return k
