#-*- coding: utf-8 -*-
import glob
import json

# DATASET comes from https://github.com/chinese-poetry/chinese-poetry
# Please clone it to your home directory like: ~/chinese-poetry
# 词 is located under ~/chinese-poetry/ci
# 诗 is located under ~/chinese-poetry/json
# poet name could be in 繁體 or 简体 so its better to search for both

poet_name = ["王维", "王維"]
dynasty = "tang" # choice from ["tang", "song"]
shiciji_file_name = "wangwei"
shiciji = []
for p_name in poet_name:
    files = glob.glob("/Users/zhangxuan/chinese-poetry/json/poet.{}*.json".format(dynasty))
    files1 = glob.glob("/Users/zhangxuan/chinese-poetry/ci/*.json")
    files.extend(files1)
    fo = open(shiciji_file_name, 'w')
    for file in files:
        with open(file) as fi:
            fi_json = json.load(fi)
            for poem in fi_json:
                if 'author' in poem and poem["author"] == p_name:
                    shiciji.extend(poem["paragraphs"])


print(len(shiciji))
for item in shiciji:
    fo.write(item)
    fo.write("\n")
