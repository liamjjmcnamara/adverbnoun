#!/usr/bin/env python

import sys
import json
import random

def read_json(wordtype):
    with open(wordtype+'.json') as data_file:
        words = json.load(data_file)
        return words
    return None

nouns      = read_json("nouns")
verbs      = read_json("verbs")
adjectives = read_json("adjectives")

def single_ver(ver1):
    random.seed(ver1)
    return random.choice(nouns)

def double_ver(ver1, ver2):
    random.seed(ver1+ver2)
    return random.choice(adjectives)+"-"+random.choice(nouns)

def triple_ver(ver1, ver2, ver3):
    random.seed(ver1+ver2+ver3)
    return random.choice(adjectives)+"-"+ random.choice(verbs)+"-"+random.choice(nouns)

if len(sys.argv)==2:
    ver1 = sys.argv[1]
    print single_ver(ver1)
elif len(sys.argv)==3:
    ver1 = sys.argv[1]
    ver2 = sys.argv[2]
    print double_ver(ver1,ver2)
elif len(sys.argv)==4:
    ver1 = sys.argv[1]
    ver2 = sys.argv[2]
    ver3 = sys.argv[3]
    print triple_ver(ver1,ver2,ver3)
else:
    raise ValueError("Max 3 args!")
