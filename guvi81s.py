n1,m1=map(int,raw_input().split())
k1=n1-m1
if n1 and m1<2**32:
	print abs(k1)
else:
	print (k1)
