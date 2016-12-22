#!/usr/bin/python

"""
A sample text generator trained on English bigrams extracted from a sample
  document containing proceedings of Parliament.
"""

import sys
import string
from collections import defaultdict
from random import choice

EOS = ['.', '?', '!']

def file2bigrams(filename):
	"""
	Generates bigrams from input file.
	"""
	return bigrams(open(filename).read().split())

def bigrams(words):
	"""
	Returns a dictionary of bigrams, where the first
	  word acts as the key, the second word as the value.

	INPUT: "The cat sat on the mat."

	OUTPUT:
		d["The"] = "cat"
		d["cat"] = "sat"
		d["sat"] = "on"
		d["on"] = "the"
		d["the"] = "mat"
		d["mat"] = "."
	"""
	d = defaultdict(list)
	for i, word in enumerate(words):
		try:
			first, second = words[i], words[i+1]
		except IndexError:
			break
		d[first].append(second)
	return d

def generate_sentence(bigrams):
	"""
	Generates a random sentence composed of allowable bigram occurrences
	  found in the training text.
	"""
	# Generate a list of allowable initial words
	#   Initial words are capitalized and not punctuation.
	init_words = [word for word in bigrams.keys() if word[0].isupper() and not word in string.punctuation]

	# Select a random initial bigram.
	w1 = choice(init_words)
	sentence = []
	sentence.append(w1)

	# Search bigams for additional allowable words until an EOS
	#   marker is found.
	while True:
		try:
			w2 = choice(bigrams[w1])
		except KeyError:
			break
		sentence.append(w2)
		if w2 in EOS:
			break
		w1 = w2
	sentence = ' '.join(sentence)
	sentence = sentence.replace(' ,', ',')
	sentence = sentence.replace(' .', '.')
	return sentence

if __name__=='__main__':
	eng_bigrams = file2bigrams('LangId.train.English')
	print generate_sentence(eng_bigrams)
