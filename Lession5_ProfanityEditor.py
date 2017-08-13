import urllib

def read_text():
    quotes = open("/Users/tiennguyen/Documents/movie_quotes.txt")
    contents_quote = quotes.read()
    print(contents_quote)
    check_profanity(contents_quote)
    quotes.close()

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    connection.close()

    if "true" in output:
        print("Profanity Alert!!")
    else:
        print("No curse words!!")

read_text()
