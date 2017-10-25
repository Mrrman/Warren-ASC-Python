
#!/usr/bin/python

from RpgGameFunctions import *

class Player(object):
 def __init__(self):
  self.inv = []


class House(object):
 def __init__(self):
  self.items = []

 def display(self):
  for item in self.items:
   print 'Item: {}'.format(item)
  

class Enemy(object):
 def __init__(self):
  self.items = []
  self.med = False
  self.ammo = True
  self.pistol = False
  

def main():
 en1 = Enemy()
 en1.pistol = True
 pl = Player()

 while 1:
  try:
  
  except:break 






pl.items += en1.items
del en1[:]


