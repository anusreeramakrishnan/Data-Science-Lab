f1=open("demo1.txt","r")
lines=f1.readlines()
print(lines)
f1.close()
del lines[1]
f1=open("demo1.txt","w+")
for line in lines:
    f1.write(line)
print(lines)
f1.close()