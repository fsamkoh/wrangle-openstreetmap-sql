#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python


import csv, sqlite3

def number_of_nodes():
    result = cur.execute('SELECT COUNT(*) FROM nodes')
    return result.fetchone()[0]

def number_of_ways():
    result = cur.execute('SELECT COUNT(*) FROM ways')
    return result.fetchone()[0]

def number_of_Unique_users():
    result = cur.execute('SELECT COUNT(distinct(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways)')
    return result.fetchone()[0]

def top_contributing_users():
    users = []
    for row in cur.execute('SELECT e.user, COUNT(*) as num             FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e             GROUP BY e.user             ORDER BY num DESC             LIMIT 10'):
        users.append(row)
    return users


def popular_cities():
    cities = []
    for row in cur.execute("""SELECT tags.value, COUNT(*) as count
                        FROM (SELECT * FROM nodes_tags
                          UNION ALL 
                          SELECT * FROM ways_tags) tags 
                        WHERE tags.key = 'city' 
                        GROUP BY tags.value 
                        ORDER By count DESC
                        LIMIT 10"""):
        cities.append(row)
    return cities

def Biggest_religion():
    for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num FROM nodes_tags                             JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="place_of_worship") i                             ON nodes_tags.id=i.id                             WHERE nodes_tags.key="religion"                             GROUP BY nodes_tags.value                             ORDER BY num DESC                            LIMIT 1'):
        return row

def popular_amenities():
    amenities = []
    for row in cur.execute('SELECT value, COUNT(*) as num                             FROM nodes_tags                             WHERE key="amenity"                             GROUP BY value                             ORDER BY num DESC                             LIMIT 10'):
        amenities.append(row)
    return amenities

def popular_cuisines():
    cuisines = []
    for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num             FROM nodes_tags                 JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="restaurant") i                 ON nodes_tags.id=i.id             WHERE nodes_tags.key="cuisine"             GROUP BY nodes_tags.value             ORDER BY num DESC            LIMIT 10'):
        cuisines.append(row)
    return cuisines    

    
def popular_cities():
    cities = []
    for row in cur.execute("""SELECT tags.value, COUNT(*) as count
                        FROM (SELECT * FROM nodes_tags
                          UNION ALL 
                          SELECT * FROM ways_tags) tags 
                        WHERE tags.key = 'city' 
                        GROUP BY tags.value 
                        ORDER By count DESC
                        LIMIT 10"""):
        cities.append(row)
    return cities    

    
def number_of_users_contributing_once():
    result = cur.execute('SELECT COUNT(*)             FROM                 (SELECT e.user, COUNT(*) as num                  FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e                  GROUP BY e.user                  HAVING num=1) u')
    return result.fetchone()[0]
                
if __name__ == '__main__':

    con = sqlite3.connect("SilverSpring.db") 
    cur = con.cursor()
    print "Number of nodes: " , number_of_nodes()
    print "Number of ways: " , number_of_ways()
    print "Number of unique users: " , number_of_Unique_users()
    print "Top Contributing users: " , top_contributing_users()
    print "Biggest religion: " , Biggest_religion()
    print "popular amenities: " , popular_amenities()
    print "Popular cuisines: " , popular_cuisines()
    print "popular Cities: " , popular_cities()
    print "Number of users contributing once: " , number_of_users_contributing_once() 

