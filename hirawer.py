import csv
import re
import MeCab
import numpy as np
import random
class Paprika(object):
    def __init__(self, path):
        self.__mecab = MeCab.Tagger("-d /usr/local/lib/mecab/dic/mecab-ipadic-neologd")
        with open(path, newline='') as csvfile:
            data = csv.reader(csvfile)
            self.__sents = np.array([row for row in data])

    def random_sent(self):
        return self.__sents[random.randint(0,len(self.__sents))][0]
    def get_newtext(self,text):
        sents = []
        for s in self.__mecab.parse(text).split('\n'):
            j = re.split('\t|\,', s)
            if len(j) > 2 :
                if re.compile('^名詞').match(j[1]):
                    j[0] = self.random_sent()
                sents.append(j[0])
        return ''.join(sents)

p = Paprika('/Users/rickshinmi/Downloads/randomtanka/tokitakun/susumuhirasawanoun.csv')
text = "仕組みとしては平沢進の歌詞とパプリカの一部シーンに出てきたセリフを形態素解析っていう品詞ごとに分解して分析する手法を使って名詞だけピックアップして提示された文章の名詞部分をランダムに置き換えてる"
texts = p.get_newtext(text)
print(texts)