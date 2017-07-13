import json

rFile = open('./text_reviews.txt','r')
wFile = open('./refined_reviews.txt','w')

#while True:
for i in range(1000):
	data = rFile.readline()
	if not data: break
	if not data.isspace():
		wFile.write(data)
