#!/usr/bin/env python3
import sys
import operator

class Picture:
	def __init__(self, orientation, nbtags, tags, i):
		self._orientation_ = orientation
		self._nbtags_ = nbtags
		self._tags_ = tags
		self._id_ = i
	
	def get_orientation(self):
		return (self._orientation_)

	def get_nbtags(self):
		return (self._nbtags_)

	def get_tags(self):
		return (self._tags_)

	def get_id(self):
		return (self._id_)

def get_input():
	array = []
	dict_tag = {}
	with open(sys.argv[1], 'r') as file:
		lines = file.readlines()
		for i, line in enumerate(lines[1:]):
			tmp = line.split(' ')
			tmp[len(tmp)-1] = tmp[len(tmp)-1].replace("\n", "")
			obj = Picture(tmp[0], tmp[1], tmp[2:], i)
			array.append(obj)
			for tag in obj.get_tags():
				if (tag in dict_tag):
					dict_tag[tag]["nb"] += 1
					#dict_tag[tag]["obj"].append(obj)
				else:
					dict_tag[tag] = {"nb": 1, "obj": []}
	sorted_dict = sorted(dict_tag.items(), key=lambda kv: kv[1]["nb"], reverse=True)
	for line in array:
		for i, tmp in enumerate(sorted_dict):
			if tmp[0] in line.get_tags():
				sorted_dict[i][1]["obj"].append(line)
				break
	return (sorted_dict)

def createSlideshow(dict_tag):
	slides = []
	slide_v = []
	for i in dict_tag:
		for j in i[1]["obj"]:
			if j.get_orientation() == 'H':
				slides.append([j.get_id()])
			else:
				slide_v.append(j.get_id())
				if len(slide_v) == 2:
					slides.append([slide_v[0], slide_v[1]])
					slide_v.clear()
		# if len(slide_v) != 0:
		# 	slides.append([slide_v[0]])
	return (slides)

def printMyArray(array):
	print(len(array))
	for obj in array:
		if len(obj) == 1:
			print("{}".format(obj[0]))
		else:
			print("{} {}".format(obj[0], obj[1]))

def main():
	dict_tag = get_input()
	michel = createSlideshow(dict_tag)
	printMyArray(michel)
	# for k, v in dict_tag:
	# 	print(k, v["nb"], len(v["obj"]))
	# 	for i in v["obj"]:
	# 		print(i.get_id())
	# 	print("")
main()