import jieba
import jieba.analyse
import re
import sys
import string

example1_txt = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/example1.txt', 'r', encoding = 'gbk')
example2_txt = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/example2.txt', 'r', encoding = 'gbk')
result1_txt = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/result1.txt', 'a+', encoding = 'gbk')
result2_txt = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/result2.txt', 'a+', encoding = 'gbk')
keywords1 = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/keywords1.txt', 'w', encoding = 'gbk')
keywords2 = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/keywords2.txt', 'w', encoding = 'gbk')
result1_txt_1 = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/result1.txt', 'r', encoding = 'gbk')
result2_txt_2 = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/result2.txt', 'r', encoding = 'gbk')
stopwords = open('F:/PyCharm/PyCharm Community Edition 2019.3.3/untitled2/stopwords.txt', 'r', encoding = 'utf-8')

#停用词文件
swlists=[]
for word in stopwords:
        swlists.append(word.strip())

#对例子1、例子2进行分词处理和去停用词处理
for line in example1_txt:
        info = ''
        text = jieba.cut(line.strip(), cut_all = False)
        for word in text:
                if word not in swlists:
                        info += word
                        info += "/ "
        print(info, file = result1_txt)

with open('result1.txt', 'r', encoding = 'gbk') as fr, open('result1_new.txt', 'w', encoding = 'gbk') as fw:
        for text in fr.readlines():
                if text.split():
                        fw.write(text)

for line in example2_txt:
        info = ''
        text = jieba.cut(line.strip(), cut_all = False)
        for word in text:
                if word not in swlists:
                        info += word
                        info += "/ "
        print(info, file = result2_txt)

with open('result2.txt', 'r', encoding = 'gbk') as fr, open('result2_new.txt', 'w', encoding = 'gbk') as fw:
        for text in fr.readlines():
                if text.split():
                        fw.write(text)

#对例子1、例子2进行关键词选取
temp = result1_txt_1.readlines()
keywords = jieba.analyse.extract_tags(str(temp), topK = 10, withWeight = False, allowPOS = ())
print(keywords, file = keywords1)

temp = result2_txt_2.readlines()
keywords = jieba.analyse.extract_tags(str(temp), topK = 10, withWeight = False, allowPOS = ())
print(keywords, file = keywords2)










