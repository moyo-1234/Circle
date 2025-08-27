import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
run = True
class Circle():
    def __init__(self,x,y,color,radius,width):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.radius = radius
    def draw(self):
        pygame.draw.circle(screen,self.color,(self.x,self.y),self.radius,self.width)


circ = Circle(250,250,"blue",80,10)

circ.draw()
pygame.display.update()
        










while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False








pygame.quit()