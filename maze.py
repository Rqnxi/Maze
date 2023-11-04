from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, p_image, p_x, p_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(p_image), (50, 50))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_RIGHT] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 445:
            self.rect.y += self.speed
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        GameSprite.reset(self)

class Enemy(GameSprite):
    moveside = 'Right'
    def update(self):
        if self.rect.x < 500:
            self.moveside = 'Right'
        if self.rect.x > 635:
            self.moveside = 'Left'
        
        if self.moveside == 'Right':
            self.rect.x += 2
        else:
            self.rect.x -= 2

class Wall(sprite.Sprite):
    def __init__(self, color1, color2, color3, x, y, height, width):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.height = height
        self.width = width
        self.image = Surface((self.width, self.height))
        self.image.fill((color1, color2, color3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def drawwall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

window = display.set_mode((700, 500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('backk.png'), (700, 500))

x1 = 50
x2 = 600
x3 = 600

y1 = 450
y2 = 300
y3 = 400

speed = 3

player = Player('hero.png', x1, y1, speed)
sprite2 = Enemy('cyborg.png', x2, y2, speed)
sprite3 = GameSprite('woman.png', x3, y3, speed)

w1 = Wall(255, 24, 58, 0, 0, 500, 10)
w2 = Wall(255, 24, 58, 690, 0, 500, 10)
w3 = Wall(255, 24, 58, 500, 200, 10, 300)
w4 = Wall(255, 24, 58, 0, 200, 10, 300)
w5 = Wall(255, 24, 58, 0, 0, 10, 700)

w6 = Wall(255, 24, 58, 150, 300, 200, 10)

w7 = Wall(255, 24, 58, 300, 200, 230, 10)
w8 = Wall(255, 24, 58, 500, 270, 500, 10)

#font
font.init()
font = font.Font(None, 70)
win = font.render('YOU WIN', True, (255, 215, 0))
lose = font.render('U LOSEr', True, (255, 215, 0))
#music
mixer.init()
mixer.music.load('jng.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')

#game base
FPS = 60
clock = time.Clock()

game = True
finish = False

#game cycle
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    
    if sprite.collide_rect(player ,sprite3):
        window.blit(win, (200,200))
        finish = True
    
    if sprite.collide_rect(player, sprite2):
        window.blit(lose, (200,200))
        finish = True        
    
    if finish != True:
        window.blit(background, (0, 0))
        w1.drawwall()
        w2.drawwall()
        w3.drawwall()
        w4.drawwall()
        w5.drawwall()
        w6.drawwall()
        w7.drawwall()
        w8.drawwall()
        player.reset()
        sprite2.reset()
        sprite3.reset()
        player.update()
        sprite2.update()

    keys_pressed = key.get_pressed()
    
    display.update()
