# coding: utf-8

from graph import *
import math
import random


def MakeCircle(size, vector, R):
    penSize(size)
    penColor(random.randrange(255),random.randrange(255),random.randrange(255))

    brushColor(random.randrange(255),random.randrange(255),random.randrange(255))
    return circle(vector[0],vector[1],R)

mouseVc = (0,0)

def Update():
    global array, way, s
    i = 0

    for a in array:
        cen = a[0]
        zr = a[1]
        r = a[3]

        onMouseMove(handleMove)

        if coords(cen)[0] < r/15 or coords(cen)[0] > 360-r/15:
            s[i][0] = -s[i][0]
            moveObjectBy(cen, s[i][0], s[i][1])
        elif coords(cen)[1] < r/15 or coords(cen)[1] > 450-r/15:
            s[i][1] = -s[i][1]
            moveObjectBy(cen, s[i][0], s[i][1])
        else:
            moveObjectBy(cen, s[i][0], s[i][1])

        i+=1

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

global array
array = []
n = random.randrange(5,15)
for i in range(n):
    rad = random.randrange(20,100)
    x = random.randrange(100,400)
    y = random.randrange(100,400)
    rVector = (x,y)
    c = MakeCircle(rad/20, rVector, rad)
    zrachok = MakeCircle(rad/15, rVector, rad / 4)
    array.append((c,zrachok,rVector,rad))

way = [random.randrange(1, 4)]*n
s = [0] * n
for j in range(n):
    s[j] = [random.randrange(-5, 5), random.randrange(-5, 5)]
onTimer(Update,70)
run()





