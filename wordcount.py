#!/usr/bin/env python
# Copyright (c) 2013 the authors listed at the following URL, and/or
# the authors of referenced articles or incorporated external code:
# http://en.literateprograms.org/Word_count_(Python)?action=history&offset=20121008175907
# 
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
# CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
# TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
# SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# 
# Retrieved from: http://en.literateprograms.org/Word_count_(Python)?oldid=18680


from optparse import OptionParser
import sys

parser = OptionParser(usage="usage: %prog [options] [file1 file2 ...]")
parser.add_option("-c", "--char", 
                  dest="characters", 
                  action="store_true",
                  default=False,
                  help="Only count characters")
parser.add_option("-w", "--words", 
                  dest="words", 
                  action="store_true",
                  default=False,
                  help="Only count words")
parser.add_option("-l", "--lines", 
                  dest="lines", 
                  action="store_true",
                  default=False,
                  help="Only count lines")
(options, args) = parser.parse_args()
if not (options.characters or options.words or options.lines):
    options.characters, options.words, options.lines = True, True, True

def get_count(data):
    lines = len(data)
    words = sum(len(x.split()) for x in data)
    chars = sum(len(x) for x in data)
    return lines, words, chars

def print_count(lines, words, chars, filename):
    print "\t",
    if options.lines:
        print lines, "\t",
    if options.words:
        print words, "\t",
    if options.characters:
        print chars, "\t",
    print filename

if args:

    total_lines = 0
    total_words = 0
    total_chars = 0
    file_count = 0

    for file_string in args:
        #this comment is there to prevent a literateprograms bug messing up the indentation (which is fatal in python)
	    platforms_needing_glob = ["os10"] # please populate!
	    if sys.platform in platforms_needing_glob:
	        import glob
	        file_list = glob.glob(file_string)
	    else:
	        file_list = [file_string]
	    for file_name in file_list:
	        file = open(file_name)
	        data = file.readlines()

	        lines, words, chars = get_count(data)
	        print_count(lines, words, chars, file_name)

	        total_lines += lines
	        total_words += words
	        total_chars += chars
	        file_count += 1
    if file_count > 1:
        print_count(total_lines, total_words, total_chars, "total") 
    
else:
    file = sys.stdin
    data = file.readlines()

    lines, words, chars = get_count(data)
    print_count(lines, words, chars, "")

