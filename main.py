from pygame import *


width = 600
height = 500

window = display.set_mode((width, height))
display.set_caption('pingpong: a casual game')

background_color = (125, 154, 251)
window.fill(background_color)


class GameSprite(sprite.Sprite):
  # class constructor
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # We call the class constructor (Sprite):
        sprite.Sprite.__init__(self)

        # each sprite must store an image property
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed

        # each sprite must store the rect property it is inscribed in
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
  # method that draws the character in the window
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# main player class
class Player(GameSprite):
    # method for controlling the sprite with keyboard arrows
    def move_p1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < height - 80:
            self.rect.y += self.speed

    def move_p2(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < height - 80:
            self.rect.y += self.speed


p1 = Player('racket.png',30, 200, 30, 100, 5)
p2 = Player('racket.png',520, 200, 30, 100, 5)
ball = GameSprite('tenis_ball.png', 250, 300, 50, 50, 5)

clock = time.Clock()

game = True 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    
    window.fill(background_color)

    p1.reset()
    p2.reset()
    ball.reset()

    display.update()
    clock.tick(60)


