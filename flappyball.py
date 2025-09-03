import pgzrun

WIDTH = 500
HEIGHT = 500

class ball():
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)
bal = ball(250,250,20,"purple")  
def draw():
    bal.draw()

pgzrun.go()
          
