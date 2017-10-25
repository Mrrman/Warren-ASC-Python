#!/usr/bin/python


class Song(object):

	def __init__(self, lyrics):
		self.lyrics = lyrics

	def sing(self):
		for line in self.lyrics:
			print line

happyBday = Song(["Happy bday to you"
 "I dont want to get sued"
 " So I\'ll stop right there"])

bullsOnParade = Song (["They rally round your family"
 " pocket full of shells"])

happyBday.sing()

bullsOnParade.sing()
