import urllib

testfile = urllib.URLopener()
testfile.retrieve("https://www.facebook.com/usask/", "usasklikes.txt")

f = open("D:\python\usasklikes.txt", "r")
s = f.readlines()
f.close()
for i, line in enumerate(s):
    if 'meta name="description"' in line:
        print line[line.find('meta name="description" content="'):line.find('&#xb7;')]

