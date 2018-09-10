str=raw_input()
l=len(str)
m=[]
for i in range(0,l):
	if(i%2==0):
		m.append(str[i])
m.append(" ")		
for j in range(0,l):
	if(j%2!=0):
		m.append(str[j])

print "".join(m)
