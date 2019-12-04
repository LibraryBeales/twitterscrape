This project uses two scripts to scrape the html saved from the twitter search results page to a csv file. 

hashtagcounts.py will create a list of all hashtags used in the search results with a count for each one.  This is useful for determining what other hashtags are used with the hashtags selected for the search.

twitterscrapetocsv.py creates a csv containing Username, Handle, Permalink, Time Stamp, Message Text, Images used in tweet (if any), Favorites, and ReTweets for each tweet in the search results.
There are options for adjusting the timestamp and all encoding forced to utf-8 so OS and document encoding conflicts are minimized.

This project uses saved html documents instead of live twitter pages, as researchers will be referencing saved html pages.  Documentation for research frequently requires a static version to include/reference in  publications. 

Improvements could include:

* VBA script to interpret and display html in Excel or Calc
* Selenium browser used to search twitter and save html files, so this does not have to be done manually outside of the command line
* Tutorials - For instructions on how to use these scripts, visit "Under Construction"

* **DONE** Encoding in utf-8 in order to avoid charmap errors on encode and decode when using the OS default encoding

* **DONE** Option to adjust time stamp to one other than location of twitter search
