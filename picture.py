# coding: utf-8

from graph import *
import time
'''
class vec(object):
    def __init__(self,x,y):
        vec.x = x;
        vec.y = y;

class dot (object):

    def __init__(self, ):
'''
def MakeCircle(size, color1, color2, vector, R):
    penSize(size)
    penColor(color1)
    brushColor(color2)
    return circle(vector[0],vector[1],R)

rVector = (250,250)
rad = 150
c = MakeCircle(10,(0,0,0),(200,0,0), rVector, rad)

def keyPressed(event):
  if event.keycode == VK_SPACE:
    return("space")
  elif event.keycode == VK_ESCAPE:
    return ("esc")

run()




