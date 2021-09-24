import pygame, sys
from src.Cookie import Cookie
from src.Snake import Snake
from src.Utils import Utils
from src.Constants import Constants


def main():
    pygame.init()
    win = pygame.display.set_mode((Constants.WIDTH, Constants.WIDTH))
    pygame.display.set_caption("Snake Game with 2 player")

    #key_list1 = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_DOWN, pygame.K_UP]
    snake1 = Snake(Constants.RED, Constants.KEY_LIST1)
    #key_list2 = [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w]
    snake2 = Snake(Constants.YELLOW, Constants.KEY_LIST2)
    snake_list = [snake1, snake2]
    cookie = Cookie(snake1)
    flag = True
    clock = pygame.time.Clock()  # create an object to help track time
    while flag:
        # pause the program for an amount of time
        pygame.time.delay(90)
        # clock.tick(60) # Now your game will be capped at FPS fps
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     keys = pygame.key.get_pressed()
        Utils.which_snake(snake_list)
        Utils.check_crossing(snake_list, cookie)
        Utils.redraw_window(win, Constants.ROWS, Constants.WIDTH, snake_list, cookie)


if __name__ == '__main__':
    main()
