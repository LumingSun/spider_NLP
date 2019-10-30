import re
import pickle
import jieba
import xlwt

jieba.load_userdict("personal_dictionary.txt")
# workbook = xlwt.Workbook(encoding = 'ascii')
# worksheet = workbook.add_sheet('My Worksheet')
# worksheet.write(0, 0, label = 'Row 0, Column 0 Value')
# workbook.save('Excel_Workbook.xls')

def get_topic_list():
    input_file = 'topic.txt'
    output_file = 'topic_list.txt'
    topic_list = []
    file = open(input_file,'r',encoding='gbk')
    f = file.readlines()
    for line in f:
        line = line.strip().split(';')
        for word in line:
            if word != 'NULL' and word != '':
                topic_list.append(word)
    file.close()
    topic_list = list(set(topic_list))
    print(topic_list)
    o = open(output_file,'w',encoding='gbk')
    o.write(str(topic_list))
    o.close()
# get_topic_list()

def get_emotion():
    input_file = 'emotion.txt'
    output_file = 'emotion.pickle'
    dict = {}
    file = open(input_file, 'r', encoding='gbk')
    f = file.readlines()
    file.close()
    cnt = 2
    for line in f:
        line = line.strip()
        data = [x for x in re.split(";|\t", line) if x]
        l = int(len(data)/2)
        for i in range(0,l):
            if dict.__contains__(data[i]) and dict[data[i]]!=data[l+i]:
                pass
                # print(cnt)
                # print(data[i],data[i+l])
            else:
                dict[data[i]] = data[l+i]
        cnt = cnt+1
    # print(dict)
    # o = open(output_file,'wb')
    # pickle.dump(dict,o)
    # o.close()
    return dict

# dict = get_emotion()
# print(dict)

def data_fenci():
    input_file = r'data.txt'
    input_file = r'data_train.txt'
    out_file = r'data_topic.txt'
    f = open(input_file,'r',encoding='utf-8')
    file = f.readlines()
    f.close()
    topic_file = r'topic.txt'
    f = open(topic_file,'r',encoding='gbk')
    topics = f.readlines()
    f.close()
    topic_list = []
    for line in topics:
        line = line.strip().split(';')
        for each in line:
            topic_list.append(each)
    while '' in topic_list:
        topic_list.remove('')
    # print(topic_list)
    for line in file:
        potional_topics = jieba.cut(line, cut_all=False)
        potional_topics = list(potional_topics)
        topics = [word for word in potional_topics if word in topic_list]
        print(topics)

def emotion_fenci():
    data_input_file = r'data.txt'
    # data_input_file = r'data_train.txt'
    f = open(data_input_file, 'r', encoding='utf-8')
    file = f.readlines()
    f.close()
    emotion_list = get_emotion()
    workbook = xlwt.Workbook(encoding='ascii')
    worksheet = workbook.add_sheet('My Worksheet')
    i = 0
    for line in file:
        result = ''
        potional_emotions = jieba.cut(line, cut_all=False)
        potional_emotions = list(potional_emotions)
        emotions = [word for word in potional_emotions if word in emotion_list]
        # print(emotions)
        for each_word in emotions:
            result = result+each_word+';'
        worksheet.write(i, 4, label=result)
        i = i+1

        # print(potional_emotions)
    workbook.save('emotion_result.xls')

emotion_fenci()

