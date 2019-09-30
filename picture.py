# coding: utf-8

from graph import *
import time
import math
import random
'''
class vec(object):
    def __init__(self,x,y):
        vec.x = x;
        vec.y = y;

class dot (object):

    def __init__(self, ):
'''
#rVector = (250,250)
#rad = 150
#lobal mouseVc
'''
def mod(x):
    if x<0 :
        x=-x
    return x


def Length(v1,v2):
    return math.sqrt(mod(v1[1]-v2[1])*mod(v1[1]-v2[1])+mod(v1[2]-v2[2])*mod(v1[2]*v2[2]))
def MakeCircle(size, color1, color2, vector, R):
    penSize(size)
    penColor(color1)
    brushColor(color2)
    return circle(vector[0],vector[1],R)
def HandleMove(event):
    return (event.x,event.y)
'''
def MakeCircle(size, color1, color2, vector, R):
    penSize(size)
    penColor(random.randrange(255),random.randrange(255),random.randrange(255))

    brushColor(random.randrange(255),random.randrange(255),random.randrange(255))
    return circle(vector[0],vector[1],R)

mouseVc = (0,0)
def Update():
    global array
    for a in array:
        cen = a[0]
        zr = a[1]
        rV = a[2]
        r = a[3]
        print(a[3])
        '''
        changePenColor(cen,randColor())
        changeFillColor(cen,randColor())
        changePenColor(zr,randColor())
        changeFillColor(zr,randColor())
        '''
        onMouseMove(handleMove)

        mousex=mouseVc[0]-rV[0]
        mousey=mouseVc[1]-rV[1]
        d = random.randrange(5,10)
        x = rV[0] + ((mousex * r) /(math.sqrt(mousex * mousex+mousey * mousey+r*r))/1.5) + (random.random()-0.5)*d
        y = rV[1] + ((mousey * r) /(math.sqrt(mousey * mousey+mousex * mousex+r*r))/1.5) + (random.random()-0.5)*d
        moveObjectTo(zr,x-r/5,y-r/5)



def handleMove(event):
    global mouseVc
    mouseVc = (event.x,event.y)
#    print(event.x)
global array
array = []
n = random.randrange(5,15)
for i in range(n):
    rad = random.randrange(20,100)
    x = random.randrange(50,450)
    y = random.randrange(50,450)
    rVector = (x,y)
    c = MakeCircle(rad/20, randColor(), randColor(), rVector, rad)
    zrachok = MakeCircle(rad/15, randColor(), randColor(), rVector, rad / 4)
    array.append((c,zrachok,rVector,rad))
    #g =circle(0,0, 20)



onTimer(Update,70)
run()





