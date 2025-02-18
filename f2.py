with open('count.txt','r') as fo:
    lchar,lline,lword=0,1,1
    for i in fo.read():
        lchar+=len(i)
        if i==' ' or i=='\n':
            lword+=1
        if i=='\n':
            lline+=1
    print('lines : ',lline,'\nwords : ',lword,'\ncharactrs : ',lchar)