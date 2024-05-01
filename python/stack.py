
stack=[]
def push():
    element=input("enter the element")
    stack.append(element)
    print(stack)
def pop():
    if not stack:
        print("stack is empty")
    else:
        pop=stack.pop()
        print("The poped element is",pop)
        print(stack)
while True:
    choice=int(input("Enter the values 1.)pop 2.)push 3.)quit: "))    
    if(choice==1):
        push()
    elif(choice==2):
        pop()
    else:
        print("Enter the correct number")
    
    