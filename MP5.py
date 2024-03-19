from cs1graphics import *
import math
import random
from tree import Tree

root = Canvas(1000,500,'skyblue','myWorld')

grass = Rectangle(1000,200)
grass.setFillColor((0,150,0))
grass.moveTo(500,400)
grass.setBorderWidth(0)

trees = []
trees.append(Tree())

#adds elements to frame
root.add(grass)
root.add(trees[0].getTreeLayer())