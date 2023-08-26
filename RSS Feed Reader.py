import feedparser

def read_rss_feed(feed_url):
    feed = feedparser.parse(feed_url)
    
    print("Title:", feed.feed.title)
    print("Description:", feed.feed.description)
    
    print("Latest posts:")
    for entry in feed.entries:
        print(f"- {entry.title}: {entry.link}")

rss_feed_url = input("Enter RSS feed URL: ")
read_rss_feed(rss_feed_url)
