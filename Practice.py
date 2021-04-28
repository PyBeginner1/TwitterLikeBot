import tweepy       #Tweepy is an open source  package that gives you a very convenient way to access the Twitter API with Python
import time

#after creating acc in developer portal, click on create app & after generte the keys
auth=tweepy.OAuthHandler('consumer_key', 'consumer_secret')
auth.set_access_token('access_token', 'access_token_secret')

api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

#api.update_status("Hello")

#to get myself
user=api.me()

#reeturn names of my followers
for follower in tweepy.Cursor(api.followers).items():
   print(follower.name)

#follow
name="imVkohli"
api.create_friendship(name)
print(f"Followed {name}")

#trends
api.trends_place(1)



#search tweets &like tweets
search ='webdevelopment'
for tweet in tweepy.Cursor(api.search, search).items(500):          #500 items
    try:
        print("Tweet liked")
        tweet.retweet()            #likes tweet
        time.sleep(5)
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break



