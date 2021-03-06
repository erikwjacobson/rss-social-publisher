import json
import feedparser
import requests
import numpy as np
import pandas as pd
from BlogPost import BlogPost

def main():
    # Link to RSS Feed
    RSS = 'https://www.erikwjacobson.com/blog?format=rss'
    
    # Load Credentials
    f = open('credentials.json', 'r')
    creds = json.loads(f.read())
    f.close()
    
    # For each post
    posts = feedparser.parse(RSS)
    for post in posts['entries']:
        post = BlogPost(post) # Instantiate
        
        # If the post has not been posted to medium yet
        if(not post.is_posted(to='medium')):
            # Post to medium
            success = postToMedium(creds, post)
            if(success):
                post.medium = True
                post.log() # Log the post
                print('Successfully posted "{}" to Medium.'.format(post.title))
            else:
                print('Something went wrong with the request!')
        else: 
            print('All posts are already on Medium!')
    print('Done')

## Post to medium
def postToMedium(creds, post):
    id = creds['medium_author_id']
    url = "https://api.medium.com/v1/users/{}/posts".format(id)
    data = ({
        'title': post.title,
        'contentFormat': "html",
        "publishStatus": "draft", # Change to 'public', or leave out if you want to automatically publish live articles
        "content": post.content
    })
    headers = ({
        'Authorization': 'Bearer {}'.format(creds['medium_token']),
        'Content-Type': 'application/json'
    })
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.json())
    posted = r.status_code == 201 # OK Status
    return posted

main()