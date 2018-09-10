str=raw_input()
x=[]
for i in str:
	if(i.isdigit()):
		x.append(i)
print "".join(x)
