import pygame as pg


pg.init()

SCREEN_WIDTH = 1080
SCREEN_HEIGHT = 880

x = 0
y = 0
width = 40
height = 60
vel = 5

win = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

pg.display.set_caption("First Game")

run = True
while run:
    pg.time.delay(100)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
    
    keys = pg.key.get_pressed()

    if keys[pg.K_LEFT] and x > vel: ## sets boundary
        x -= vel

    if keys[pg.K_RIGHT] and x < SCREEN_WIDTH - width: ##boundary minus charatcer width
        x += vel

    if keys[pg.K_UP] and y > vel:
        y -= vel
    
    if keys[pg.K_DOWN] and y < SCREEN_HEIGHT - height:
        y+= vel


    win.fill ((0,0,0))

    pg.draw.rect(win,(255,0,0), (x,y, width, height))
    pg.display.update()
    
pg.quit()

