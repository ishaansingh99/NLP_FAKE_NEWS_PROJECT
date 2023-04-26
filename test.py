# Import packages
import os, json
import numpy as np
from nltk.stem.snowball import EnglishStemmer
import matplotlib.pyplot as plt

skip = True
title = []
text = []
url = []
labels = []
foo = 0

print(len(os.listdir("fakenewsnet_dataset/politifact/fake")) + len(os.listdir("fakenewsnet_dataset/politifact/real")))