import twint
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from time import strftime, localtime
import time
def getReplyer(name, id):
    replies_to_users = []
    replies_time = []
    replies_content = []
    url = "https://twitter.com/" + str(name) + "/status/" + str(id)
    # print(url)
    f = requests.get(url, headers={"X-Requested-With": "XMLHttpRequest"})  
    soup = BeautifulSoup(f.content, "lxml")  
    # print(f.text)

    # @classmethod

    tweet_div = soup.find('div', 'tweet')
    # print(tweet_div)
    tem = soup.find(
        'span', 'ProfileTweet-action--reply u-hiddenVisually')
    if tem is None:
        return replies_to_users,replies_time,replies_content
    replies = int(tem.find(
        'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0')
    is_replied = False if replies == 0 else True

    if is_replied == False:
        pass
    else:
        stream_items = \
            soup.find_all('div', 'content')
        # print(stream_items)
        for k in stream_items:

            try:
                username = k.find('div', class_='stream-item-header').find('b').text.strip('@')
 #              time = k.find('small', 'time').find('a')['title']
                time = int(k.find('div', class_='stream-item-header').find('small', 'time').find("span", "_timestamp")["data-time-ms"])
 #              datestamp = strftime("%Y-%m-%d", localtime(time/1000.0))
                timestamp = strftime("%Y-%m-%d,%H:%M:%S", localtime(time/1000.0))
                replytext = k.find('div', class_='js-tweet-text-container').find('p', 'tweet-text').text or ""

            except:
                continue
            #        username = "".join(username.split())
            #         print(username)
            #         print(time)
            replies_to_users.append(username)
            replies_time.append(timestamp)
            replies_content.append(replytext)
        # print(replies_to_users)
    return replies_to_users,replies_time,replies_content
def get_retweeters_list(tweet_id):
    # get the data of retweets
    r = requests.get('https://twitter.com/i/activity/retweeted_popup?id=' + str(tweet_id), headers={"X-Requested-With": "XMLHttpRequest"})
    # r = requests.get('https://twitter.com/BryanAlexander/status/' + str(tweet_id))
    # use the grep in order to get the retweeters

    text = r.text
    x = re.findall(
        'div class=\\\\"account  js-actionable-user js-profile-popup-actionable \\\\" data-screen-name=\\\\"(.+?)\\\\" data-user-id=\\\\"',
        text)
    return x
def twintScraper(from_date=None, end_date=None):

    # Configure
    c = twint.Config()
    c.Username = "realDonaldTrump"
    # c.Search = "coronavirus"
    c.Limit = 10

    # c.Tweet_id = "1257793742540386304"
    c.Show_hashtags = True
    c.Get_replies = True
    c.Verified = True
    c.Stats = True
    c.Count = True
    c.Lang = "en"
    c.Hide_output = True
    # c.Resume = "1223026504482918405"
    # print(get_retweeters_list("1258837711806496770"))
    # twint.run.Profile(c)
    c.Store_object = True
    # c.Since = "2020-01-30 00:00:00"
    # c.Until ="2020-02-01 00:00:00"
    c.Since = from_date
    c.Until =end_date
    # c.Until =str(datetime.datetime.now())[:19]
    # print(str(datetime.datetime.now())[:19])
    # exit()
    twint.run.Search(c)

    tweets_as_objects = twint.output.tweets_list
    print("Real tweets amount: ", len(tweets_as_objects))
    dict_op = {
            "CONTENT": [],
            "TWEET_ID": [],
            "USER_NAME": [],
            "POST_DATE": [],
            "POST_TIME": [],
            "LINK": [],
            "URL_INCLUDED": [],
            "RETWEETS_COUNT": [],
            "RETWEETS_PEOPLE": [],
            "LIKES_AMOUNT": [],
            "REPLIIES_AMOUNT": [],
            "REPLAY_PEOPLE": [],
            "REPLAY_TIME": [],
            "REPLAY_CONTENT": []

    }
    count =0
    for tweet in tweets_as_objects:
        id = tweet.id
        name = tweet.username
        # print(name,"HHHHHHHHHHHHHHHHHHHHHHHH")
        likes_amount = tweet.likes_count
        retweets_count = tweet.retweets_count
        replies_count = tweet.replies_count
        replies_people=[]

        replies_time=[]
        replies_content=[]
        replies_people, replies_time, replies_content=getReplyer(name, id)
        print(
            count,
            " CONTENT: ", tweet.tweet,
            " TWEET_ID: ", str(id),
            " USER_NAME: ", str(name),
            " POST_DATE: ",tweet.datestamp,
            " POST_TIME: ",tweet.timestamp,
            " LINK: ", tweet.link,
            " URL_INCLUDED: ", tweet.urls,
            " RETWEETS_COUNT: ", len(get_retweeters_list(id)),
            " RETWEETS_PEOPLE: ", get_retweeters_list(id),
            " LIKES_AMOUNT: ", likes_amount,
            " REPLIIES_AMOUNT: ", len(replies_people),
            " REPLAY_PEOPLE: ", replies_people,
            " REPLAY_TIME: ", replies_time,
            " REPLAY_CONTENT: ", replies_content
        )
        dict_op["CONTENT"].append(tweet.tweet)
        dict_op["TWEET_ID"].append(str(id))
        dict_op["USER_NAME"].append(str(name))
        dict_op["POST_DATE"].append(tweet.datestamp)
        dict_op["POST_TIME"].append(tweet.timestamp)
        dict_op["LINK"].append(tweet.link)
        dict_op["URL_INCLUDED"].append(tweet.urls)
        dict_op["RETWEETS_COUNT"].append(len(get_retweeters_list(id)))
        dict_op["RETWEETS_PEOPLE"].append(get_retweeters_list(id))
        dict_op["LIKES_AMOUNT"].append(likes_amount)
        dict_op["REPLIIES_AMOUNT"].append(len(replies_people))
        dict_op["REPLAY_PEOPLE"].append(replies_people)
        dict_op["REPLAY_TIME"].append(replies_time)
        dict_op["REPLAY_CONTENT"].append(replies_content)
        count+=1
        if (count%200==0 and count!=0) or count==len(tweets_as_objects):
            lastsavedtweetid = dict_op["TWEET_ID"][len(dict_op["TWEET_ID"])-1]
            print(f"SAVE_MARK {count}: lasts aved tweetid = ",lastsavedtweetid)
            df = pd.DataFrame(data=dict_op)
            df.to_json(f"{from_date} {count} COVID-19.json",orient='records')
            dict_op = {
                "CONTENT": [],
                "TWEET_ID": [],
                "USER_NAME": [],
                "POST_DATE": [],
                "POST_TIME": [],
                "LINK": [],
                "URL_INCLUDED": [],
                "RETWEETS_COUNT": [],
                "RETWEETS_PEOPLE": [],
                "LIKES_AMOUNT": [],
                "REPLIIES_AMOUNT": [],
                "REPLAY_PEOPLE": [],
                "REPLAY_TIME": [],
                "REPLAY_CONTENT": []
            }
        if count%1000==0 and count!=0:
            time.sleep(60.0)

# c.Since = "2020-01-30 00:00:00"
# c.Until ="2020-02-01 00:00:00"

# twintScraper(from_date="2020-01-31" ,end_date="2020-02-01" )
# twintScraper(from_date="2020-01-30" ,end_date="2020-01-31" )
# twintScraper(from_date="2020-01-29" ,end_date="2020-01-30" )
# twintScraper(from_date="2020-01-28" ,end_date="2020-01-29" )
# twintScraper(from_date="2020-01-27" ,end_date="2020-01-28" )
# twintScraper(from_date="2020-01-26" ,end_date="2020-01-27" )



# twintScraper(from_date="2020-02-29" ,end_date="2020-03-01" )
twintScraper(from_date="2020-02-28" ,end_date="2020-02-29" )
# for i in reversed(range(10,14)):
#     from_date = f"2020-02-{i}"
#     end_date = f"2020-02-{i+1}"
#     print(f"DAY_MARK: ",from_date," ",end_date)
#     try:
#         twint.output.tweets_list = []
#         twintScraper(from_date=from_date ,end_date=end_date )
#     except:
#         pass

# twintScraper(from_date="2020-01-09" ,end_date="2020-01-10" )
# for i in reversed(range(0,9)):
#     from_date = f"2020-01-0{i}"
#     end_date = f"2020-01-0{i+1}"
#     print(f"DAY_MARK: ",from_date," ",end_date)
#     try:
#         twint.output.tweets_list = []
#         twintScraper(from_date=from_date ,end_date=end_date )
#     except:
#         pass

