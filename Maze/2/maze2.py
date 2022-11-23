from contextlib import nullcontext
import pew

pew.init()
level1 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
))

level2 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 0, 2, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
))

level3 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level4 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level5 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

x = 6
y = 0
stand_x = 6
stand_y = 0

level = level3

def clear(x, y, num):
    level.pixel(x, y, num)
while True:
    # Level 1
    if level == level1:
        # Next level
        if x == 1 and y == 2:
            clear(1, 2, 0)
            level = level2
            x = 6
            y = 0
    # Level 2
    if level == level2:
        if x == 1 and y == 2:
            level.pixel(6, 3, 0)
            x = stand_x
            y = stand_y
        # Next Level
        if x == 1 and y == 4:
            level = level3
            clear(1, 4, 0)
        # Previous level
        if x == 6 and y == -1:
            level = level1
            x = 6
            y = 0
            clear(6, -1, 0)
    # Level 3       
    if level == level3:
        # Teleport
        if x == 4 and y == 6:
            x = 6
            y = 3
            clear(4, 6, 0)
        # Next level
        if x == 6 and y == 8:
            level = level4
            x = 6
            y = 0
            clear(1, 4, 0)
        # Previous level
        if x == 6 and y == -1:
            level = level2
            x = 6
            y = 0
            clear(6, -1, 0)
    if level == level4:
        # Next level
        if x == 1 and y == 4:
            level = level5
            clear(1, 4, 0)
        

    level.pixel(x, y, 0)
    keys = pew.keys()
    dx = 0
    dy = 0
    if keys & pew.K_UP:
        dy = -1
    elif keys & pew.K_DOWN:
        dy = 1
    elif keys & pew.K_LEFT:
        dx = -1
    elif keys & pew.K_RIGHT:
        dx = 1
    target = level.pixel(x+dx, y+dy)    
    if target == 0:
        x += dx
        y += dy
    level.pixel(x, y, 3)
    pew.show(level)
    pew.tick(1/2)