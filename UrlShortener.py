# I am shortening the URL using TinyURL Service
# I am importing pyshorteners package for this purpose


import pyshorteners as pys

s = pys.Shortener()


def urlshortener(Url):
    shortUrl = s.tinyurl.short(Url)
    return shortUrl


# Main Function
if __name__ == "__main__":
    url = input("Enter the Original URL: ")
    short_url = urlshortener(url)
    print("\n")
    print("Original URL is:" + url)
    print("Shortened URL is:" + short_url)
