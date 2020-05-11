import twint
import requests
import re
def get_retweeters_list(tweet_id):
    # get the data of retweets
    r = requests.get('https://twitter.com/i/activity/retweeted_popup?id='+str(tweet_id))
    # use the grep in order to get the retweeters
    text = r.text
    x = re.findall('div class=\\\\"account  js-actionable-user js-profile-popup-actionable \\\\" data-screen-name=\\\\"(.+?)\\\\" data-user-id=\\\\"', text)
    return x
# Configure
c = twint.Config()
c.Username = "realDonaldTrump"
# c.Search = "great"
c.Limit=10

# c.Tweet_id = "1257793742540386304"
c.Show_hashtags = True
c.Get_replies = True
print(get_retweeters_list("1258837711806496770"))
# Run
# twint.run.Profile(c)
c.Store_object= True
twint.run.Search(c)

tweets_as_objects = twint.output.tweets_list
print(type(tweets_as_objects))
# print(tweets_as_objects[0].id)
for tweet in tweets_as_objects:
    id = tweet.id
    print(str(id),":",get_retweeters_list(id))