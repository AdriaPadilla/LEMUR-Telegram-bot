import tweepy

# Autorització de Twitter
auth = tweepy.OAuthHandler("", "")
auth.set_access_token("", "")

api = tweepy.API(auth)

def tweet(missatge):
    api.update_status(status=missatge)