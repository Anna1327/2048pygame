from logics import *


import sys

mas = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]

WHITE = ((255, 255, 255))
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
BLOCKS = 4
SIZE_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + MARGIN * (BLOCKS + 1)
HEIGHT = WIDTH + SIZE_BLOCK
TITLE_REC = pygame.Rect(0, 0, WIDTH, SIZE_BLOCK)


# положили в массив два значения
mas[1][2] = 2
mas[3][0] = 4
print(convert_item_to_string(mas))
# print(convert_item_to_string(mas))

pretty_print(mas)

print(get_empty_list(mas))
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Classic 2048")

clock = pygame.time.Clock()
FPS = 60
'''
положить в массив два значения +
начать цикл игры:
    ждать от пользователя команды - pygame
    когда получим команду - обрабатывать массив - pygame
    найти пустые клетки
    если есть пустые клетки, случайно выбрать одну из них
    и положить туда либо 2 либо 4
    если пустых клеток нет и нельзя двигать массив - игра закончена

'''
# начинаем цикл игры

while is_zero_in_mas(mas):
    events = pygame.event.get()
    clock.tick(FPS)

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

        elif event.type == pygame.KEYDOWN:
            pygame.draw.rect(screen, WHITE, TITLE_REC)
            for row in range(BLOCKS):
                for colomn in range(BLOCKS):
                    w = colomn * SIZE_BLOCK + (colomn + 1)*MARGIN
                    h = row * SIZE_BLOCK + (row + 1) * MARGIN + SIZE_BLOCK
                    r = pygame.draw.rect(screen,GRAY, (w, h, SIZE_BLOCK, SIZE_BLOCK))
                    #получить из массива список элементов из строк convert_item_to_string(mas)
                    #создать функцию, которая будет определять координаты блоков block_coordinates()
                    #прорисовывать значения элементов
                    font = pygame.font.SysFont('Calibri', 50, True, False)
                    text = font.render("2", True, YELLOW)
                    screen.blit(text, [SIZE_BLOCK / 2, 160])
                    screen.blit(text, [175, 160])
                    screen.blit(text, [295, 160])

            # ждем от пользователя команды
            #input()
            # найти пустые клетки
            empty = get_empty_list(mas)
            random.shuffle(empty)
            # здесь будет находиться значение, которое мы будем заполнять случайным числом
            random_num = empty.pop()
            x, y = get_index_from_number(random_num)
            mas = insert_2_or_4(mas, x, y)
            print(f'Мы заполнили элемент под номером {random_num}')
            pretty_print(mas)

    pygame.display.update()

'''
https://younglinux.info/pygame/key
http://programarcadegames.com/index.php?lang=ru&chapter=introduction_to_graphics
http://programarcadegames.com/index.php?chapter=bitmapped_graphics_and_sound&lang=ru
'''