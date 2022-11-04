from collections import deque
import sys
queue=deque()

#Insert element
def enqueue():
    if len(queue)==size:
        print("Queue is full! ")
    else:
        n=int(input("Enter an element to be Inserted: "))
        print("1.Insert to the Right End || 2.Insert to the Left End")
        ch=input("Enter Your Choice ")
        if ch=='1':
            queue.append(n)
        elif ch=='2':
            queue.appendleft(n)
        else:
            print("Wrong Choice!!")        
        print(f"{n} Inserted in to the Queue")
#Insert element
def dqueue():
    if not queue:
        print("Queue is Empty! ")
    else:
        print("1.Delete From Right End || 2.Delete From Left End")
        ch=input("Enter Your Choice ")
        if ch=='1':
            ele=queue.pop()
        elif ch=='2':
            ele=queue.popleft()
        else:
            print("Wrong Choice!!")        
        print(f"{ele} Deleted from the Queue")
#display
def show():
    if not queue:
        print("There is no element in Queue")
    else:
        print("Elements presents into the Queue are ")
        for i in queue:
            print(i,end=" ") 

size=int(input("Enter the size of Queue: "))

while True:
    print("\n1.INSERT || 2.SHOW || 3.DELETE || 4.EXIT ")
    choice=input("Enter your choice: ")
    if choice=='1':
        enqueue()
    elif choice=='2':
       show()
    elif choice=='3':
        dqueue()   
    elif choice=='4':
        sys.exit("You exit from program! ") 
    else:
        print("You choose wrong choice ")      
                                          
