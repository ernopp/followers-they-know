#!/usr/bin/env python

import argparse

parser = argparse.ArgumentParser(description='\"Followers they know\". x just followed y. What is the list z of people who are followed by x and follow y? They caused x to follow y. Uses https://github.com/bear/python-twitter', prefix_chars='-')

parser.add_argument("--x", type=str, help="the user x")
parser.add_argument("--y", type=str, help="the user y")
parser.add_argument("--consumer_key", help="twitter consumer key")
parser.add_argument("--consumer_secret", help="twitter consumer_secret")
parser.add_argument("--access_token_key", help="twitter access_token_key")
parser.add_argument("--access_token_secret", help="twitter access_token_secret")

args = parser.parse_args()

print 'initilising with' + str(args)

x = args.x
y = args.y

import twitter

api = twitter.Api(consumer_key=args.consumer_key,
                  consumer_secret=args.consumer_secret,
                  access_token_key=args.access_token_key,
                  access_token_secret=args.access_token_secret)

def getFriends(x, maxCalls):
	
	# print 'running getfriends with input ' + x

	followed_by_x = []
	cursor = -1
	calls = 0

	while (cursor != 0 and calls < maxCalls ):
		# print 'getting page ' + str(cursor) + ' with GetFriendsPaged'
		res = api.GetFriendsPaged(screen_name=x,cursor=cursor)
		calls+=1
		cursor = res[0]
		followed_by_x += res[2]
		# print 'res is: ' + str(res[2])
		# print 'next cursor is ' + str(cursor) 

	return followed_by_x

def getFollowers(y, maxCalls):

	# print 'running getFollowers with input ' + y

	follow_y = []
	cursor = -1
	calls = 0
	
	while (cursor != 0 and calls < maxCalls ):
		# print 'getting page ' + str(cursor) + ' with getfollowerspaged'
		res = api.GetFollowersPaged(screen_name=y,cursor=cursor)
		calls+=1
		cursor = res[0]
		follow_y += res[2]
		# print 'res is: ' + str(res[2])
		# print 'next cursor is ' + str(cursor)

	return follow_y

def getIntersectionOfUsersLists(a,b):
  c = []
  for u in a:
    for v in b:
      if u.id == v.id:
        c.insert(len(c),u)
  return c

# list of people that x follows
print 'getting list of followed by x, with x= ' +x
followed_by_x = getFriends(x, 5)

# list of people who follow y
print 'getting list of follow y, with y= ' +y
follow_y = getFollowers(y, 5)

# print 'followed by x, there are: ' + str(len(followed_by_x)) + ' people in the list'
# print followed_by_x

# print 'follow y' + str(len(follow_y)) + ' people in the list'
# print follow_y

print 'getting list of followers of y that x knows (because he/she follows them)'
z = getIntersectionOfUsersLists(followed_by_x,follow_y)
print z
