
import pew

pew.init()
level1 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level2 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level3 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level4 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level5 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 2, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 2, 1, 1, 1, 2, 0, 2],
))

level6 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 1, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level7 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level8 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level9 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

level10 = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

def clear():
    level.pixel(x, y, 0)

x = 4
y = 1

level = level1

while True:

    # Level 1
    if level == level1:
        if x==6 and y==8:
            level = level2
            y = 0
    # Level 2
    elif level == level2: 
        if x==6 and y==4:
            clear()
            x = 2
            y = 1
        if x==6 and y==8:
            level = level3
            y = 0
        if x == 6 and y == -1:
            level = level1
            y = 7 
    # Level 3
    elif level == level3:
        if x==6 and y==8:
            level = level4
            y = 0
        if x==6 and y==4:
            clear()
            x = 1
            y = 6
        if x==6 and y==-1:
            level = level2
            y = 7  
    # Level 4
    elif level == level4:
        if x==6 and y==8:
            level = level5
            y = 0
        if x==1 and y==4:
            clear()
            x = 5
            y = 5
        if x==1 and y==6:
            clear()
            x = 6
            y = 6
        if x==6 and y==-1:
            level = level3
            y = 7
    # Level 5
    elif level == level5:
        if x==6 and y==8:
            level = level6
            y = 0
        if x==1 and y==4:
            clear()
            y = 6
        if x==6 and y==-1:
            level = level4
            y = 7
    # Level 6
    elif level == level6:
        if x==6 and y==8:
            level = level7
            y = 0
        if x==1 and y==4:
            clear()
            x = 5
            y = 6
        if x==6 and y==-1:
            level = level5
            y = 7
    # Level 7
    elif level == level7:
        if x==3 and y==4:
            clear()
            x = 1
            y = 1
        if x==6 and y==4:
            clear()
            x = 4
            y = 1
        if x==6 and y==8:
            level = level8
            y = 0
        if x==6 and y==-1:
            level = level6
            y = 7
    # Level 8
    elif level == level8:
        if x==1 and y==1:
            clear()
            x = 1
            y = 3
        if x==4 and y==3:
            clear()
            x = 6
            y = 3
        if x==6 and y==8:
            level = level9
            y = 0
        if x==6 and y==-1:
            level = level7
            y = 7
    # Level 9
    elif level == level9:
        if x==3 and y==1:
            clear()
            x = 1
        if x==6 and y==8:
            level = level10
            y = 0
        if x==6 and y==-1:
            level = level8
            y = 7
    # Level 10
    elif level == level10:
        if x==6 and y==4:
            clear()
            y = 6

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