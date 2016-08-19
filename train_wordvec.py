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

	# default parameters
	lr=0.005
	dim=100
	ws=5
	epoch=5
	min_count=1
	neg=5
	word_ngrams=1
	loss='ns'
	bucket=2000000
	minn=3
	maxn=6
	thread=4
	lr_update_rate=10000
	t=1e-4
	silent=0

	if model_type == 'skipgram' :
		# Skipgram model
		model = fasttext.skipgram(train_path, model_path, lr, dim, ws, epoch, \
								  min_count, neg, word_ngrams, loss, bucket, \
								  minn, maxn, thread, lr_update_rate, t, silent)
		if VERBOSE : print model.words
	else :
		# CBOW model
		model = fasttext.cbow(train_path, model_path, lr, dim, ws, epoch, \
							  min_count, neg, word_ngrams, loss, bucket, \
							  minn, maxn, thread, lr_update_rate, t, silent)
		if VERBOSE : print model.words
	

	
