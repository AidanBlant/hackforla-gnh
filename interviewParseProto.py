from __future__ import unicode_literals
import spacy, re

# Set up spaCy
from spacy.en import English
parser = English()

# Test Data
multiSentence = "There is an art, it says, or rather, a knack to flying." \
                 "The knack lies in learning how to throw yourself at the ground and miss." \
                 "In the beginning the Universe was created. This has made a lot of people "\
                 "very angry and been widely regarded as a bad move."

fname = "Aidan Blant, Midway City, CA 080417.001.txt"
with open(fname) as f:
    content = f.readlines()
content = [x.strip() for x in content]
# print("len(content): ",len(content));


## PROCESS HEADER FOR NAME, LOCATION, INTERVIEWID

# First line should be the name, city, and interview id
header = re.split(",",content[0])
fname,lname = header[0].split()
city = header[1]
state,idnum = header[2].split()
print("First: {} | Last: {} | City: {} | State {} | id#: {}".format(fname,lname, city,state,idnum))


## SEPERATE DIALOGUE SPOKEN BY INTERVIEWER AND INTERVIEW SUBJECT
# In these examples, Paula's lines start with her full name, or initial 
# Unfortunately there are lines with NO indicator
	 # TODO: Find method that covers majority of cases with high accuracy

paulaLine = []
intervieweeLine = []
unknownLine = []

for i in range(1,len(content)):
	# if( len( content[i] ) >= 5 ):
	# Split has a second parameter, maxsplit to specify number of splits
	# since we only want first "word" or indicator s2 = line.split(' ', 1)[1]

	firstWord = content[i].split(' ', 1)
	if( not firstWord[0] ):
		continue;
	# print firstWord[0]

	if( firstWord[0] == "P:" or firstWord[0] == "Paula:" ):
		# print "This is Paula's line"
		paulaLine.append(content[i])
	elif( firstWord[0] == fname[0]+":" or firstWord[0] == fname+":" ):
		# print "This is interviewee's line"
		intervieweeLine.append(content[i])
	else:
		unknownLine.append(content[i])


#Having issues with unicode to string conversion

# for j in range (len(intervieweeLine)):
	# map(unicode,intervieweeLine[j])
	
	# print (j," ",intervieweeLine[j])
	# parsedData = parser(intervieweeLine[j])

	# for i, token in enumerate(parsedData):
	#     print("original:", token.orth, token.orth_)
	#     print("lowercased:", token.lower, token.lower_)
	#     print("lemma:", token.lemma, token.lemma_)
	#     print("shape:", token.shape, token.shape_)
	#     print("prefix:", token.prefix, token.prefix_)
	#     print("suffix:", token.suffix, token.suffix_)
	#     print("log probability:", token.prob)
	#     print("Brown cluster id:", token.cluster)
	#     print("----------------------------------------")
	#     if i > 1:
	#         break	

