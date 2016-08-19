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
	parser.add_option("-t", "--train", dest="train_path", help="train file path", metavar="train_path")
	parser.add_option("-m", "--model", dest="model_path", help="model file path", metavar="model_path")
	parser.add_option("-y", "--type", dest="type", help="model type, ex) skipgram, cbow", metavar="type")
	(options, args) = parser.parse_args()
	if options.verbose == 1 : VERBOSE = 1
	train_path = options.train_path
	model_path = options.model_path
	if train_path == None or model_path == None :
		parser.print_help()
		exit(1)
	model_type = options.type
	if not model_type : model_type = 'skipgram'

	if model_type == 'skipgram' :
		# Skipgram model
		model = fasttext.skipgram('data.txt', 'model')
		if VERBOSE : print model.words # list of words in dictionary
	else :
		# CBOW model
		model = fasttext.cbow('data.txt', 'model')
		if VERBOSE : print model.words # list of words in dictionary
	

	
