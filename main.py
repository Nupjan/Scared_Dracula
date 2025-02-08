import pygame
from random import choice
from generate_maze import *


# All Images
image = pygame.image.load("Scared_Dracula/Images/garlic.jpg")
Garlic =  pygame.transform.scale(image, (50, 30))
background_img = pygame.image.load("Scared_Dracula/Images/background.jpg")

pygame.init()

# Set display mode to fullscreen
surface = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
game_surface = pygame.Surface(RES)
FPS = 10

pygame.display.set_caption("Scared_Dracula")
clock = pygame.time.Clock() 
# Creating a tile for maze

# COLORS
Black = (0,0,0)
White = (255,255,255)
Red = (255, 0, 0)

maze =generate_maze()



# def add_player(x,y):
#     screen.blit(Garlic, (x, y))
# x, y = 400, 400
running = True

while running:
    surface.blit(background_img, (WIDTH, 0))
    surface.blit(game_surface, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Stop the loop

    # Draw maze
    [cell.draw(game_surface) for cell in maze]

    clock.tick(FPS)
    pygame.display.flip()

pygame.quit()  # Quit pygame properly

    