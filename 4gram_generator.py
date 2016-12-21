#!/usr/bin/python

"""
A sample text generator trained on English 4-grams extracted from a sample
  document containing proceedings of Parliament.
"""

import sys
import string
from collections import defaultdict
from random import choice

EOS = ['.', '?', '!']

def file2four_grams(filename):
	"""
	Generates 4-grams from input file.
	"""
	return four_grams(open(filename).read().split())

def four_grams(words):
	"""
	Returns a dictionary of 4-grams, where the tuple of the first three
          words acts as the key, the fourth word as the value.

	INPUT: "The cat sat on the mat."

	OUTPUT:
	d[("The", "cat", "sat")] = "on"
	d[("cat", "sat", "on")] = "the"
	d[("sat", "on", "the")] = "mat"
	d[("on", "the", "mat")] = "."

	"""
	d = defaultdict(list)
	for i, word in enumerate(words):
		try:
			first, second, third, fourth = words[i], words[i+1], words[i+2], words[i+3]
		except IndexError:
			break
		d[(first,second,third)].append(fourth)
	return d

def generate_sentence(four_grams):
	"""
	Generates a random sentence composed of allowable 4-gram occurrences
	  found in the training text.
	"""
	# Generate a list of allowable initial words
	#   Initial words are capitalized and not punctuation.
	init_words = [word for word in four_grams.keys() if word[0][0].isupper() and not word[0] in EOS and not word[1] in EOS and not word[2] in EOS]

	# Select a random initial trigram
	w1, w2, w3 = choice(init_words)
	sentence = []
	sentence.append(w1)
	sentence.append(w2)
	sentence.append(w3)

	# Search 4-grams for additional allowable words until an EOS
	#   marker is found.
	while True:
		try:
			w4 = choice(four_grams[(w1,w2,w3)])
		except KeyError:
			break
		except IndexError:
			break
		sentence.append(w4)
		if w4 in EOS:
			break
		w1 = w2
		w2 = w3
		w3 = w4
	sentence = ' '.join(sentence)
	sentence = sentence.replace(' ,', ',')
	sentence = sentence.replace(' .', '.')
	return sentence
	
if __name__=='__main__':
	eng_four_grams = file2four_grams('LangId.train.English')
	print generate_sentence(eng_four_grams)
