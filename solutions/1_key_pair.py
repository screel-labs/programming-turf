t=int(input())
while(t):
	n,x=input().split()
	n,x=int(n),int(x)
	a=input().split()
	a=[int(ele) for ele in a]
	flag=0
	for i in range(len(a)-1):
		if (x-a[i]) in a[i+1:]:
			flag=1
			break
	if(flag):
		print('Yes')
	else:
		print('No')
	t-=1