#program to check whether there exist atlest one pair(a,b) such the sum of a+b=given sum and a,b belongs to given array,
#time and space complexity is O(n)

# Binary Search implementation
# Returns index of x in arr if present, else -1
def binarySearch (arr, l, r, x):
 
    # Check base case
    if r >l:
 
        mid = int(l + (r - l)/2)
        print(l,mid,r,arr)
        if arr[mid] == x:
            return mid
         
        elif arr[mid] > x:
            return binarySearch(arr, l, mid-1, x)
 
        else:
            return binarySearch(arr, mid+1, r, x)
 
    else:
        # Element is not present in the array
        return -1

t=int(input())
while(t):
	n,x=input().split()
	n,x=int(n),int(x)
	a=input().split()
	a=[int(ele) for ele in a]
	a.sort()
	
	i=0
	j=len(a)
	
	#run to each element in array until you find a pair element, in worst case it is O(n),since cost of binary search is O(logn) overall cost is O(nlogn) 
	flag=0
	while i<j-1:
		ele=a[i]
		pair_ele=x-a[i]
		#print(a[i+1:j],j-i-1)
		pair_ele_pos=binarySearch(a[i+1:j],0,j-i-1,pair_ele)
		if pair_ele_pos>=0:
			#print(ele,pair_ele)
			#pair element exist
			flag=1;
			break;
		i+=1	
	
	if(flag):
		print('Yes')
	else:
		print('No')
	t-=1