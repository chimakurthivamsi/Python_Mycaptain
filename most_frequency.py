s=input("Please enter a String: ")
s=s.lower()
l=list(s)
freq={}
freq1={}
for i in l:
    if i in freq:
        freq[i]+=1
    else:
        freq[i]=1
freq1=list(sorted(freq.items(),key=lambda x:x[1],reverse=True))
for i in freq1:
    print(i[0],"=",end=" ")
    print("%02d"%i[1])
