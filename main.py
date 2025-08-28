from pygame import *


width = 600
height = 500

window = display.set_mode((width, height))
display.set_caption('pingpong: a casual game')

background_color = (125, 154, 251)
window.fill(background_color)

game = True 

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False 
    
    window.fill(background_color)
    display.update()


