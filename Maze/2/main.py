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
    [1, 1, 1, 1, 1, 2, 2, 2],
))

level2 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level3 = pew.Pix.from_iter((
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

level = level2

def clear():
    level.pixel(x, y, 0)
while True:
    # Level 1
    if level == level1:
        # Next level
        if x == 1 and y == 2:
            clear()
            level = level2
            x = 6
            y = 0
            clear()
    # Level 2
    if level == level2:
        pixel(self, 6, 3, 0)
        # Previous level
        if x == 6 and y == -1:
            level = level1
            x = 6
            y = 0
 
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