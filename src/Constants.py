import pygame

class Constants:

    ROWS = 30
    WIDTH = 750
    SIZE_CUBE = WIDTH // ROWS
    INITIAL_SNAKE_POS = 10*SIZE_CUBE, 10*SIZE_CUBE
    RED = 255, 0, 0
    YELLOW = 255, 255, 0
    COOKIE_COLOR = 0, 255, 0
    BLACK = 0, 0, 0
    KEY_LIST1 = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]
    KEY_LIST2 = [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w]
