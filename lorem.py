""" 
Filename: lorem.py
Author: Vicki Boykis
Date Modified: Nov 6 2015
Generate random lorem ipsem text in 10 files. 
(good if you need to test something against a batch of files )
"""


from loremipsum import get_sentences
   
def generate_lorem():
    sentences_list = get_sentences(5)
    return str(sentences_list)

def create_file(i):
    with open("%s.txt" % i , "w") as f:
    	data = f.write(generate_lorem())
       
if __name__ == "__main__":
	for i in xrange(0,10):
		create_file(i)
