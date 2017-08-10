#!/usr/bin/env python

import argparse
import json

with open('keys.json') as json_data_file:
    data = json.load(json_data_file)
print(data)

print "cosumer secret is" + data['consumer_secret']

import twitter

api = twitter.Api(consumer_key=data['consumer_key'],
                  consumer_secret=data['consumer_secret'],
                  access_token_key=data['access_token_key'],
                  access_token_secret=data['access_token_secret'])

import pickle

users = api.GetFriends()

output = open('data.pkl', 'wb')
pickle.dump(users, output)

output.close()

#user= api.GetUser(screen_name="gabropp")


#"created_at": "Sat Apr 11 20:51:35 +0000 2009"
#statuses_count

#print([u.name for u in users])
