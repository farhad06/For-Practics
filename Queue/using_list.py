import sys
queue=[]

#Insert element
def enqueue():
    if len(queue)==size:
        print("Queue is full! ")
    else:
        n=int(input("Enter an element "))
        queue.append(n)
        print(f"{n} Inserted in to the Queue")
#display
def show():
    if not queue:
        print("There is no element in Queue")
    else:
        print("Elements presents into the Queue are ")
        for i in queue:
            print(i,end=" ") 
#delete element
def dqueue():
    if not queue:
        print("Queue is empty")
    else:
        ele=queue.pop(0)
        print(f"{ele} is deteled from Queue")                 

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
              