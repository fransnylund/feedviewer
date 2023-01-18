#!/usr/bin/python

import feedparser
import sys

def usage():
    print("Error: Incorrect number of args.\nUsage: ./feedlistener [<URL>]")
    quit()

# Choose news source
def feed_chooser():
    print("Choose a news source:\n")
    print("1. CNN")
    print("2. Wall Street Journal")
    print("3. Ilta-sanomat")
    print("4. The New York Times")
    print("5. Fox News")
    print("6. Reddit")
    print("7. Enter custom URL")
    print("")
    choice = input()

    if choice == "1":
            return "http://rss.cnn.com/rss/edition_world.rss"
    elif choice == "2":
            return "http://feeds.a.dj.com/rss/RSSWorldNews.xml"
    elif choice == "3":
            return "https://www.is.fi/rss/tuoreimmat.xml"
    elif choice == "4":
            return "http://rss.nytimes.com/services/xml/rss/nyt/World.xml"
    elif choice == "5":
            return "http://moxie.foxnews.com/google-publisher/world.xml"
    elif choice == "6":
            return "http://reddit.com/r/news.rss"
    elif choice == "7":
            return input()
    else:
        print("Enter a valid number.")
        quit()

if len(sys.argv) > 2:
    usage()

if len(sys.argv) == 2:
    file = feedparser.parse(sys.argv[1])
else:
    feed_choice = feed_chooser()
    file = feedparser.parse(feed_choice)

# Display RSS elements
print("""
The website is : """ + file['feed']['link'] + """
The feed is : """ + file['feed']['title'] + """
Last updated : """ + file['feed']['updated'] + "\n")


i = 0

# Loop through all entries
for elem in file['entries']:
    print(i + 1, ":" , file.entries[i].title)
    print(file.entries[i].link)
    print('\n')
    i += 1



