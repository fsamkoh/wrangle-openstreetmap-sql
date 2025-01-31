#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python


import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osm_file = open("SilverSpringMap.xml", "r")

# Regular expression to recognise street type
street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE) 

street_types = defaultdict(int)

def audit_street_type(street_types, street_name):
    # Build defaultdict of unexpected street types
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        street_types[street_type] += 1

def print_sorted_dict(d):
    keys = d.keys()
    keys = sorted(keys, key=lambda s: s.lower())
    for k in keys:
        v = d[k]
        print("%s: %d" % (k, v))

def is_street_name(elem):# Check if it is a street name
    return (elem.tag == "tag") and (elem.tag == "tag") and (elem.attrib['k'] == "addr:street")

def audit():
    for event, elem in ET.iterparse(osm_file):
        if is_street_name(elem):
            audit_street_type(street_types, elem.attrib['v'])    
    print_sorted_dict(street_types)    

if __name__ == '__main__':
    audit()

