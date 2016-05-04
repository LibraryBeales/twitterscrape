from bs4 import BeautifulSoup
import requests
import sys
import csv
import re
import operator

url = input("Enter the name of the file to be scraped:")
r = open(url)
soup = BeautifulSoup(r.read())

tags = soup('a', {'class': 'twitter-hashtag pretty-link js-nav'})
alltag = [tag.contents[1].string for tag in tags]

alltags = [item.lower() for item in alltag]

counts = dict((items, alltags.count(items)) for items in alltags)

print (counts)

sorted_counts = sorted(counts.items(), key = operator.itemgetter(0))

print (sorted_counts)

newfile = input("Enter a filename for the hastag counts:") + ".csv"

with open(newfile, 'w') as out:
	csv_out=csv.writer(out)
	csv_out.writerow(['Hashtag', 'Count'])
	for row in sorted_counts:
		csv_out.writerow(row)


#This dictionary maintains the capitalization and separates hastags that have identical spelling but separate capitaliztion, 
#the capitaliztion may matter to you so I decided to keep it.  I can also just make everything lowercase and count that way if you want.
