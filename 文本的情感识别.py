# -*- coding: utf-8 -*-
"""
Created on Mon Apr 16 15:48:52 2018

@author: ArcherX
"""
from aip import AipNlp

import pandas as pd

""" 你的 APPID AK SK """

APP_ID = 'XXXXXXX'

API_KEY = 'XXXXXXXXXX'

SECRET_KEY = 'XXXXXXXXXXXX'

 

client = AipNlp(APP_ID, API_KEY, SECRET_KEY)

 

demotext = "百度情感分析API"

 

""" 调用情感倾向分析，返回具体数值 """

def get_sentiment(text):

    #print (text)

    json_data=client.sentimentClassify(text)   

    text=json_data['text']

    items=json_data['items']

    items=items[0]

    positive_prob=items['positive_prob']

    confidence=items['confidence']

    negative_prob=items['negative_prob']

    sentiment=items['sentiment']

    return text,positive_prob,confidence,negative_prob,sentiment

 

print (get_sentiment(demotext))
