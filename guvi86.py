str=raw_input()
l=len(str)
c=0
for i in range(0,l):
	for j in range(i+1,l):
	    if(str[i]==str[j]):
		c=c+1
		break
if(c==0):
	print("Yes")
else:
	print("No")
