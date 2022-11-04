from queue import LifoQueue
import sys
#create a empty stack
def create_stack():
    stack=LifoQueue(maxsize=5)
    return stack
'''#ckecking for empty or not
def Isempty(stack):
    return len(stack)==0
    '''
#push
def push(stack):
    if (stack.full()):
        print("Stack is full: ")
    else:    
        n=int(input("Enter an element "))
        stack.put(n)
        print(f"{n} pushed in to the stack")
#display
def show(stack):
    print("Total size of stack is ",stack.qsize())
#pop
def pop(stack):
    if (stack.empty()):
        print("Stack is empty ")
    else:
        #ele=stack.pop()
        print(stack.get()," is poped out from stack")                 
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
        print("You choose wrong choice")                    