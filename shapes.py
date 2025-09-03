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
    def incr_size(self):
        self.radius = self.radius + 5
        self.draw()
        

class recta():
    def __init__(self,x,y,color,length,width,height):
        self.x = x
        self.y = y
        self.color = color
        self.width = width
        self.length = length
        self.height = height
    def draw(self):
        pygame.draw.rect(screen,self.color,(self.x,self.y,self.length,self.height),self.width)
    def incre_size(self):
        self.length = self.length + 5
        self.height = self.height + 5
        self.draw()

circ = Circle(250,250,"blue",80,10)
circl = Circle(350,400,"red",80,10)
cir = Circle(150,400,"green",80,10)
rect = recta(211,100,"orange",80,5,70)

pygame.display.update()
        





while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        elif i.type == pygame.MOUSEBUTTONDOWN:
            circ.draw()
            circl.draw()
            cir.draw()
            rect.draw()
            pygame.display.update()
        elif i.type == pygame.MOUSEBUTTONUP:
            circ.incr_size()







pygame.quit()