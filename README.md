This project contains two scripts to scrape the html saved from the twitter search results page to a csv file. 

hashtagcounts.py will create a list of all hashtags used in the search results with a count for each one.  This is useful for determining what other hashtags are used with the hashtags selected for the search.

twitterscrapetocsv.py creates a csv containing Username, Handle, Permalink, Time Stamp, Message Text, Images used in tweet (if any), Favorites, and ReTweets for each tweet in the search results.

This project uses saved html documents instead of live twitter pages because researchers will be referencing saved html pages as they frequently require a static version to include/reference in their publications. 

Coming improvements include:

* Encoding in utf-8 in order to avoid charmap errors on encode and decode when using the OS default encoding.
* VBA script to interpret and display html in Excel or Calc