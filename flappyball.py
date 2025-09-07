import pgzrun

WIDTH = 500
HEIGHT = 500

GRAVITY = 2000

class ball():
    def __init__(self,x,y,radius,color):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.vx = 200
        self.vy = 0
    def draw(self):
        screen.draw.filled_circle((self.x,self.y),self.radius,self.color)
bal = ball(250,250,20,"purple")
bal1 = ball(375,450,30,"pink") 
bal2 = ball(100,137,10,"blue")  
def draw():
    screen.clear()
    bal.draw()
    bal1.draw()
#    bal2.draw()

def update(dt):
    uy = bal.vy
    iy = bal1.vy
    bal.vy = bal.vy + GRAVITY * dt
    bal1.vy = bal1.vy + GRAVITY * dt
    bal.y = bal.y + (uy + bal.vy)/2*dt
    bal1.y = bal1.y + (iy + bal1.vy)/2*dt
    if bal.y > HEIGHT:
        bal.y = HEIGHT - bal.radius
        bal.vy = -bal.vy *0.75
    if bal1.y > HEIGHT:
        bal1.y = HEIGHT - bal1.radius
        bal1.vy = -bal1.vy *0.75
    bal.x = bal.x + bal.vx * dt
    if bal.x > WIDTH or bal.x < 20:
        bal.vx = bal.vx * -1
    bal1.x = bal1.x + bal1.vx * dt
    if bal1.x > WIDTH or bal1.x < 30:
        bal1.vx = bal1.vx * -1
def on_key_down(key):
    if key == keys.SPACE:
        bal.vy = -200
    if key == keys.W:
        bal1.vy = -200    



























          
pgzrun.go()