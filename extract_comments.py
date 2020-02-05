import facebook
import itertools
import json
import re
import requests
import pandas as pd
user = '@username'

access_token = 'my_token'
graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'],'posts', limit=100) #The API itself gives 100 posts as limit

Jstr = json.dumps(posts)
JDict = json.loads(Jstr)

data = JDict['data']

#creating an empty dataframe to put the comments and replies from inside the loop
df = pd.DataFrame(columns=['content', 'post_id', 'comment_created', 'comment_id', 'comment_message', 'reply'])

for elements in data:
    post_id = elements['id']
    content = elements['message']
    comment=graph.get_connections(post_id, connection_name='comments')
    for elements in comments:
        commentd = elements['data']
        for obj in commentd:
            comment_created = obj['created_time']
            comment_message = obj['message']
            comment_id = obj['id']
            reply=graph.get_connections(comment_id, connection_name='comments')
            df = df.append({'content': content, 'post_id': post_id, 'comment_created': comment_created, 'comment_id': comment_id, 'comment_message': comment_message, 'reply': reply}, ignore_index=True)
