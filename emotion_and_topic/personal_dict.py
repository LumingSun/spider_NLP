import re
input_file = 'emotion.txt'
output_file = 'emotion.pickle'
dict = {}
file = open(input_file, 'r', encoding='gbk')
f = file.readlines()
file.close()
cnt = 2
emotion_list = []
for line in f:
    line = line.strip()
    data = [x for x in re.split(";|\t", line) if x]
    l = int(len(data)/2)
    for i in range(0, l):
        emotion_list.append(data[i])
set = set(emotion_list)
# print(set)
emotion_dict = {}
for item in set:
    emotion_dict.update({item: emotion_list.count(item)})
# print(emotion_dict)
f = open(r'personal_dictionary.txt','w',encoding='utf-8')
for key,value in emotion_dict.items():
    line = key+' '+str(value)+'\n'
    f.write(line)
    print(line)
f.close()