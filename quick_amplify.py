import pandas as pd

orig_data = pd.read_json('opendata-e18.array.json')

comments = orig_data['comments'].sum()
likes = orig_data['rtotal'].sum()
shares = orig_data['shares'].sum()

for i in orig_data['profileAlign'].unique():
    g = orig_data[orig_data['profileAlign'].str.contains(i)]
    print("Amplification bubbles top data for " + i)
    print("Emotions ") 
    print(float(g['rtotal'].sum()) / float(likes))
    print("Shares ") 
    print(float(g['shares'].sum()) / float(shares))
    print("Comments ") 
    print(float(g['comments'].sum()) / float(comments))
