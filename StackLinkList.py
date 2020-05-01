import Node as node1
        
class StackLinkList:
    def __init__(self):
        self.__top = None
        self.__count = 0

    def set_top(self, value):
        self.__top = value

        
    def push(self, data):
        node = node1.Node(data)
        self.__count+=1
        if self.__top == None:
            self.__top = node
        else:
            node.set_next(self.__top)
            self.__top = node
            
    def isEmpty(self):
        if self.__top == None:
            return True
        else:
            return False
        
    def pop(self):
        if self.isEmpty():
            return "Stack is Empty"
        else:
            poped_link = self.__top
            self.__top = self.__top.get_next()
            poped_link.set_next(None)
            return poped_link.get_data()
        
    def peek(self):  # Return Head Node Data
        if self.isEmpty():
            return "Stack is Empty"
        else:
            return self.__top.get_data()
        
    def display(self):
        head = self.__top
        self.__count = 0
        if self.isEmpty():
            return True
        else:
            while head != None:
                print(head.get_data())
                self.__count+=1
                head = head.get_next()
        
    def get_count(self):
        return self.__count
    
    def get_top(self):
        return self.__top
        # class Node:
#     def __init__(self, data):
#         self.__data=data
#         self.__next=None
#       
#     def get_data(self):
#         return self.__data
#   
#     def set_data(self, data):
#         self.__data = data
#     
#     def get_next(self):
#         return self.__next
#   
#     def set_next(self, next_node):
#         self.__next = next_node

# String1 = "Raghvendra Pal"
# stack = StackLinkList()
# for char in String1:
#     stack.push(char)
#     
# print("*"*40)
# stack.display()
# print("*"*40)
# print("Count of words : ",stack.get_count())
# print("*"*40)
# String2 = ""
# print(String1)
# print("*"*40)
# for i in range(stack.get_count()):
#     String2+=stack.pop()
# # Time Complexity = O(n)
# # Space Complexity = O(n) We are creating new stack in Computer Memory
# print(String2)
# stack.push("A")
# stack.push("B")
# stack.push("C")
# stack.push("D")
# stack.push("E")
# stack.push("F")
# print("*"*30)
# if stack.display():
#     print("Stack is empty")
# stack.display()
# print("size of stack ",stack.get_count())
# print("*"*30)
# stack.pop()
# stack.pop()
# stack.pop()
# if stack.display():
#     print("Stack is empty")
# print("size of stack ",stack.get_count())
# print("*"*30)
# stack.pop()
# stack.pop()
# stack.pop()
# if stack.display():
#     print("Stack is empty")
# print("*"*30)
# print("size of stack ",stack.get_count())




# It uses time n/2 and constant space
# Time Complexity = O(n)
# Space = O(1) We are using existing String to reverse
# String1 = "Raghvendra"
# list_S = list(String1)
# j = len(list_S)-1
# for i in range((len(list_S)//2)+1):
#     if i < j:
# #         temp = String1[i]
# #         String1[i] = String1[j]
# #         String1[j] = temp
#         list_S[i], list_S[j] = list_S[j], list_S[i]
#     else:
#         break
#     j-=1
#     
# print("".join(list_S))