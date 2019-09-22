#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# Process the map file with iterative parsing and 
# find out how many times each tag appears
# in the file by using count_tags function

import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict


def count_tags(filename):
    tags = {}
    for ev,elem in ET.iterparse(filename):
        tag = elem.tag
        if tag not in tags.keys():
            tags[tag] = 1
        else:
            tags[tag]+=1
    return tags
       
def test():

    tags = count_tags('SilverSpringMap.xml')
    pprint.pprint(tags)
    

if __name__ == "__main__":
    test()

