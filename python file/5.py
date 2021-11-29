f1=open("demo1.txt","r")
f2=open("demo2.txt","r")
i=0
for j in f1:
    i+=1
for k in f2:
    if j==k:
        print("same")
        break
    else:
        print("not same")
        break
f1.close()
f2.close()