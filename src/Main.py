import pygame
from src.Cookie import Cookie
from src.Snake import Snake
from src.Utils import Utils
from src.Constants import Constants


def main():
    pygame.init()
    win = pygame.display.set_mode((Constants.WIDTH, Constants.WIDTH))
    pygame.display.set_caption("Snake Game with 2 player")

    snake1 = Snake(Constants.RED)
    snake2 = Snake(Constants.YELLOW)
    snake_list = [snake1, snake2]
    cookie = Cookie(snake1)
    flag = True
    clock = pygame.time.Clock()  # create an object to help track time
    while flag:
        # pause the program for an amount of time
        pygame.time.delay(90)
        # clock.tick(60) # Now your game will be capped at FPS fps
        for snake in snake_list:
            snake.move()
        Utils.check_crossing(snake_list, cookie)
        Utils.redraw_window(win, Constants.ROWS, Constants.WIDTH, snake_list, cookie)


if __name__ == '__main__':
    main()
