
import random
class Node:
  def __init__(self,num,color,next=None):
    self.num=num
    self.color=color
    self.next=next

  def getData(self):
    dictt={"Number": self.num, "Color": self.color}
    return dictt

  def getNumber(self):
    return self.num

  def getColor(self):
    return self.color

  def getNext(self):
      return self.next
    
  def setNumber(self, num):
    self.num=num

  def setColor(self, color):
    self.color=color

  def  setNext(self,node):
      self.next=node



class Stack(Node):
    def __init__(self,limit):
      self.top=None
      self.limit=limit
      self.length=0

    def isEmpty(self):
        return self.length==0

    def isFull(self):
        return self.length==self.limit

    def getTop(self): 
     return self.top   

    def peek(self):
        return self.top.getData()

    def pop(self):
        if self.isEmpty():
            return("Stack is empty")
        else:
            rem=self.top
            self.top=rem.getNext()
            self.length-=1
            return rem.getData()

    def push(self,num,color) :
        if self.isFull():
            print("Stack is full")
        else:
            new=Node(num,color)
            new.setNext(self.top)
            self.top=new
            self.length+=1


    def getData(self): 
       data=[]
       currentNode=self.top
       while currentNode:
         if currentNode.getData()!= None:
            data.append(currentNode.getData())
         currentNode=currentNode.getNext()
       return data      
    # def getData(self):
    #    dictt={"Number": self.num, "Color": self.color}
    #    return dictt        

# randomlist = random.sample(range(10, 30), 5)
s=Stack(20)
colors=["red","yeallow","green","blue"]
for m in range(1,21):
  s.push(int(random.randint(1,9)),random.choice(colors))



# s.push(int(random.randint(1,9)),random.choice(colors))
# s.push(int(random.randint(1,9)),random.choice(colors))
# s.push(4,"red")
# s.push(6,"blue")
# p1=[]
# p2=[]
print("-------------------------")
print("player 1:")
print("-------------------------")
c=1
while c!=6:
  lis=[]
  lis=s.pop()
  print(f'{c}- {lis["Color"]}-{lis["Number"]}')
  c+=1
  # print(s.pop())
  # c+=1
print("-------------------------")
print("player 2:")
print("-------------------------")
c=1
while c!=6:
  lis=[]
  lis=s.pop()
  print(f'{c}- {lis["Color"]}-{lis["Number"]}')
  c+=1
print("\n")

print("-------------------------")

c=1
while c!=2:
  lis=[]
  lis=s.pop()
  print(f'First card in deck: {lis["Color"]}-{lis["Number"]}')
  c+=1
print("-------------------------")



# print(s.pop())
# print(s.pop())
# print(s.pop())
# print(s.pop())
