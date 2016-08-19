#!/bin/env python
#-*- coding: utf8 -*-

import sys
import os
from   optparse import OptionParser
import fasttext

# --verbose
VERBOSE = 0

if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option("--verbose", action="store_const", const=1, dest="verbose", help="verbose mode")
	parser.add_option("-m", "--model", dest="model_path", help="model file path", metavar="model_path")
	(options, args) = parser.parse_args()
	if options.verbose == 1 : VERBOSE = 1
	model_path = options.model_path
	if model_path == None :
		parser.print_help()
		exit(1)

	classifier = fasttext.load_model(model_path)
		
	i = 0
	while 1 :
		try : line = sys.stdin.readline()
		except KeyboardInterrupt : break
		if not line : break
		line = line.strip()
		if not line : continue

		texts = [line]
		labels = classifier.predict(texts)
		print labels

		i += 1
