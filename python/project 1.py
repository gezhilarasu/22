import random
letters=["A","B","C","Q","W","E","R","T","Y","U","I","O","P","S","D","F","G","H","J","K","L","Z","X","C","V","N","M"]
symbols=["!","@","#","$","%","^","&","*","(",")"]
numbers=["1","2","3","4","5","6","7","8","9","0"]
print("PASSWORD GENERATOR")
n_letters=int(input("how many letters do you want in your password\n"))
n_symbols=int(input("how many symbols do you want in your password\n"))
n_numbers=int(input("how many numbers do you want in your password\n"))
password_list=[]
password=" "
for char in range(1,n_letters+1):
    
    password_list.append(random.choice(letters))
for sym in range(1,n_symbols+1):
    password_list.append(random.choice(symbols))
for num in range(1,n_numbers+1):
    password_list.append(random.choice(numbers))
random.shuffle(password_list)
for char in password_list:
    password=password+char
print("The generated password is : ",password)
