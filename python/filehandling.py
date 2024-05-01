

f=open("fruits.txt","w")
f.write("hello\n")
f.close()

f=open("fruits.txt","a")
f.write("hi")

f.close()
f=open("fruits.txt")
content=f.read()
print(content)




