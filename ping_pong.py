from pygame import*


clock = time.Clock()
FPS = 120

window = display.set_mode((1200, 900))
display.set_caption('Ping Pong')

background = transform.scale(image.load('Tennis_Court.jpg'), (1200, 900))








game = True

while game:

    window.blit(background,(0, 0))

    for e in event.get():
        if e.type == QUIT:
            game = False










    clock.tick(FPS)
    display.update()
