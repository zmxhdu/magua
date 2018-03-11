# coding = utf-8

import os


path = 'E:/git/magua/first-day/files'
files = os.listdir(path)

for f in files:
    if (not f.endswith('.gif')) and ('project30' in f or 'commercial' in f):
        print('Look ,I found this : '+f)
