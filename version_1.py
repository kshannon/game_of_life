__author__ = 'kyle shannon'


import pygame
import time
from pygame import K_RETURN
from pygame import K_p

# Define some colors
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)

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

pygame.init()
pygame.display.init()


# Create a 2 dimensional array. A two dimesional
# array is simply a list of lists.
grid = []
for row in range(MAX_ROW):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for col in range(MAX_COL):
        grid[row].append(0) # Append a cell

# Set row 1, cell 5 to one. (Remember rows and
# column numbers start at zero.)
#grid[49][49] = 1

# Initialize pygame
#pygame.init()

# Set the height and width of the screen
size = [601, 601]
screen = pygame.display.set_mode(size)

# Set title of screen
pygame.display.set_caption("Conway's Life: The Game")

#Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

running = False


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
            if event.key == K_RETURN:
                running = True
                continue

   # -------- Main Game Logic Loop ----------- #
    if running == True:
    #while running == True:       with this while loop instead if an if statement it would not draw to screen?
        # conway's game logic
        # neighbors = 0
        time.sleep(0.05)
        new_grid = []
        for new_row in range(MAX_ROW):
            new_grid.append([])
            for new_col in range(MAX_COL):
                new_grid[new_row].append(0)
                #print new_grid[0][0]

        for row in range(MAX_ROW):
            for col in range(MAX_COL):
                neighbors = 0
                #print 'Row: %s and Col: %s' % (row, col)
                #print grid

                # if grid[row][col] == 1 or grid[row][col] == 0:
                #     if grid[row][col] == 1:
                #         print 'Cell alive at: row: %s and col: %s' % (row, col)

               # !------------------- top row -----------------! #
               # if grid[row] > MAX_ROW + 1 and grid[col] > MAX_COL + 1: # double check for corner neighbor
                if row >= 1 and col >= 1: # double check for corner neighbor
                    if grid[row -1][col-1] == 1:
                        neighbors += 1
                        print("A. neighbor at {},{}".format(row-1, col-1))

                #if grid[row] > MAX_ROW + 1: # single check, because neighbor is directly above.
                if row >= 1: # double check for corner neighbor
                    if grid[row-1][col] == 1:
                        neighbors += 1
                        print("B. neighbor at {},{}".format(row-1, col))

                #if grid[row] < MAX_ROW + 1 and grid[col] > MAX_COL + 1: # double check
                if row >= 1 and col < MAX_COL - 1: # double check for corner neighbor
                    if grid[row-1][col+1] == 1:
                        neighbors += 1
                        print("C. neighbor at {},{}".format(row-1, col+1))

                # !------------------- middle row -----------------! #
                #if grid[col] > MAX_COL + 1: # single check for left neighbor
                if col >= 1:
                    if grid[row][col-1] == 1:
                        neighbors += 1
                        print("D. neighbor at {},{}".format(row, col-1))

                #if grid[col] < MAX_COL - 1: # single check for right neighbor
                if col < MAX_COL - 1:
                    if grid[row][col+1] == 1:
                        neighbors += 1
                        print("E. neighbor at {},{}".format(row, col+1))

                # !------------------- bottom row -----------------! #
                #if grid[row] < MAX_ROW - 1 and grid[col] < MAX_COL + 1: # double check for corner neighbor
                if row < MAX_ROW - 1 and col >= 1:
                    if grid[row+1][col-1] == 1:
                        neighbors += 1
                        print("F. neighbor at {},{}".format(row+1, col-1))

                #if grid[row] < MAX_ROW - 1: # single check, because neighbor is directly below.
                if row < MAX_ROW - 1:
                    if grid[row+1][col] == 1:
                        neighbors += 1
                        print("G. neighbor at {},{}".format(row+1, col))

                #if grid[row] > MAX_ROW + 1 and grid[col] < MAX_COL - 1: # double check
                if row < MAX_ROW - 1 and col < MAX_COL - 1:
                    if grid[row+1][col+1] == 1:
                        neighbors += 1
                        print("H. neighbor at {},{}".format(row+1, col+1))

                if grid[row][col] == 0 and neighbors == 3:
                    print "dead cell comes alive due to procreation at {},{}".format(row, col)
                    new_grid[row][col] = 1
                    continue
                    # neighbors = 0


                # the rules of life.
                if grid[row][col] == 1 and (neighbors == 0 or neighbors == 1):
                    print "too few neighbors, cell dies at {},{}".format(row, col)
                    new_grid[row][col] = 0
                    # neighbors = 0
                elif grid[row][col] == 1 and (neighbors == 2 or neighbors == 3):
                    print "bringing cell to life at {},{}".format(row, col)
                    new_grid[row][col] = 1
                    # neighbors = 0
                elif grid[row][col] == 1 and neighbors > 3:
                    print "too many neighbors, cell dies at {},{}".format(row, col)
                    new_grid[row][col] = 0
                    # neighbors = 0
                #elif grid[row][col] == 0 and neighbors >= 3:
                    #print "dead cell comes alive due to procreation at {},{}".format(row, col)
                    #new_grid[row][col] = 1
                    #    neighbors = 0

        grid = list(new_grid)

    # pausing the game
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == K_p:
                #if running == True:
                running = False

        #for one run.
        #running = False

    screen.fill(BLACK) # Set the screen background
    for row in range(MAX_ROW): # Draw the 2D grid
        for col in range(MAX_COL):
            color = WHITE
            if grid[row][col] == 1:
                color = BLACK
            pygame.draw.rect(screen, color, ((MARGIN + WIDTH)* col + MARGIN,
                                                     (MARGIN + HEIGHT) * row + MARGIN,
                                                     WIDTH, HEIGHT))
    # Limit to 20 frames per second
    clock.tick(20)

    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()
