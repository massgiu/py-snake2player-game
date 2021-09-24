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
    KEY_DICT1 = {"LEFT":pygame.K_LEFT, "RIGHT":pygame.K_RIGHT, "DOWN":pygame.K_DOWN, "UP":pygame.K_UP}
    KEY_DICT2 = {"LEFT":pygame.K_a, "RIGHT":pygame.K_d, "DOWN":pygame.K_s, "UP":pygame.K_w}
