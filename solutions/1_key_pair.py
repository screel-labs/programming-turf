def check(s,e):
    if arr[s]+arr[e] == x and s!=e:
        print("Yes")
    elif arr[s]+arr[e] < x and s<e:
        s+=1
        check(s,e) 
    elif arr[s] + arr[e] > x and e>s:
        e-=1
        check(s,e)
    else:
        print("No")


t = int(input())
for i in range(t):
    n,x = [int(i) for i in input().split()]
    input_arr = input()
    arr = list(map(int,input_arr.split(" ")[:n]))
    arr.sort()
    for i in arr:
        if i>=x:
            k = arr.index(i)-1
        else:
            k = len(arr) - 1
    s = 0
    e = k
    check(s,e)


