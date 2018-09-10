N,M=map(int,raw_input().split())
if(N>M):
	max1=N
else:
	max1=M
while(1):
	if(max1%N==0 and max1%M==0):
		print(max1)
		break
	else:
		max1=max1+1
	
		
