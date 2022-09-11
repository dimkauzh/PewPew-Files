import pew
pew.init()


level = pew.Pix.from_iter((
    [1, 1, 1, 1, 1, 2, 0, 2],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 2, 0, 2],
))

x = 1
y = 3

while True:
    # Keys
    level.pixel(x, y, 0)
    keys = pew.keys()
    if keys & pew.K_UP:
        y -= 1
    elif keys & pew.K_DOWN:
        y += 1
    elif keys & pew.K_LEFT:
        x -= 1
    elif keys & pew.K_RIGHT:
        x += 1
    level.pixel(x, y, 3)
    pew.show(level)
    pew.tick(1/6)
