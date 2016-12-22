#!/usr/bin/python

"""
A sample text generator trained on English trigrams extracted from a sample
  document containing proceedings of Parliament.
"""

import sys
import string
from collections import defaultdict
from random import choice

EOS = ['.', '?', '!']

def file2trigrams(filename):
	"""
	Generates trigrams from input file.
	"""
	return trigrams(open(filename).read().split())

def trigrams(words):
	"""
	Returns a dictionary of trigrams, where the tuple of the first two
	  words acts as the key, the third word as the value.

	INPUT: "The cat sat on the mat."

	OUTPUT:
		d[("The", "cat")] = "sat"
		d[("cat", "sat")] = "on"
		d[("sat", "on")] = "the"
		d[("on", "the")] = "mat"
		d[("the", "mat")] = "."
	"""
	d = defaultdict(list)
	for i, word in enumerate(words):
		try:
			first, second, third = words[i], words[i+1], words[i+2]
		except IndexError:
			break
		d[(first,second)].append(third)
	return d

def generate_sentence(trigrams):
	"""
	Generates a random sentence composed of allowable trigram occurrences
	  found in the training text.
	"""
	# Generate a list of allowable initial words
	#   Initial words are capitalized and not punctuation.
	init_words = [word for word in trigrams.keys() if word[0][0].isupper() and not word[0] in string.punctuation and not word[1] in string.punctuation]

	# Select a random initial bigram.
	w1, w2 = choice(init_words)
	sentence = []
	sentence.append(w1)
	sentence.append(w2)

	# Search trigams for additional allowable words until an EOS
	#   marker is found.
	while True:
		try:
			w3 = choice(trigrams[(w1,w2)])
		except KeyError:
			break
		sentence.append(w3)
		if w3 in EOS:
			break
		w1 = w2
		w2 = w3
	sentence = ' '.join(sentence)
	sentence = sentence.replace(' ,', ',')
	sentence = sentence.replace(' .', '.')
	return sentence

if __name__=='__main__':
	eng_trigrams = file2trigrams('LangId.train.English')
	print generate_sentence(eng_trigrams)
