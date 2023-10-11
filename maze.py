#создай игру "Лабиринт"!

from pygame import *
font.init()
font = font.Font(None,47)
window = display.set_mode((700,500))
display.set_caption('Лабиринт')
player_step = 10
background = transform.scale(image.load('background.jpg'),(700,500))
class Players(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_step):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(50,50))
        self.rect = self.image.get_rect()
        self.rect_x = player_x
        self.rect_y = player_y
        self.step = player_step
    def reset(self):
        window.blit(self.image,(self.rect_x,self.rect_y))
class Player(Players):
    def control(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_d] and self.rect_x < 650:
            self.rect_x += self.step
        if keys_pressed[K_a] and self.rect_x > 0:
            self.rect_x -= self.step
        
        if keys_pressed[K_w] and self.rect_y > 0:
            self.rect_y -= self.step
        if keys_pressed[K_s] and self.rect_y < 450:
            self.rect_y += self.step
class Enemy(Players):
    direction = 'left'
    def control(self):
        if self.rect_x <= 500:
            self.direction = 'right'
        if self.rect_x >= 600:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect_x -= self.step
        if self.direction == 'right':
            self.rect_x += self.step
        


Mikula = Player('hero.png',10,450,10)
Cibercotleta = Enemy('cyborg.png',410,450,5)
game = True
clock = time.Clock()
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
while game:
    window.blit(background,(0,0))
    for e in event.get():
        if e.type == QUIT:
            game = False
    Mikula.reset()
    Cibercotleta.reset()
    Mikula.control()
    Cibercotleta.control()
    display.update()
    clock.tick(60)