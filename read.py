import pickle, pprint

pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(users)

pkl_file.close()


