import datetime
string = "Sat May 12 12:03:26 +0000 2012"
string = string.replace("+0000", "")
d = datetime.datetime.strptime(string, "%a %B %d %H:%M:%S %Y")
#https://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior

print(d)