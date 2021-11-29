f1=open("demo1.txt","r")
f2=open("demo2.txt","w")
for i in f1:
    f2.write(i)
f1.close()
f2.close()