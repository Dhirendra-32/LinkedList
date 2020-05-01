# here we will create structure of node in linked list : design a class node

# A Node of list will have two data point IE: data , address of next  node
import random as rndi
import math


class ListNode(object):

    def __init__(self, data):
        self.data = data
        self.next = None

# here we will design a compplete linked and some of its properties: design a class with Name Linked list

# when we say we have linked list it means we have addess of first node


class LinkedList(object):

    lenth = 0

    def __init__(self):

        self.head = None

    def addNewNode(self, data):

        newNode = ListNode(data)

        if self.head is None:

            self.head = newNode

            return self.head

        else:

            temp = self.head

            while (temp.next):

                temp = temp.next

            temp.next = newNode

            # self.head = self.head.next

            return self.head

    def traverseList(self):

        temp = self.head

        while (temp):

            print(temp.data)

            temp = temp.next

    def reverseList(self):

        print("reversed list ")

        previous = None

        current = self.head

        while current is not None:

            nxet = current.next

            current.next = previous

            previous = current

            current = nxet

        return previous

    def lenthOfList(self, Dict):

        head = self.head

        lenth = self.lenth
        i = 1
        while (head):

            Dict[i] = head

            lenth += 1

            i += 1

            head = head.next

        self.lenth = lenth

        return Dict

    def middleNode1(self):

        head = self.head

        lenth = self.lenth

        lenth = (math.ceil((lenth / 2)) - 1)

        while (lenth):

            head = head.next

            lenth -= 1

        return head.data

    # Using two pointer

    def middleNode2(self):

        head = self.head

        forward = head

        while (forward and forward.next):

            head = head.next

            forward = forward.next.next

        return head.data

    def reversedList_recursive(self, head):

        if head is None:

            return None

        if head.next is None:

            self.head = head

            return head

        else:

            self.reversedList_recursive(head.next)

            head.next.next = head

            head.next = None

    def deleteNode(self, data):

        found = False

        head = self.head

        if head is None:

            return f"Linked list is empty "

        if head.data == data:

            found = True

            self.head = head.next

            head = None

            self.lenth -= 1

            return self.head

        while head:

            if head.data == data:

                found = True

                break

            else:

                prev = head

                head = head.next

        if found and head.next is not None:

            prev.next = head.next

            self.lenth -= 1

            return head

        elif found and head.next is None:

            prev.next = None

            self.lenth -= 1

            return head

        else:

            print(("Node didnt find"))

            return


""" instanciation start from here """

list = LinkedList()

# Begin -creating linked list of of our lenth

Dict = dict()

print("Enter the lenth of Linked list ")

lenth = int(input())

print("Given lenth is ", lenth)

for i in range(1, lenth+1):

    value = int(input("enter number here"))

    print('Node [{0}] data '.format(i), value)

    list.addNewNode(value)

# End

# """ we can call any function from here """

ReturnHashTable = list.lenthOfList(Dict)
print("lenth is "+str(list.lenth))
print('Middle Node of Linked list is :{0}'.format(list.middleNode1()))
print('Middle Node of Linked list is :{0}'.format(list.middleNode2()))


# < ------------------------------------------------------- ->
#  creating has table(ReturnHashTable) containing node of linked list and its posittion and looping it's object data fiels

for i in ReturnHashTable.values():

    print(i.data)

