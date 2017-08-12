import pickle, pprint, twitter, datetime

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)

def getKey(item):
    return item.statuses_count

def creationStringToDate(string):
	#format is "Sat May 12 12:03:26 +0000 2012", using https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior
	s = string.replace("+0000 ", "")
	s = datetime.datetime.strptime(s, "%a %b %d %H:%M:%S %Y")
	return s

data1.sort(key=getKey, reverse=True)

for d in data1[:100]:
	dayssincecreation = (datetime.datetime.now() - creationStringToDate(d.created_at)).days
	print (d.name, d.screen_name, d.created_at, d.statuses_count, dayssincecreation, float(d.statuses_count / dayssincecreation))

#pprint.pprint(data1)
# print(data1[0])

# pprint.pprint(data1[0])
# pprint.pprint(data1[0].name)


pkl_file.close()


