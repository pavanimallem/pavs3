def do_stuff(raw_input):
	n,op,m=[x for x in raw_input.split(" ")]
	if op=='/':
		print(int(n)/int(m))
	else:
		print(int(n)%int(m))
 
 
 
while true:
	try:
		value=raw_input()
		do_stuff(value.rstrip())
	except(EOFError):
		break
