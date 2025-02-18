n=input()
f="FLAG"
e="ESC"
if(n.find("ESC")):
    k=n.replace(e,"ESC ESC")
k=n.replace(f,"ESC FLAG")
print(k)