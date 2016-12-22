#!/usr/bin/python

"""
A sample text generator trained on English unigrams extracted from a sample
  document containing proceedings of Parliament.
"""

import sys
import string
from collections import defaultdict
from random import choice

EOS = ['.', '?', '!']

def file2unigrams(filename):
	"""
	Generates unigrams from input file.
	"""
	return open(filename).read().split()

def generate_sentence(unigrams):
	"""
	Generates a random sentence composed of allowable unigram occurrences
	  found in the training text.
	"""
	# Generate a list of allowable initial words
	#   Initial words are capitalized and not punctuation.
	init_words = [word for word in unigrams if word[0].isupper()]

	# Select a random initial bigram.
	w1 = choice(init_words)
	sentence = []
	sentence.append(w1)

	# Search unigams for additional allowable words until an EOS
	#   marker is found.
	while True:
		w1 = choice(unigrams)
		sentence.append(w1)
		if w1 in EOS:
			break
	sentence = ' '.join(sentence)
	sentence = sentence.replace(' ,', ',')
	sentence = sentence.replace(' .', '.')
	return sentence

if __name__=='__main__':
	eng_unigrams = file2unigrams('LangId.train.English')
	print generate_sentence(eng_unigrams)
