'''
   Script to extract the name, impression time and links from 
   the JSON and put into a CSV
'''

import sys
import json

from collections import Counter

fname = sys.argv[1]

counter = Counter()

f = open(fname.strip() + ".json", 'r')
posts = json.loads(f.read())
f.close()

fh = open(fname.strip() + 'links.csv', 'w+')
fh.write("Publisher \; Capture\; Links")
for post in posts["results"]:
    links = []
    imp_tme = ""
    link = ""

    if "impressionTime" in post:
        imp_time = post["impressionTime"]

    if "externalLinks" in post:
        links = [external['link'] for external in post["externalLinks"]]

    if len(links) > 0:
        link = ','.join(links)
        for l in links:
            counter[l] += 1

    write_data = ';'.join([post["attributions"][0]["content"], imp_time, link])
    fh.write(write_data.encode('utf-8') + "\n")

fh.close()

print counter.most_common(5)
