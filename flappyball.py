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
bal1 = ball(375,450,30,"pink") 
bal2 = ball(100,137,10,"blue")  
def draw():
    bal.draw()
    bal1.draw()
    bal2.draw()


























          
pgzrun.go()