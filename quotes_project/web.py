from sys import api_version
from py import apipkg
import tweepy
import requests
from bs4 import BeautifulSoup
import random
import time

class webScraper:
        def twitter():
                global twitter_stuff
        # twitter api details
                auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
                auth.set_access_token(access_token, access_token_secret)
                api = tweepy.API(auth)
        # lists
                twitter_details = [consumer_key, consumer_secret, access_token, access_token_secret]
                twitter_auth = [auth, api]
        # join the two lists
                twitter_stuff = [twitter_details, twitter_auth]
        twitter()    
        def webScrape():
                global quote
                url = "https://www.goodreads.com/quotes/tag/stoicism?page=2"
                page = requests.get(url)
                soup = BeautifulSoup(page.content, "html.parser")
                quotes = soup.find_all("div", class_="quoteText")
                quoteS = random.choice(quotes)
                quote = quoteS.text
                quote = quote.replace("“", "")
                quote = quote.replace("”", "")
                quote = quote.replace("", "") 
                
        webScrape()

class test:
        def duplicated(): # if the quote is duplicated the function will loop again until it finds a new quote
                while quote != quote:
                        print("Quote is duplicated")
                        return
                else:
                        quote == quote # if the quote is not duplicated the function will stop
                        webScraper.webScrape()
                        print(quote)
        duplicated()
        def tooLong(): # if the quote is too long the function will loop again until it finds a new quote
                while len(quote) > 280:
                        return
                else:
                        len(quote) < 280
                        webScraper.webScrape
        tooLong()


# main function that will run the program and break
def main():
        webScraper.twitter()
main()
