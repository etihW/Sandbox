import feedparser

def main():
    d = feedparser.parse('https://www.reddit.com/r/dnd/.rss')
    read = int(input("How many posts do you want to see?\n"))
    print("---------------")
    print(d.feed.title)
    print("---------------\n")
    for x in range(1,read):
        print(d.entries[x].title)
        print()
main()
