__author__ = 'kyle shannon'

import pygame
import time
from pygame import K_RETURN
from pygame import K_p

# building the display and size
SCREEN_WIDTH = 601
SCREEN_HEIGHT = 601
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Conway's Life: The Game")
# individual grid dimensions
HEIGHT = 10
WIDTH = 10
MARGIN = 2
# row & column size
MAX_COL = 50
MAX_ROW = 50
# define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 250, 250, 250)
D_GREY   = ( 35, 35, 35)
# initialize pygame
pygame.init()
pygame.display.init()
# game states
done = False
running = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# function to draw grid on screen
def draw_screen(row, col):
    screen.fill(D_GREY) # Set the screen background
    for row in range(MAX_ROW): # Draw the 2D grid
        for col in range(MAX_COL):
            color = BLACK
            if grid[row][col] == 1:
                color = WHITE
            pygame.draw.rect(screen, color, ((MARGIN + WIDTH)* col + MARGIN, (MARGIN + HEIGHT)
                                            * row + MARGIN, WIDTH, HEIGHT))

# check each cell in grid[] for number of alive neighbors
def check_neighbors(row, col):
    global neighbors
    check_up = (row >= 1)
    check_down = (row < MAX_ROW - 1 )
    check_left = (col >= 1)
    check_right = (col < MAX_COL - 1)
    if check_up and check_left and grid[row -1][col-1] == 1:    # top left
        neighbors += 1
    if check_up and grid[row-1][col] == 1:                      # top middle
        neighbors += 1
    if check_up and check_right and grid[row-1][col+1] == 1:    # top right
        neighbors += 1
    if check_left and grid[row][col-1] == 1:                    # middle left
        neighbors += 1
    if check_right and grid[row][col+1] == 1:                   # middle right
        neighbors += 1
    if check_down and check_left and grid[row+1][col-1] == 1:   # bottom left
        neighbors += 1
    if check_down and grid[row+1][col] == 1:                    # bottom middle
        neighbors += 1
    if check_down and check_right and grid[row+1][col+1] == 1:  # bottom right
        neighbors += 1
    return neighbors

# evole the game board, which cells are born, live and perish
def evolution(neighbors):
    if grid[row][col] == 0 and neighbors == 3:
        new_grid[row][col] = 1
    if grid[row][col] == 1 and (neighbors == 0 or neighbors == 1):
        new_grid[row][col] = 0
    elif grid[row][col] == 1 and (neighbors == 2 or neighbors == 3):
        new_grid[row][col] = 1
    elif grid[row][col] == 1 and neighbors > 3:
        new_grid[row][col] = 0
    return new_grid[row][col]

grid = []
for row in range(MAX_ROW):
    grid.append([])
    for col in range(MAX_COL):
        grid[row].append(0) # Append a cell

# -------- Main Program Loop ----------- #
while done == False:
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done = True # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos() # User clicks the mouse. Get the position
            col= pos[0] // (WIDTH + MARGIN) # Change the x/y screen coordinates to grid coordinates
            row = pos[1] // (HEIGHT + MARGIN)
            if grid[row][col] == 0:
                grid[row][col] = 1
                #print 'Mouse position: %s Row: %s Column: %s' % (pos, row, col)
            elif grid[row][col] == 1:
                grid[row][col] = 0
                #print 'Mouse position: %s Row: %s Column: %s' % (pos, row, col)
        elif event.type == pygame.KEYDOWN:
            if event.key == K_p:
                #if running == True:
                running = False
            elif event.key == K_RETURN:
                running = True
                continue

   # -------- Main Game Loop ----------- #
    if running == True:
        time.sleep(0.05)

        # making new grid to use as a copy sheet.
        new_grid = []
        for new_row in range(MAX_ROW):
            new_grid.append([])
            for new_col in range(MAX_COL):
                new_grid[new_row].append(0)

        # game loop to check for neighbors and update cells.
        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                neighbors = 0

                # functions to determine natural selection
                check_neighbors(row, col)
                evolution(neighbors)

        # copy new grid to old grid
        grid = list(new_grid)

    # function to drawn the grid
    draw_screen(row, col)
    # Limit to 20 frames per second
    clock.tick(20)
    # update the screen with what we've drawn.
    pygame.display.flip()
# Be IDLE friendly.
pygame.quit()



