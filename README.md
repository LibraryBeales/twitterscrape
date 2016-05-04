This project contains two scripts to scrape the html saved from the twitter search results page to a csv file. 

hashtagcounts.py will create a list of all hashtags used in the search results with a count for each one.
twitterscrapetocsv.py creates a csv containing Username, Handle, Permalink, Time Stamp, Message Text, Images used in tweet (if any), Favorites, and ReTweets for each tweet in the search results.

This project uses saved html documents instead of live twitter pages because researchers will be referencing saved html pages as they frequently require a static version to include/reference in their publications. 

Coming improvements include:
Encoding in utf-8 so that encode/decode errors are not encountered when using the OS default encoding. 
VBA script to interpret and display html in Excel or Calc. 
Options to adjust time stamp to location of an event. 
Selenium browser used to search twitter and save html files, so this does not have to be done manually outside of the command line. 
Tutorials - For instructions on how to use these scripts, visit "Under Construction" 