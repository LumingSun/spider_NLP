import os
import numpy as np
import datetime
import time


def get_matrix():
    files = os.listdir(r'D:\python\topic_detection\tdt\data')
    matrix = [0]*19
    date_list = []
    matrix = np.array(matrix)
    for each in files:
        # print(each)
        path = 'D:\python\\topic_detection\\tdt\data\\'+ each
        date_list.append(each.strip('.txt'))
        f = open(path, 'r').readlines()
        new_list = [0]*19
        cnt = 0
        for each in f:
            attr =[]
            cnt +=1
            for i in range(len(each.split(',')[:-1])):
                attr.append(int(each.split(',')[i]))
            for i in range(0, len(each.split(',')[:-1])):
                if (attr[i]>0):
                    attr[i] = 1
                new_list[i] = new_list[i] + attr[i]
        new_list = np.array(new_list)
        if (cnt<=2):
            new_list = new_list
        else:
            new_list = new_list/cnt*100
        # print(cnt)
        print(new_list)
        matrix = np.vstack((matrix,new_list))
    matrix = np.delete(matrix,0,axis=0)
    # print(matrix)
    # print(matrix.T)
    return date_list,matrix.T

date_list,matrix = get_matrix()


