from bs4 import BeautifulSoup
import requests
import sys
import csv
import re
import operator

url = input("Enter the name of the file to be scraped:")
with open(url, encoding="utf-8") as infile:
	soup = BeautifulSoup(infile, "html.parser")

tags = soup('a', {'class': 'twitter-hashtag pretty-link js-nav'})
alltag = [tag.contents[1].string for tag in tags]

alltags = [item.lower() for item in alltag]

counts = dict((items, alltags.count(items)) for items in alltags)

sorted_counts = sorted(counts.items(), key = operator.itemgetter(0))

newfile = input("Enter a filename for the hastag counts:") + ".csv"

#with open(newfile, 'w') as out:
#	csv_out=csv.writer(out)
#	csv_out.writerow(['Hashtag', 'Count'])
#	for row in sorted_counts:
#		csv_out.writerow(row)

with open(newfile, 'w', encoding='utf-8') as f:
	writer = csv.writer(f, delimiter=",")
	writer.writerow(['Hashtag', 'Count'])
	for row in sorted_counts:
		writer.writerow(row)

