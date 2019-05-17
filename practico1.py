# -*- coding: utf-8 -*-
"""
Created on Fri May 17 16:05:59 2019

@author: Javier
"""
import json
import nltk
from nltk.corpus import stopwords 



def deleteStopWords(split_text):
    stop_words = set(stopwords.words('spanish'))
    
    for i in split_text:
        for j in stop_words:
            if(i == j):
                split_text.remove(i)
    return split_text
    
def readJson(file_name = "tweets.json"):
    with open(file_name, encoding='utf8') as file:
        tweets = json.load(file)
        for tweet in tweets['statuses']:
            #Eliminar stop words        
            split_text_stop = deleteStopWords(nltk.word_tokenize(tweet['text']))
            tokens_text = nltk.pos_tag(split_text_stop)

readJson()



    