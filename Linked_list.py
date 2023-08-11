class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

        
def Printll(head):                #TRAVERSALL LINKED LIST
    while head is not None:
        print(head.data)
        head=head.next
    print("None")

def insert_begin(data,head):      #INSERT BEGIN
    newNode = Node(data)
    newNode.next=head
    head=newNode
    return head

def insert_pos(data,head,pos):    #INSERT AT POSITION
    prev=None
    cur=head
    i=0
    while i<pos:
        prev=cur
        cur=cur.next
        i+=1
    newNode=Node(25)
    prev.next=newNode
    newNode.next=cur
    return head


def insert_end(data,head):          #INSERT END
    cur=head
    while cur.next is not None:
        cur=cur.next
    newNode=Node(data)
    cur.next=newNode
    return head

def delete_at_begin(head):        #DELETE BEGIN
    head=head.next
    return head


def delete_at_pos(head,pos):     #DELETE POS
    prev=None
    cur=head
    i=0
    while i<pos:
        prev=cur
        cur=cur.next
        i+=1
    prev.next=cur.next
    return head

def deletion_at_end(head):      #DELETE END
    prev=None
    cur=head
    while cur.next is not None:
        prev=cur
        cur=cur.next
    prev.next=None
    return head


x=Node(10)                    #NODE CREATION
y=Node(20)
z=Node(30)

x.next=y
y.next=z
z.next=None


#Printll(x)                  #Traversallll


#llb=insert_begin(150,x)     #INSERT BEGIN
#Printll(llb)

#llp=insert_pos(25,x,2)      #INSERT AT POSITION
#Printll(llp)


#lle=insert_end(40,x)        #INSERT END
#Printll(lle)

#ll_db=delete_at_begin(y)    #DELETE BEGIN
#Printll(ll_db)


#ll_dp = delete_at_pos(x,1)  #DELETE POS
#Printll(ll_dp)

#ll_de = deletion_at_end(x)   #DELETE END
#Printll(ll_de)

