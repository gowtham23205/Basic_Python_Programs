t=tuple(int(i) for i in input().split())
print(t)
n=int(input())
l=list(t)
c=0
for i in range(len(l)):
    if l[i]==n:
         del l[i]
         c+=1
         break
if c==1:
    print(tuple(l))
else:
    print("error")