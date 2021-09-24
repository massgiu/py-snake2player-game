import pygame, sys, random
from src.Cube import Cube
from random import randint
from src.Constants import  Constants

class Snake(object):
    #body_list = []  # lista di cube

    def __init__(self, color, key_list): #left, right, down, up
        self.color = color
        # pos: head position
        pos = (random.randrange(Constants.ROWS) * Constants.SIZE_CUBE, random.randrange(Constants.ROWS) * Constants.SIZE_CUBE)
        self.direction = self.get_direction() #initial direction
        self.head = Cube(pos, color, self.direction)
        self.body_list = [self.head]  #add head (which is a cube object)
        # Dictionary that stores tuple about point of rotations
        self.turns = {}
        self.left = key_list[0]
        self.down = key_list[2]
        self.right = key_list[1]
        self.up = key_list[3]

    def get_direction(self):
        rndm = randint(0, 3)
        if rndm == 0:
            return "UP"
        elif rndm == 1:
            return "DOWN"
        elif rndm == 2:
            return "LEFT"
        elif rndm == 3:
            return "RIGHT"

    def move(self):
        # # Gestore di eventi: intercetto eventi tastiera
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         pygame.quit()
        #         sys.exit()
        #     keys = pygame.key.get_pressed()
        #     #se premo a sx and la direz non è dx e la lunghez >1 oppure se premo a sx e la lunghezza è 1
        #     if (keys[self.left] and self.direction != "RIGHT" and len(self.body_list) > 1) or (
        #             keys[self.left] and len(self.body_list) == 1):
        #         self.direction = "LEFT"
        #     elif (keys[self.right] and self.direction != "LEFT" and len(self.body_list) > 1) or (
        #                     keys[self.right] and len(self.body_list) == 1):
        #         self.direction = "RIGHT"
        #     elif (keys[self.up] and self.direction != "DOWN" and len(self.body_list) > 1) or (
        #                     keys[self.up] and len(self.body_list) == 1):
        #         self.direction = "UP"
        #     elif (keys[self.down] and self.direction != "UP" and len(self.body_list) > 1) or (
        #                     keys[self.down] and len(self.body_list) == 1):
        #         self.direction = "DOWN"
        #     # All'atto della rotazione devo memorizzare la direzione
        #     # Come chiave la posizione della testa, come valore la direzione
        #     self.turns[self.head.pos[:]] = self.direction

        # Implemento il movimento del serpente (indico la direzione per ciascuno blocchetto)
        for index, cub in enumerate(self.body_list):  # body_list è una lista di cube
            # per ciascun blocchetto del body prendo la tupla della posizione (x,y)
            p = cub.pos[:]
            # se la posizione del blocchetto coincide con quella in cui
            # è avvenuta la rotazione della testa
            if p in self.turns:
                direction = self.turns[p]  # prendo la direzione di rotaz dal dizion
                # per ogni blocchetto del body chiamo il metodo move()
                cub.move_cube(direction)  # turn[0]=direzX, turn[1]=direzY
                # se è l'ultimo cubo lo rimuovo
                if index == len(self.body_list) - 1:
                    self.turns.pop(p)
            else:
                # se la direz è sx e la pos_x<0 => riporto la x all'estremo dx
                if cub.direction == "LEFT" and cub.pos[0] <= 0:
                    cub.pos = (Constants.WIDTH - Constants.SIZE_CUBE, cub.pos[1])
                # se la direz è dx e la pos_x è al termine => riporto la x allo 0
                elif cub.direction == "RIGHT" and cub.pos[0] >= Constants.WIDTH:
                    cub.pos = (0, cub.pos[1])
                # se la direz y è down e la pos_y è al termine => riporto la y allo 0
                elif cub.direction == "DOWN" and cub.pos[1] >= Constants.WIDTH + Constants.SIZE_CUBE:
                    cub.pos = (cub.pos[0], 0)
                # se la direz y è up e la pos_y è al termine => riporto la y al termine
                elif cub.direction == "UP" and cub.pos[1] < 0:
                    cub.pos = (cub.pos[0], Constants.WIDTH - Constants.SIZE_CUBE)
                else:  # If we haven't reached the edge just move in our current direction
                    cub.move_cube(cub.direction)

    def add_cube(self):
        tail = self.body_list[-1]
        direction = tail.direction

        # We need to know which side of the snake to add the cube to.
        # So we check what direction we are currently moving in to determine if we
        # need to add the cube to the left, right, above or below.
        if direction == "RIGHT":  # going right (x-1, same y)
            self.body_list.append(Cube((tail.pos[0] - Constants.SIZE_CUBE, tail.pos[1]), self.color, direction))
        elif direction == "LEFT":  # going left (x+1, same y)
            self.body_list.append(Cube((tail.pos[0] + Constants.SIZE_CUBE, tail.pos[1]), self.color, direction))
        elif direction == "DOWN":  # going down (same x, y-1)
            self.body_list.append(Cube((tail.pos[0], tail.pos[1] - Constants.SIZE_CUBE), self.color, direction))
        elif direction == "UP":  # going up (same x, y+1)
            self.body_list.append(Cube((tail.pos[0], tail.pos[1] + Constants.SIZE_CUBE), self.color, direction))

        # We then set the new cube direction to the direction of the snake.
        self.body_list[-1].direction = direction

    # Draw every cube of the body
    def draw(self, surface, color):
        for index, cub in enumerate(self.body_list):
            if index == 0:  # this is head, we need to draw eyes
                cub.draw_cube(surface, True)
            else:
                cub.draw_cube(surface)