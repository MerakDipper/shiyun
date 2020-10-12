#!/usr/local/bin/python2
#-*- coding: utf-8 -*-


# Please note this only works with python2
import argparse
import jieba
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont

parser = argparse.ArgumentParser()
parser.add_argument('--file', dest='poet_text_path',
                    required=True,
                    help='the poet text you would like to analyze')

args = parser.parse_args()

#stopwords is NOT working properly for now.
stopwords = set()
stopwords.add("故人")
stopwords.add("不可")

text_from_file_with_apath = open(args.poet_text_path).read()
wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

back_img = np.array(Image.open("./cloud5.png"))
my_wordcloud = WordCloud(font_path="./ZiYueSongKeBenJianTi-2.ttf",
                           background_color="white",
                           max_words=100,
                           max_font_size=200,
                           width=1280,
                           stopwords=stopwords,
                           mask=back_img,
                           height=800).generate(wl_space_split)

plt.imshow(my_wordcloud,interpolation='bilinear')
plt.axis("off")
plt.show()
