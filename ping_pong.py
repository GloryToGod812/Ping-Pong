from pygame import*
font.init()

clock = time.Clock()
FPS = 120

window = display.set_mode((1200, 900))
win_width = 1200
win_height = 800
display.set_caption('Ping Pong')

background = transform.scale(image.load('Tennis_Court.jpg'), (1200, 900))


class GameSprite(sprite. Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, size, size1):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size, size1))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed





player1 = Player('raketka.png', 1030, 350, 5, 70, 250)

player2 = Player('raketka.png', 100, 350, 5, 70, 250)

ball = GameSprite('ball.png', 580, 430, 10, 45, 45 )





finish = False

game = True


speed_x = 3

speed_y = 3

font1 = font.Font(None, 35)
lose1 = font1.render('Player 1 lose!', True, (180, 0, 0))
lose2 = font1.render('Player 2 lose!', True, (180, 0, 0))


while game:
   
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0)) 
        player1.reset()
        player1.update_r()
        player2.reset()
        player2.update_1()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y
    if ball.rect.y > 855 or ball.rect.y < 0:
        speed_y *= -1
    if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
        speed_x *= -1
    if ball.rect.x < 0:
        finish = True
        window.blit(lose1, (200, 200))
    if ball.rect.x > 1155:
        finish = True
        window.blit(lose2, (200, 200))








    clock.tick(FPS)
    display.update()
