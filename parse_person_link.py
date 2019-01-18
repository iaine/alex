'''
   Script to extract the name, impression time and links from 
   the JSON and put into a CSV
'''

import sys
import json

fname = sys.argv[1]

link_name = sys.argv[2]


f = open(fname.strip() + ".json", 'r')
posts = json.loads(f.read())
f.close()

fh = open(fname.strip() + 'person.csv', 'w+')
fh.write("Publisher, Capture, UserId\n")
for post in posts["results"]:
    imp_time = "No Date"

    if "externalLinks" in post:
        for l in post["externalLinks"]:
            if link_name == l['link']:
                if "impressionTime" in post:
                    imp_time = post["impressionTime"]
                userid = str(post["userId"])
                write_data = ','.join([post["attributions"][0]["content"], imp_time, userid])
                fh.write(write_data.encode('utf-8') + "\n")

fh.close()
