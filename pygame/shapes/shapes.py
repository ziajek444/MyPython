##      Def section   ##

class Color:
    def __init__(self):
        # Zeroize / Zeroization
        self.__red = self.__green = self.__blue = self.__Alpha = 0
    def RGB(self,r,g,b):
        return (r,g,b)
    def RGBA(self,r,g,b,a):
        return (r,g,b,a)
    def RedA(self,visibility):
        return (255,0,0,visibility)
    def Red(self):
        return tuple([255,0,0])
    def TAPETA(self):
        return (15,15,15)

def DrawAll(kolor,ekran,r=25,g=55,b=89):
    ekran.fill((150,15,15))
    pygame.draw.rect(ekran,kolor.RGB(r,g,b), [75, 10, 50, 20], 2) # Draw a rectangle outline
    pygame.draw.rect(ekran,kolor.RGB(r,g,b), [150, 10, 50, 20]) # Draw a solid rectangle
    pygame.draw.polygon(ekran,kolor.RGB(r,g,b), [[100, 100], [0, 200], [200, 200]], 5) # This draws a triangle using the polygon command
    pygame.draw.circle(ekran,kolor.RGB(r,g,b), [60, 250], 40) # Draw a circle
    pygame.draw.ellipse(ekran,kolor.RGB(r,g,b), [225, 10, 50, 20], 2) # Draw an ellipse outline, using a rectangle as the outside boundaries
    pygame.draw.ellipse(ekran,kolor.RGB(r,g,b), [300, 10, 50, 20])# Draw an solid ellipse, using a rectangle as the outside boundaries
    #pygame.draw.arc(ekran,kolor.RBG(r,g,b))
    pygame.draw.line(ekran,kolor.RGB(r,g,b), [0, 0], [50,30], 5) # Draw on the screen a GREEN line from (0,0) to (50.75)  # 5 pixels wide.
    pygame.draw.lines(ekran,kolor.RGB(r,g,b), False, [[0, 80], [50, 90], [200, 80], [220, 30]], 5) # Draw on the screen a GREEN line from (0,0) to (50.75) 
    pygame.draw.aaline(ekran,kolor.RGB(r,g,b), [0, 50],[50, 80], True) # Draw on the screen a GREEN line from (0,0) to (50.75) 
    #pygame.draw.aalines(ekran,kolor.RBG(r,g,b))
##--------------------##

import pygame

clock = pygame.time.Clock()

color = Color()
assert color.Red() == (255,0,0)
for ass in range(0,255,5):
    assert color.RGB(ass,ass,ass) == (ass,ass,ass)
    assert color.RGBA(ass,ass,ass,ass) == (ass,ass,ass,ass)

pygame.init()

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('A bit Racey')



DrawAll(color,gameDisplay)



crashed = False
while not crashed:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        #print(event)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()
