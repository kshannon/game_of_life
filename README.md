game_of_life
============

Building a simple Conway's Game of Life using pygame. Details about each version below.

# ------------ Version 1 ------------ #
The game is complete with a preset game area that niether wraps around or continues.
Basic Conway Logic ironed out:
  1. Any live cell with fewer than two live neighbours dies, as if caused by under-population.
  2. Any live cell with two or three live neighbours lives on to the next generation.
  3. Any live cell with more than three live neighbours dies, as if by overcrowding.
  4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
The code is still pretty rough and needs to be written better.

# ------------ Version 2 ------------ #
I am working on this version which will include cleaner code and some graphical updates.
