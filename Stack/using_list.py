import sys
#create a empty stack
def create_stack():
    stack=list()
    return stack
#ckecking for empty or not
def Isempty(stack):
    return len(stack)==0
#push
def push(stack):
    n=int(input("Enter an element "))
    stack.append(n)
    print(f"{n} pushed in to the stack")
#display
def show(stack):
    if(Isempty(stack)):
        print("There is no element in stack")
    else:
        print("Elements presents into the stack are ")
        for i in stack:
            print(i) 
#pop
def pop(stack):
    if (Isempty(stack)):
        print("Stack is empty")
    else:
        ele=stack.pop()
        print(f"{ele} is poped out from stack")                 

stack=create_stack()

while True:
    print("1.PUSH || 2.SHOW || 3.POP || 4.EXIT ")
    choice=input("Enter your choice: ")
    if choice=='1':
        push(stack)
    elif choice=='2':
       show(stack)
    elif choice=='3':
        pop(stack)   
    elif choice=='4':
        sys.exit("You exit from program! ") 
    else:
        print("You choose wrong choice ")      
              