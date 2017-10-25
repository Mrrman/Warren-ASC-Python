#!/usr/bin/python

class Animal(object):
	
	def tag (self):
		return "tag"

	def eat(food):
		print"The animal ate %s" %(food)

	def shit(self):
		print"This animal can shit"

	def walk(self):
		print"This animal can walk"

class Dog(Animal):

	def __init__(self, name):
		self.name = name

	def bark(self):
		print"%s has barked"% (self.name)

	def tag(self)
		return Animal.tag.fget


class Cat(Animal):

	def __init__(self, name):
		self.name = name


spot = Dog("spot")

spot.bark()

carl = Cat("carl")

carl.walk()
