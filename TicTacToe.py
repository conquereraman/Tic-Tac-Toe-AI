import pygame
import time

pygame.init()
width = 300
height = 300
pygame.display.set_caption('Tic Tac Toe')
win = pygame.display.set_mode((width, height))
rows, columns = 3, 3
red = (255, 0, 0)
blue = (0, 255, 0)
white = (255, 255, 255)
FPS = 60
block_size = 100
from numpy import Infinity, negative

a = [' ' for x in range(10)]
radius = [0, (50, 50), (150, 50), (250, 50), (50, 150), (150, 150), (250, 150), (50, 250), (150, 250), (250, 250)]


def player_make_move(pos):
    global a
    a[pos] = 'X'


def computer_makes_move(pos):
    global a
    a[pos] = 'O'
    if (pos == 1):
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif (pos == 2):
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif (pos == 3):
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif pos == 4:
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif pos == 5:
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif pos == 6:
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif pos == 7:
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif pos == 8:
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass
    elif pos == 9:
        pygame.draw.circle(win, blue, radius[pos], 25)
        pygame.display.flip()
        pass


def tie(a):
    if (a.count(' ') > 1):
        return False
    else:
        return True


def winner(a, symbol):
    if (a[3] == a[5] == a[7] == symbol):
        return True
    elif (a[1] == a[2] == a[3] == symbol):
        return True
    elif (a[4] == a[5] == a[6] == symbol):
        return True
    elif (a[7] == a[8] == a[9] == symbol):
        return True
    elif (a[1] == a[4] == a[7] == symbol):
        return True
    elif (a[2] == a[5] == a[8] == symbol):
        return True
    elif (a[3] == a[6] == a[9] == symbol):
        return True
    elif (a[1] == a[5] == a[9] == symbol):
        return True
    return False


def check_block(x, y):
    if x <= block_size and y <= block_size:
        player_make_move(1)
        return 25, 25
    elif x <= 2 * block_size and y <= block_size:
        player_make_move(2)
        return 125, 25
    elif x <= 3 * block_size and y <= block_size:
        player_make_move(3)
        return 225, 25
    if x <= block_size and y <= 2 * block_size:
        player_make_move(4)
        return 25, 125
    elif x <= 2 * block_size and y <= 2 * block_size:
        player_make_move(5)
        return 125, 125
    elif x <= 3 * block_size and y <= 2 * block_size:
        player_make_move(6)
        return 225, 125
    elif x <= block_size and y <= 3 * block_size:
        player_make_move(7)
        return 25, 225
    elif x <= 2 * block_size and y <= 3 * block_size:
        player_make_move(8)
        return 125, 225
    elif x <= 3 * block_size and y <= 3 * block_size:
        player_make_move(9)
        return 225, 225


def minimax(b, ismaximising):
    if (winner(b, 'O')):
        return 100
    elif (winner(b, 'X')):
        return -1
    elif (tie(b)):
        return 0
    if (ismaximising == True):
        best = -Infinity
        for i in range(1, 10):
            if (b[i] == ' '):
                b[i] = 'O'
                scoring = minimax(b, False)
                b[i] = ' '
                best = max(best, scoring)
        return best
    elif (ismaximising == False):
        best = Infinity
        for i in range(1, 10):
            if (b[i] == ' '):
                b[i] = 'X'
                scoring = minimax(b, True)
                b[i] = ' '
                best = min(best, scoring)
        return best


def computer_move():
    global a
    best_score = -Infinity
    for i in range(1, 10):
        if (a[i] == ' '):
            a[i] = 'O'
            score = minimax(a, False)
            a[i] = ' '
            if (score > best_score):
                best_score = score
                move = i
    computer_makes_move(move)


for i in range(0, 300, block_size):
    for j in range(0, 300, block_size):
        rect = pygame.Rect(i, j, block_size, block_size)
        pygame.draw.rect(win, white, rect, 1)
pygame.display.update()


def player_turn():
    x, y = pygame.mouse.get_pos()
    center = check_block(x, y)
    sq = pygame.Rect(center[0], center[1], 50, 50)
    pygame.draw.rect(win, red, sq)
    pygame.display.flip()


def main():
    run = True
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                player_turn()
                if winner(a, 'X'):
                    time.sleep(.5)
                    win.fill(white)
                    myfont = pygame.font.SysFont('Comic Sans MS', 30)
                    textsurface = myfont.render('You Won', False, (0, 0, 0))
                    win.blit(textsurface, (20, 20))
                    pygame.display.update()
                if (tie(a)):
                    time.sleep(.5)
                    win.fill(white)
                    myfont = pygame.font.SysFont('Comic Sans MS', 30)
                    textsurface = myfont.render('Its A Tie', False, (0, 0, 0))
                    win.blit(textsurface, (20, 20))
                    pygame.display.update()
                else:
                    computer_move()
                    if winner(a, 'O'):
                        time.sleep(.5)
                        win.fill(white)
                        myfont = pygame.font.SysFont('Comic Sans MS', 30)
                        textsurface = myfont.render('Computer Won', False, (10, 10, 10))
                        win.blit(textsurface, (20, 20))
                        pygame.display.update()


main()
