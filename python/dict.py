d={
    0:["Ezhil","Thamarai"],
    1:["Ganesan"],
    2:["Vasantha"],
    3:["Praba"]
   } 
d[4]=["kanna"]
print(d)
print(d.items())
print(d.values())
d1={
    4:['Bala'],
    5:['ram'],
    }
d.update(d1)

print(d)
del d[0]
print(d)
