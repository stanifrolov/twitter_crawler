from settings import consumer_key, consumer_secret, access_token, access_token_secret
from TwitterSearch import *

try:
    tso = TwitterSearchOrder()
    hashtags = ['#some']
    tso.set_keywords(hashtags)
    tso.set_include_entities(False)

    ts = TwitterSearch(
        consumer_key=consumer_key,
        consumer_secret=consumer_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
     )

    all_tweets = []
    filename = '_'.join(hashtags)
    file = open(filename + ".txt", "w", encoding='utf-8')

    for tweet in ts.search_tweets_iterable(tso):
        tweet = tweet['text']
        file.write(tweet + "\n")

    file.close()

except TwitterSearchException as e:
    print(e)
