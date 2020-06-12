# This file is used to summarize how to label the collect data:

The data are in **json** format, here is one sample:

{"CONTENT":"\u201cThe fatality rate [of the coronavirus] is 200\/10,000, which is currently lower compared to many other viruses including SARS, so if it was meant as a bioweapon, it is not a good one.\"\n https:\/\/www.buzzfeednews.com\/article\/ryanhatesthis\/a-pro-trump-blog-has-doxed-a-chinese-scientist-it-falsely\u00a0\u2026","TWEET_ID":"1223395526223118336","USER_NAME":"simonplittle","POST_DATE":"2020-01-31","POST_TIME":"18:59:57","LINK":"https:\/\/twitter.com\/simonplittle\/status\/1223395526223118336","URL_INCLUDED":["https:\/\/www.buzzfeednews.com\/article\/ryanhatesthis\/a-pro-trump-blog-has-doxed-a-chinese-scientist-it-falsely"],"RETWEETS_COUNT":0,"RETWEETS_PEOPLE":[],"LIKES_AMOUNT":"1","REPLIIES_AMOUNT":0,"REPLAY_PEOPLE":[],"REPLAY_TIME":[],"REPLAY_CONTENT":[]},

## The steps for labelling:

* Focus on the content: read through the text of tweet. If the content contains words like: click this video, click this link, follow me, look at the video... be careful!! It may be a ** '**spam**' **.
* Manually check the content: you can put the tweet into Google and search it. Google will give some info about the content, if it looks like rumor or had been notified as rumor/spam in goole, then you can lable it as ** '**spam**' **.
* Check the URL link in the content: for example, you can put the link in above sample into browser, then the link will give you some info. If the link points to virus or illgal content, then it must be a spam. If it points to legal web, then based on former steps and it looks fine, we can label it as ** '**non-spam**' **.
* If you cannot make sure about the news, you can search the related keyword in google to find it is fake or real news. It may take some time to identify it.
* If all above steps still cannot identify the tweet, then you can search it in Twitter. If no any labels (rumor, malicious, ...) in Twitter, we can label it as ** '**non-spam**' **.