import pygame
import random, sys
import tkinter as tk
from tkinter import messagebox

from src.Constants import Constants


class Utils(object):

    @staticmethod
    def draw_grid(width, rows, surface):
        color_line = (128, 128, 128)
        x = 0
        y = 0
        for l in range(rows):
            x = x + Constants.SIZE_CUBE
            y = y + Constants.SIZE_CUBE
            # Vertical line
            pygame.draw.line(surface, color_line, (x, 0), (x, width))
            # Horizontal line
            pygame.draw.line(surface, color_line, (0, y), (width, y))

    # Update display
    @staticmethod
    def redraw_window(surface, rows, width, snk_list, cookie):
        surface.fill(Constants.BLACK)  # Fills the screen with black
        for snake in snk_list:
            snake.draw(surface, snake.color)
        cookie.draw_cube(surface)
        Utils.draw_grid(width, rows, surface)  # Will draw our grid lines
        pygame.display.update()  # Updates the screen

    # This function generates the coordinates x,y for a random cube to eat
    @staticmethod
    def random_cookie(snk):
        while True:  # Keep generating random positions until we get a valid one
            x = random.randrange(Constants.ROWS) * Constants.SIZE_CUBE
            y = random.randrange(Constants.ROWS) * Constants.SIZE_CUBE
            # get a list with all position of snake's cube
            position_list = list(map(lambda z: z.pos, snk.body_list))
            if (x, y) in position_list:  # This wll check if the position we generated is occupied by the snake
                continue
            else:
                break

        return x, y

    @staticmethod
    def message_box(subject, content):
        root = tk.Tk()
        root.attributes("-topmost", True)
        root.withdraw()
        messagebox.showinfo(subject, content)
        try:
            root.destroy()
        except:
            pass

    @staticmethod
    def check_crossing(snake_list, cookie):
        for snake in snake_list:
            for x in range(len(snake.body_list)):
                # Check if snake head overlaps with its body
                if snake.body_list[0].pos in list(map(lambda z: z.pos, snake.body_list[1:])):
                    Utils.you_lost(snake_list)
                #eat cookie
                if snake.body_list[0].pos == cookie.pos:  # Checks if the head collides with cookie
                    snake.add_cube()  # Adds a new cube to the snake
                    cookie.__init__(snake)# creates a new cube object


    @classmethod
    def you_lost(cls, snake_list):
        for snake in snake_list:
            print(f'Snake {snake.color} score is: {len(snake.body_list)-1}')
        Utils.message_box('You Lost!', 'Play again...')
        #for snake in snake_list:
        #    snake.__init__(snake.color)
        snake_list[0].__init__(snake_list[0].color, Constants.KEY_LIST1)
        # key_list2 = [pygame.K_a, pygame.K_d, pygame.K_s, pygame.K_w]
        snake_list[1].__init__(snake_list[1].color, Constants.KEY_LIST2)
        pygame.display.update()

    @classmethod
    def which_snake(cls, snake_list):
        # Gestore di eventi: intercetto eventi tastiera
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            for snake in snake_list:
                #se premo a sx and la direz non è dx e la lunghez >1 oppure se premo a sx e la lunghezza è 1
                if (keys[snake.left] and snake.direction != "RIGHT" and len(snake.body_list) > 1) or (
                        keys[snake.left] and len(snake.body_list) == 1):
                    snake.direction = "LEFT"
                elif (keys[snake.right] and snake.direction != "LEFT" and len(snake.body_list) > 1) or (
                                keys[snake.right] and len(snake.body_list) == 1):
                    snake.direction = "RIGHT"
                elif (keys[snake.up] and snake.direction != "DOWN" and len(snake.body_list) > 1) or (
                                keys[snake.up] and len(snake.body_list) == 1):
                    snake.direction = "UP"
                elif (keys[snake.down] and snake.direction != "UP" and len(snake.body_list) > 1) or (
                                keys[snake.down] and len(snake.body_list) == 1):
                    snake.direction = "DOWN"
                # All'atto della rotazione devo memorizzare la direzione
                # Come chiave la posizione della testa, come valore la direzione
                snake.turns[snake.head.pos[:]] = snake.direction
        for snake in snake_list:
            snake.move()