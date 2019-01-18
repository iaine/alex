import urllib2
import sys

group_name = sys.argv[1]

#static endpoint from https://github.com/tracking-exposed/facebook/wiki/Researchers-API-and-how-to-download-the-data
api_end = 'https://facebook.tracking.exposed/api/v1/research/data/l:'

if not group_name:
    print("get data needs a group name")
    sys.exit(1)

print("Getting data from\n" + api_end + group_name)

data = urllib2.urlopen(api_end + group_name).read()
print(data)

fname = group_name + '.json'

f = open(fname, 'w+')
f.write(data)
f.close()
