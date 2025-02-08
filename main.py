import pygame
from random import choice

# All Images
image = pygame.image.load("Scared_Dracula/Images/garlic.jpg")
Garlic =  pygame.transform.scale(image, (50, 30))
background_img = pygame.image.load("Scared_Dracula/Images/background.jpg")

# Creating a screen
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Scared_Dracula")
# COLORS
BLACK = (0,0,0)
WHITE = (255,255,255)
# Maze parameters
cell_size = 40
grid_width = width // cell_size
grid_height = height // cell_size

# # Create maze grid
# maze = [[1 for _ in range(grid_width)] for _ in range(grid_height)]
# # Function to draw maze
# def draw_maze():
#     for y in range(grid_height):
#         for x in range(grid_width):
#             if maze[y][x] == 1:
#                 pygame.draw.rect(screen, BLACK, (x*cell_size, y*cell_size, cell_size, cell_size))
#             else:
#                 pygame.draw.rect(screen, WHITE, (x*cell_size, y*cell_size, cell_size, cell_size))
 

def add_player(x,y):
    screen.blit(Garlic, (x, y))
x, y = 400, 400
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(background_img,(0,0))
    add_player(x,y)
    pygame.display.update()
    
pygame.quit()   

