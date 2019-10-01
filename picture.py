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
        r = a[3]
        s = a[4]
        #print(a[3])
        '''
        changePenColor(cen,randColor())
        changeFillColor(cen,randColor())
        changePenColor(zr,randColor())
        changeFillColor(zr,randColor())
        '''
        '''moveObjectBy(cen,s[0],s[1])
        moveObjectBy(zr,s[0],s[1])
        '''
        onMouseMove(handleMove)
        '''
        if(coords(cen)[0]+s[0]<0):
            s[0] = -s[0]
        if(coords(cen)[1]+s[1]<0):
            s[1] = -s[1]
        if (coords(cen)[0] + s[0] > 500):
            s[0] = -s[0]
        if (coords(cen)[1] + s[1] < 500):
            a[4] = -a[4]
            '''
        moveObjectBy(cen,s[0],s[1])

        rV = (coords(cen)[0], coords(cen)[1])
        print(rV)
        rr = (r, r)

        rVec = (rV[0]+rr[0], rV[1]+rr[1])

        mousex=mouseVc[0]-rVec[0]
        mousey=mouseVc[1]-rVec[1]
        d = random.randrange(5,10)
        x = rVec[0] + ((mousex * r) /(math.sqrt(mousex * mousex+mousey * mousey+r*r))/1.5) + (random.random()-0.5)*d*0
        y = rVec[1] + ((mousey * r) /(math.sqrt(mousey * mousey+mousex * mousex+r*r))/1.5) + (random.random()-0.5)*d*0
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
    x = random.randrange(-5,5)
    y = random.randrange(-5,5)
    sVector = (x,y)
    c = MakeCircle(rad/20, randColor(), randColor(), rVector, rad)
    zrachok = MakeCircle(rad/15, randColor(), randColor(), rVector, rad / 4)
    array.append((c,zrachok,rVector,rad,sVector))
    #g =circle(0,0, 20)



onTimer(Update,70)
run()





