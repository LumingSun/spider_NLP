# -*- coding: utf-8 -*-
import sys
import pynlpir
import jieba
from topic_list import *
from jieba import analyse
from collections import Counter
import time
import datetime
import json
# reload(sys)
# sys.setdefaultencoding('utf8')


def getKeyWords(string,words = 10,way=1):
    keywords = []
    if (way == 1):
        pynlpir.open()
        str = string.encode('utf-8')
        wordslist = pynlpir.get_key_words(str,words,False)
        for each in wordslist:
            # print(each)
            keywords.append(each)
    if (way == 2):
        textrank = analyse.textrank
        wordslist = textrank(string)
        for each in wordslist[0:words]:
            # print(each)
            keywords.append(each)
    return keywords


def fenci(string,way=1):
    result = []
    if (way == 1):
        pynlpir.open()
        string = string.encode('utf-8')
        wordslist = pynlpir.segment(string)
        for item in wordslist:
            result.append(item[0])
    if (way == 2):
        words = jieba.cut(string)
        for each in words:
            result.append(each)
    length = len(result)
    return result,length


def find_topic(string,words_dictionary,way=1):
    dictionary = words_dictionary
    segment,length = fenci(string,way)
    # print(Counter(segment))
    topic_dic = {}
    detail_dic = {}
    for topic,detail in dictionary.items():
        topic_dic[topic] = 0
        detail_list = detail
        for each in detail_list:
            if (segment.count(each)>=1):
                detail_dic[each]=segment.count(each)
            topic_dic[topic] = topic_dic[topic] + segment.count(each)
    # print(topic_dic)
    # print(detail_dic)
    return topic_dic,detail_dic,length


def judge_topic(topic_dic, detail_dic, length, single_limit=4, all_limit=10):
    if (length<=50):
        single_limit = 3
        all_limit = 5
    topic_value = 0
    for topic,value in topic_dic.items():
        if (value>=single_limit):
            return True
        else:
            topic_value += value
    if(topic_value>=all_limit):
        return True
    else:
        return False


def get_word_list_of_dictionary(dictionary):
    word_list = []
    for v in dictionary.values():
        for each in v:
            word_list.append(each)
    return word_list

def get_category(dictionary):
    dict = sorted(dictionary.items(), key=lambda d: d[1], reverse=True)
    return dict[0][0]

def add_new_topic(string,words_list,limit=5):
    new_key_word = {}
    stop_words = open(r'D:\python\topic_detection\tdt\stop_words.txt', 'r', encoding='utf-8').read().splitlines()
    key_words = getKeyWords(string, 20, 2)
    word_list = fenci(string,2)
    # print(words_list)
    for key_word in key_words:
        # print(key_word)
        if (key_word not in words_list and word_list.count(key_word)>=2 and key_word not in stop_words):
            # print(key_word)
            new_key_word[key_word]=word_list.count(key_word)
    segment,length = fenci(string,way=2)
    segment = [word for word in list(segment) if word not in stop_words]
    words_count = Counter(segment)
    for k,v in words_count.items():
        if (v >= limit and k not in words_list and len(k)>1):
            # print(k)
            new_key_word[k]=v
    return new_key_word

def return_date(ddate):
    ddate = ddate.rstrip('.txt')
    t = time.strptime(ddate, "%Y年%m月%d日")
    ddate = time.strftime('%Y-%m-%d',t)
    return ddate

if __name__ == '__main__':
    day_topic_dict = {}
    words_dictionary = read_from_dict()
    words_list = get_word_list_of_dictionary(words_dictionary)
    f = open(r'D:\python\spider\zaobao\zaobao_news\zaobao_news_1-23.txt','r',encoding='utf-8')
    i = 0
    for line in f:
        # print(i)
        # i += 1
        date = line.split('\001')[0].split(' ')[0]
        date = return_date(date)
        string = line.split('\001')[1]
        # title = line.split('\001')[2]
        t_d,d_d,length = find_topic(string,words_dictionary,2)

        # 标题及类别
        category = get_category(t_d)
        print(category)
        # category_file = open('category\\'+category+'.txt','a')
        # category_file.write(date+title+'\n')

        # 新词
        new_word_file = open('new_word\\new_word_' + date + '.txt', 'a')
        whether = judge_topic(t_d,d_d,length)
        if (whether == False):
            new_key_word = add_new_topic(string,words_list,5)
            new_key_word = sorted(new_key_word.items(), key=lambda d: d[1], reverse=True)
            # print(new_key_word)
            for each in new_key_word:
                new_word_file.write(each[0]+',')
            new_word_file.write('\t\t')
            new_word_file.close()

        # 类别权重
        file = open('data\\'+date+'.txt','a')
        for k,v in t_d.items():
            file.write(str(v)+',')
        file.write('\n')
