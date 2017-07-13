import codecs
import json

File = codecs.open('./yelp_academic_dataset_review.json','r','utf-8')
wFile = codecs.open('./text_reviews.txt','w','utf-8')

for x in range(2000):
        data = File.readline()
        json_data = json.loads(data)
        review = json_data['text']
        wFile.write(review)