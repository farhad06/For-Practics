from queue import Queue
import sys
queue=Queue(maxsize=5)

#Insert element
def enqueue():
    if queue.full():
        print("Queue is full! ")
    else:
        n=int(input("Enter an element "))
        queue.put(n)
        print(f"{n} Inserted in to the Queue")
#display
def show():
    print("The size of Queue is: ",queue.qsize())
#delete
def dqueue():
    if queue.empty():
        print("Queue is empty")
    else:
        #ele=queue.pop(0)
        print(queue.get()," is deteled from Queue")                 


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