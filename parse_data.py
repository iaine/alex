'''
   Script to extract the name and impression time from 
   the JSON and put into a CSV
'''

import sys
import json

fname = sys.argv[1]

f = open(fname.strip() + ".json", 'r')
posts = json.loads(f.read())
f.close()

fh = open(fname.strip() + '.csv', 'w+')
fh.write("Publisher \, Capture")
for post in posts["results"]:
    if "impressionTime" in post:
        write_data = ','.join([post["attributions"][0]["content"], post["impressionTime"]]) 
    else:
        write_data = ','.join([post["attributions"][0]["content"], "No Date"])


    fh.write(write_data.encode('utf-8') + "\n")

fh.close()
