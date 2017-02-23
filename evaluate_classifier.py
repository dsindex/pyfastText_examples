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
	parser.add_option("-t", "--test", dest="test_path", help="test file path", metavar="test_path")
	(options, args) = parser.parse_args()
	if options.verbose == 1 : VERBOSE = 1
	test_path = options.test_path
	model_path = options.model_path
	if test_path == None or model_path == None :
		parser.print_help()
		exit(1)

	classifier = fasttext.load_model(model_path)

	result = classifier.test(test_path)
	print 'P@1:', result.precision
	print 'R@1:', result.recall
	print 'Number of examples:', result.nexamples	

	
