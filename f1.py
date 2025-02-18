with open('demo.txt','r') as fb:
    data=fb.read()
    with open('empty.txt','w') as fb1:
        data1=data[::-1]
        fb1.write(data1)
with open('empty.txt','r') as f:
    print(f.read())