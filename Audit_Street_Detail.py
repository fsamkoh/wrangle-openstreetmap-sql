#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# create a dictionary of the street types and street names

import pprint
import xml.etree.cElementTree as ET
from collections import defaultdict
import re
# initial version of expected street names
expected = ["Street", "Avenue", "Boulevard", "Drive", "Court", "Place", "Square", "Lane", "Road", "Trail", "Parkway"]

osm_file="SilverSpringMap.xml"

street_type_re = re.compile(r'\S+\.?$', re.IGNORECASE)
street_types = defaultdict(int)

def audit_street_type(street_types, street_name):
    # add unexpected street name to a list
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected:
            street_types[street_type].add(street_name)
            
def is_street_name(elem):
    # determine whether a element is a street name
    return (elem.attrib['k'] == "addr:street")

def audit_street(osmfile):
    # iter through all street name tag under node or way and audit the street name value
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])
    return street_types

st_types = audit_street(osm_file)
# print out the value these unexpected street name keys
pprint.pprint(dict(st_types)['#101'])
pprint.pprint(dict(st_types)['#404'])
pprint.pprint(dict(st_types)['20740'])
pprint.pprint(dict(st_types)['20903'])
pprint.pprint(dict(st_types)['W'])
pprint.pprint(dict(st_types)['Row'])

