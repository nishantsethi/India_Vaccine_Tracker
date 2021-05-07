import tweepy
from Credentials.Keys import api_key,api_secret_key,access_token,access_token_secret
from VaccineBar import VaccinesBar

#Auth
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)


api = tweepy.API(auth)

# toTweet = VaccinesBar()
# if toTweet != "Same Data":
#     api.update_status(toTweet)

api.update_status("test")