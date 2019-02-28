#!/usr/bin/env python3
import sys

class Picture:
	def __init__(self, orientation, nbtags, tags):
		self._orientation_ = orientation
		self._nbtags_ = nbtags
		self._tags_ = tags
	
	def get_orientation():
		return (_orientation_)

	def get_nbtags():
		return (_nbtags_)

	def get_tags():
		return (_tags_)


def get_input():
	array = []
	with open(sys.argv[1], 'r') as file:
		i = 0
		lines = file.readlines()
		for line in lines:
			i += 1
			if (i == 1)
				continue
			array = line.split(' ')
			array.append(Picture(array[0], array[1], array[2:]))

def main():
	array = get_input()
	for line in array:
		line.get

main()