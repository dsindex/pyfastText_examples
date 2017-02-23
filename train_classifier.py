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
	(options, args) = parser.parse_args()
	if options.verbose == 1 : VERBOSE = 1
	train_path = options.train_path
	model_path = options.model_path
	if train_path == None or model_path == None :
		parser.print_help()
		exit(1)
	'''
	input_file              training file path (required)
	output                  output file path (required)
	label_prefix            label prefix ['__label__']
	lr                      learning rate [0.1]
	lr_update_rate          change the rate of updates for the learning rate [100]
	dim                     size of word vectors [100]
	ws                      size of the context window [5]
	epoch                   number of epochs [5]
	min_count               minimal number of word occurences [1]
	neg                     number of negatives sampled [5]
	word_ngrams             max length of word ngram [1]
	loss                    loss function {ns, hs, softmax} [softmax]
	bucket                  number of buckets [0]
	minn                    min length of char ngram [0]
	maxn                    max length of char ngram [0]
	thread                  number of threads [12]
	t                       sampling threshold [0.0001]
	silent                  disable the log output from the C++ extension [1]
	encoding                specify input_file encoding [utf-8]
	pretrained_vectors      pretrained word vectors (.vec file) for supervised learning []
	'''
	classifier = fasttext.supervised(train_path, model_path, label_prefix='__label__', lr=0.1, epoch=1000, word_ngrams=1, dim=100, ws=5, bucket=10000, minn=3, maxn=5, silent=0)
	
