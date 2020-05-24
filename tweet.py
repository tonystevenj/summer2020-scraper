from bs4 import BeautifulSoup
import requests



def getReplyer(id):
    url = "https://twitter.com/BryanAlexander/status/1250937008081514498"
    url="https://twitter.com/realdonaldtrump/status/1261793147069366279"
    f = requests.get(url)                 
    soup = BeautifulSoup(f.content, "lxml")  
    #print(f.text)

    #@classmethod

    tweet_div = soup.find('div', 'tweet')
    # print(tweet_div)
    replies = int(soup.find(
        'span', 'ProfileTweet-action--reply u-hiddenVisually').find(
        'span', 'ProfileTweet-actionCount')['data-tweet-stat-count'] or '0')
    is_replied = False if replies == 0 else True

    if is_replied == False:
        replies_to_users = []
    else:
        stream_items= \
            soup.find_all('div', 'stream-item-header')
        # print(stream_items)
        replies_to_users = []
        for k in stream_items:
            username = k.find('b').text.strip('@')
    #        username = "".join(username.split())
    #         print(username)
            replies_to_users.append(username)
        print(replies_to_users)

getReplyer(0)



