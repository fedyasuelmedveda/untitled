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

rVector = (250,250)
rad = 150
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
    changePenColor(c,randColor())
    changeFillColor(c,randColor())
    changePenColor(zrachok,randColor())
    changeFillColor(zrachok,randColor())
    onMouseMove(handleMove)
    mousex=mouseVc[0]-rVector[0]
    mousey=mouseVc[1]-rVector[1]
    x = rVector[0] + ((mousex * rad) /(math.sqrt(mousex * mousex+mousey * mousey+rad*rad))/1.5) + (random.random()-0.5)*d
    y = rVector[1] + ((mousey * rad) /(math.sqrt(mousey * mousey+mousex * mousex+rad*rad))/1.5) + (random.random()-0.5)*d
    #((random.random()-0.7)*rad)/c
    moveObjectTo(zrachok,x-25,y-25)
#    moveObjectTo(g,x,y)
def handleMove(event):
    global mouseVc
    mouseVc = (event.x,event.y)
#    print(event.x)

c = MakeCircle(10,(0,0,0),(255,255,255), rVector, rad)
zrachok = MakeCircle(10,(0,0,0),(0,0,0),rVector,rad/5)
#g =circle(0,0, 20)
d = 40


onTimer(Update,70)
run()





