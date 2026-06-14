import pygame
import random
import time
import math
import os


pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_CENTERED'] = '1'
info = pygame.display.Info()
width,hieght = info.current_w,info.current_h

wn = pygame.display.set_mode((width,hieght))
print(width)
print(hieght)
    

class BaseVariablesClass:
    def __init__(self, myID, mybranch, mysubgroup, myfamily, myisSolid, mysize, myposition, myimage):
        self.myID = myID
        self.mybranch = mybranch
        self.mysubgroup = mysubgroup
        self.myfamily = myfamily
        self.myisSolid = myisSolid
        self.mysize = mysize
        self.myposition = myposition
        self.myimage = pygame.transform.scale(pygame.image.load(myimage),mysize)#.convert()
        self.myrect = self.myimage.get_rect(center = self.myposition)

    # Get Methods 
    def getID(self):
        return self.myID
    def getbranch(self):
        return self.mybranch
    def getsubgroup(self):
        return self.mysubgroup 
    def getfamily(self):
        return self.myfamily
    def getisSolid(self):
        return self.myisSolid
    def getsize(self):
        return self.mysize
    def getposition(self):
        return self.myposition
    def getimage(self):
        return self.myimage
    def getrect(self):
        return self.myrect
    
    # Print Methods
    def printID(self):
        print(self.getID())
    def printbranch(self):
        print(self.getbranch())
    def printsubgroup(self):
        print(self.getsubgroup())
    def printfamily(self):
        print(self.getfamily())
    def printisSolid(self):
        print(self.getisSolid())
    def printsize(self):
        print(self.getsize())
    def printposition(self):
        print(self.getposition())
    def printimage(self):
        print(self.getimage())
    def printrect(self):
        print(self.getrect())
    
    # Set Methods    
    def setID(self,newID):
        self.myID = newID
    def setbranch(self,newbranch):
        self.mybranch = newbranch
    def setsubgroup(self,newsubgroup):
        self.mysubgroup = newsubgroup
    def setfamily(self,newfamily):
        self.myfamily = newfamily
    def setisSolid(self,newisSolid):
        self.myisSolid = newisSolid
    def setsize(self,newsize):
        self.mysize = newsize
    def setposition(self,newposition):
        self.myposition = newposition
        self.myrect = self.getimage().get_rect(center = self.getposition())
    def setimage(self,newimage):
        self.myimage = newimage
        self.setposition(self.getposition())

class background(BaseVariablesClass):
    def __init__(self, myID, mybranch, mysubgroup, myfamily, myisSolid, mysize, myposition, myimage):
        super().__init__(myID, mybranch, mysubgroup, myfamily, myisSolid, mysize, myposition, myimage)

class machinegunner(BaseVariablesClass):
    def __init__(self, myID, mybranch, mysubgroup, myfamily, myisSolid, mysize, myposition, myimage):
        super().__init__(myID, mybranch, mysubgroup, myfamily, myisSolid, mysize, myposition, myimage)
        self.myfacingleft = True
        self.setimage(pygame.transform.flip(super().getimage(),not(self.myfacingleft),False))

    def getimage(self):
        return pygame.transform.flip(self.myimage,not self.myfacingleft,False)
    
    def getfacingleft(self):
        return self.myfacingleft
    
    def turn(self,b):
        self.myfacingleft = b

    def printfacingleft(self):
        print(self.getfacingleft())

    def calculateratiox_y(self,x,y):
        pass

    def move(self,x,y):
        if x>0 and self.getfacingleft():
            self.turn(False)
        elif x<0 and not self.getfacingleft():
            self.turn(True)
        self.setposition([self.getposition()[0]+x,self.getposition()[1]+y])

class mediumtank(BaseVariablesClass):
    def __init__(self, myID, mybranch, mysubgroup, myfamily, myisSolid, mysize, myposition, myimage):
        super().__init__(myID, mybranch, mysubgroup, myfamily, myisSolid, mysize, myposition, myimage)
        self.myangle = 0
        self.myturnspeed = 3
        # self.mygoal = {"where":myposition,"what":self.movethere([0,0],0)}

    def getimage(self):
        # self.myrect = pygame.transform.flip(super().getimage(),not self.myfacingleft,False).get_rect(center = self.getposition())
        return pygame.transform.rotate(super().getimage(),self.getangle())
    
    def getangle(self):
        return self.myangle
    
    def turn(self,angle):
        if self.myangle - angle < angle - self.myangle:
            self.myangle += self.myturnspeed
        if self.myangle - angle > angle - self.myangle:
            self.myangle -= self.myturnspeed
        self.myangle %= 360
        self.myrect = pygame.transform.rotate(super().getimage(),self.getangle()).get_rect(center = self.getposition())

    def printangle(self):
        print(self.getangle())

    def calculateratiox_y(self,x,y):
        x,y = x-self.getposition()[0],y-self.getposition()[1]
        if x == 0:
            print( [0,(1 if y>0 else -1)] )
        elif y == 0:
            print( [(1 if x>0 else -1),0] )
        else:
            px = (1 if x>0 else -1)/math.sqrt(y/x*y/x+1)
            py = (1 if x>0 else -1)*(y/x)/math.sqrt(y/x*y/x+1)
            print( [px,py] )
    
    def calculateangle(self,x,y):
        x,y = x-self.getposition()[0],y-self.getposition()[1]
        angle = math.degrees(math.atan(y/x))
        print( angle )

    def move(self,speed):
        self.setposition([self.getposition()[0]+speed*math.cos(math.radians(self.getangle()-90)),self.getposition()[1]-speed*math.sin(math.radians(self.getangle()-90))])

    # def shootheavy(self):

    # def shootlight(self):

    # def inrangeheavy(self):

    # def inrangelight(self):




clock = pygame.time.Clock()
FPS = 30

# HomeScreen = True
# while HomeScreen:
#     clock.tick(FPS)


b1 = background("Machinegunner",None,None,None,True,[75,75],[300,300],"total con pistol soldier2.png")
p1 = machinegunner("Machinegunner",None,None,None,True,[width/60,width/60],[300,300],"total con pistol soldier2.png")
t1 = mediumtank("Machinegunner",None,None,None,True,[width/30,width/22],[600,600],"total con tank.png")

running = True


startTime = time.time()

while running:
    x,y=0,0
    if pygame.key.get_pressed()[pygame.K_w]: y=-5
    if pygame.key.get_pressed()[pygame.K_s]: y=5
    if pygame.key.get_pressed()[pygame.K_a]: x=-5
    if pygame.key.get_pressed()[pygame.K_d]: x=5
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
    if time.time()-startTime > 4:
        startTime = time.time()


    wn.fill((255,255,255))
    # wn.blit()
    wn.blit(p1.getimage(),p1.getrect())
    p1.move(x,y)
    wn.blit(t1.getimage(),t1.getrect())
    t1.turn(45)
    t1.move(3)
    t1.calculateangle(599,599)
    pygame.display.flip()
    clock.tick(FPS)