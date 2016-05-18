from twython import Twython, TwythonError
import time
import random
from datetime import datetime

app_key = "SECRET"
app_secret = "SECRET"
oauth_token = "SECRET"
oauth_token_secret = "SECRET"

twitter = Twython(app_key, app_secret, oauth_token, oauth_token_secret)

bad_words = ["Sucks", "Boring", "Hate", "Store", "Shirts", "Buy", "Merchandise", "shirts", "merchandise", "buy", "BUY", "SHIRTS"]
good_words = ["Rick and Morty", "Rick Morty", "RickandMorty"]
filter = " OR ".join(good_words)
blacklist = " -".join(bad_words)
keywords = filter + blacklist


while True:
    try:
        search_results = twitter.search(q=keywords, count=15)
        for tweet in search_results["statuses"]:
            id=tweet['id']
            name= "@" + tweet['user']['screen_name']
            try:
                twitter.update_status(status="%s My Man!" % (name), in_reply_to_status_id=id)
                #twitter.update_status(status="Test")
                now = datetime.now()
                print "Replying to %s on " % (name)
                print '%s/%s/%s at %s:%s:%s \n' % (now.month, now.day, now.year, now.hour, now.minute, now.second)
                time.sleep(600)
            except Exception as e:
                raise
    except TwythonError as e:
        print e
