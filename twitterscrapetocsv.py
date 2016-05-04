from bs4 import BeautifulSoup
import requests
import sys
import csv
import re


url = input("Enter the name of the file to be scraped:")
r = open(url)
soup = BeautifulSoup(r.read())

#url = 'https://twitter.com/search?q=%23bangkokbombing%20since%3A2015-08-10%20until%3A2015-09-30&src=typd&lang=en'
#headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'}
#r = requests.get(url, headers=headers)
#data = r.text.encode('utf-8')
#soup = BeautifulSoup(data, "html.parser")

names = soup('strong', {'class': 'fullname js-action-profile-name show-popup-with-id'})
usernames = [name.contents[0] for name in names]

handles = soup('span', {'class': 'username js-action-profile-name'})
userhandles = [handle.contents[1].contents[0] for handle in handles]  
athandles = [('@')+abhandle for abhandle in userhandles]

links = soup('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})
urls = [link["href"] for link in links]
fullurls = [('http://www.twitter.com')+permalink for permalink in urls]

timestamps = soup('a', {'class': 'tweet-timestamp js-permalink js-nav js-tooltip'})
datetime = [timestamp["title"] for timestamp in timestamps]

messagetexts = soup('p', {'class': 'TweetTextSize  js-tweet-text tweet-text'}) 
messages = [messagetext for messagetext in messagetexts]  

retweets = soup('button', {'class': 'ProfileTweet-actionButtonUndo js-actionButton js-actionRetweet'})
retweetcounts = [retweet.contents[3].contents[1].contents[1].string for retweet in retweets]

favorites = soup('button', {'class': 'ProfileTweet-actionButtonUndo u-linkClean js-actionButton js-actionFavorite'})
favcounts = [favorite.contents[3].contents[1].contents[1].string for favorite in favorites]

images = soup('div', {'class': 'content'})
imagelinks = [src.contents[5].img if len(src.contents) > 5 else "No image" for src in images]

print (usernames, "\n", "\n", athandles, "\n", "\n", fullurls, "\n", "\n", datetime, "\n", "\n",retweetcounts, "\n", "\n", favcounts, "\n", "\n", messages, "\n", "\n", imagelinks)

rows = zip(usernames,athandles,fullurls,datetime,retweetcounts,favcounts,messages,imagelinks)

rownew = list(rows)

print (rownew)

with open('scrapeddataimg.csv', 'w') as f:
	writer = csv.writer(f)
	for row in rownew:

		writer.writerow(row)


#Save html instead of web
#edit code to analyze saved file
#html in chrome or safari
#import into access
#dates - August 10 to December 31
#html display in excel
#hashtag list from Penn
#list of software - Firefox - Sublime Text
#no text edit
#timestamp intwitter?  your timezone or poster?
#profile image
#count/list of hastags - csv or page - not connected to posts - hashtags with counts - dictionary
#
