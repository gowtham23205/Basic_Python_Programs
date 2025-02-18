t=(1,2,3,4,5)
index=int(input())
newele=int(input())
l=list(t)
if len(t)>index:
    l[index]=newele
    print(tuple(l))
else:
    print("error")