# This file is used to summarize how to label the collect data:

The data are in **json** format, here is one sample:

```javascript
{"CONTENT":"\u201cThe fatality rate [of the coronavirus] is 200\/10,000, which is currently lower compared to many other viruses including SARS, so if it was meant as a bioweapon, it is not a good one.\"\n https:\/\/www.buzzfeednews.com\/article\/ryanhatesthis\/a-pro-trump-blog-has-doxed-a-chinese-scientist-it-falsely\u00a0\u2026","TWEET_ID":"1223395526223118336","USER_NAME":"simonplittle","POST_DATE":"2020-01-31","POST_TIME":"18:59:57","LINK":"https:\/\/twitter.com\/simonplittle\/status\/1223395526223118336","URL_INCLUDED":["https:\/\/www.buzzfeednews.com\/article\/ryanhatesthis\/a-pro-trump-blog-has-doxed-a-chinese-scientist-it-falsely"],"RETWEETS_COUNT":0,"RETWEETS_PEOPLE":[],"LIKES_AMOUNT":"1","REPLIIES_AMOUNT":0,"REPLAY_PEOPLE":[],"REPLAY_TIME":[],"REPLAY_CONTENT":[]}
```


## The steps for labelling:

* Focus on the content: read through the text of a tweet. If the content contains words like: click this video, click this link, follow me, look at the video... be careful!! It may be a **spam**.
* Manually check the content: you can put the tweet into Google and search it. Google will give some info about the content, if it looks like rumor or had been notified as rumor/spam in Google, then you can label it as ** '**spam**' **.
* Check the URL link in the content: for example, you can put the link in above sample into browser, then the link will give you some info. If the link points to virus or illgal content, then it must be a spam. If it points to a legal web, then based on former steps and it looks fine, we can label it as **true news**.
* If you cannot make sure about the news, you can search the related keyword in Google to find it is fake or real news. It may take some time to identify it.
* If all above steps still cannot identify the tweet, then you can search it in Twitter. If no any labels (rumor, malicious, ...) in Twitter, we can label it as **true news**.
* For the fake ones, you need to prepare an excel to document the reason why you judge it as **fake**. A short description will be enough. 
* We are expecting around 10% of all the tweets are **fake**.
* If some tweets just express opinion, you can label it as **opinion**, which will be excluded when we train the model.  

## After labelling:

You can directly modify the original json file like:

```javascript
{"CONTENT"xxx,"REPLAY_TIME":[],"REPLAY_CONTENT":[],"LABEL":"1"}
```
Adding an entry at the end, of **"LABEL":"1"**.

The label 0 means **true news**.

The label 1 means **fake news**.

The label 2 means **opinion**.
