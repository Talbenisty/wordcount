#print "hello world"

f = open('danielle.txt', 'r')
#print f

countmap = {}

for line in f:
	for word in line.split():
		#print word 
		if countmap.get(word)!= None :
			countmap[word]+=1
		else : 
			countmap[word]=1
#print countmap
print "000"
print "000"
print "000"
countlist = countmap. items() 
countlist.sort(key=lambda tup: tup[1]) 
#countlist.reverse()
print countlist

for word, count in countlist: 
	print "{}:{}".format(count,word)
	print

