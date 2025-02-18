t=tuple(int(i) for i in input().split())
n=int(input())
if len(t)>n:
    print(t[n])
else:
    print("error")