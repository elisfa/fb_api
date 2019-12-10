import facebook
import itertools
import json
import re
import requests
import pandas as pd
user = 'username'

access_token = 'my_token'
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'],'posts', limit=100)

Jstr = json.dumps(posts)
JDict = json.loads(Jstr)

data = JDict['data']

comments = []
posts_ids=[]
message = []
for elements in data:
    post_id = elements['id']
    posts_ids.append(post_id)
    comment=graph.get_connections(post_id, connection_name='comments')
    comments.append(comment)

for i in comments:
    data = i['data']
    with open('facebook_comments.txt', 'a+') as f:
        for each in data:
            f.write("%s\n" % each)
