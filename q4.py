num=int(input())
r=int(num/2+1)
def row(i):
	l=""
	n=i	
	while i-1!=0:
		l+=str(i)
		i-=1
	print((" "*(r-n))+l+str(i)+l[::-1])
	if n<r:	
		row(n+1)
		print((" "*(r-n))+l+str(i)+l[::-1])
row(1)
		

