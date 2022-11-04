import sys
##create a node 
class Node:
    def __init__(self,dataVal=None):
        self.dataval=dataVal
        self.nextval=None

##Single list class
class SLinkedList:
    def __init__(self):
        self.headval=None

    def listPrint(self):
        printval=self.headval
        if printval==None:
            print("List is empty")
        else:    
            print("\nThe List is: ")
            while printval is not None:
                if printval.nextval == None:
                    print(printval.dataval,end=" ")
                else:
                    print(printval.dataval,end=" ->")    
                printval=printval.nextval

    def atBeggining(self,newdata):
        Newnode=Node(newdata) 
        Newnode.nextval= self.headval
        self.headval=Newnode

    def atEnd(self,newdata):
        Newnode=Node(newdata)
        if self.headval is None:
            self.headval=Newnode
            return
        laste=self.headval
        while laste.nextval:
            laste=laste.nextval
        laste.nextval=Newnode

    def removeNode(self,renode):
        temp=self.headval
        if temp is not None:
            if temp.dataval==renode:
                self.headval=temp.nextval
                temp=None
                return
        while temp is not None:
            if temp.dataval==renode:
                break
            prev=temp
            temp=temp.nextval
        if temp==None:
            return 
        prev.nextval=temp.nextval
        temp=None               


                    


Slist=SLinkedList()
# Slist.headval=Node("Mon")
# e2=Node("Tue")
# e3=Node("Wed")
# Slist.headval.nextval=e2
# e2.nextval=e3
# Slist.listPrint()

while True:
    print("\n1.CREATE || 2.SHOW || 3.INSERT AT BEGGING || 4.INSERT AT END || 5.DELETE || 6.EXIT ")
    choice=input("Enter your choice: ")
    if choice=='1':
       n=int(input("Enter a number: "))
       Slist.headval=Node(n)
    elif choice=='2':
      Slist.listPrint()
    elif choice=='3':
        n=int(input("Enter a number: "))
        Slist.atBeggining(n)
    elif choice=='4':
        n=int(input("Enter a number: "))
        Slist.atEnd(n)
    elif choice=='5':
        n=int(input("Enter a number to be deleted: "))
        Slist.removeNode(n)    
    elif choice=='6':
        sys.exit("You exit from program! ") 
    else:
        print("You choose wrong choice")
              
        