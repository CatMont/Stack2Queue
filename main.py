
class Stack: #Create Stack Class
    def __init__(self):
        self.stack = []
    def isEmpty(self):
        if len(self.stack) > 0:
            return False
        else:
            return True
    def size(self):
        x = 0
        for i in self.stack:
            x += 1
        return x
    def push(self, item): #adds element to end
        self.stack.append(item)
    def pop(self):
        return self.stack.pop() #removes and returns element from end
    def print(self):
        for i in self.stack:
            print(i, end= " ")


s1 = Stack()
s2 = Stack()
s1.push(1)
s1.push(2)
s1.push(3)
s1.print()
print("\n")

#by popping elements from s1 and pushing them onto s2, we reverse the stack and call it s2, now it will function as a queue
s2.push(s1.pop())
s2.push(s1.pop())
s2.push(s1.pop())

#return elements from s2 last to first.
print(s2.pop())
print(s2.pop())
print(s2.pop())


def checkdelimiters(input): #checks delimiters when programming
    input = [i for i in input]
    for i in input: #inserts into Stack OpenStack
        if i == '{' or i == '(' or i == '[':
            openStack.push(i)
    input.reverse()
    for i in input:
        if i == '}' or i == ')' or i == ']':
            closeStack.push(i)
    openStack.print() #outputs Stack with left delimiters
    print('\n')
    closeStack.print() #outputs stack with right delimiters
    n = 0
    x = openStack.size() #takes size of left delimiter Stack
    y = closeStack.size() #takes size of right delimiter stack

    if x == y:
        for i in range(x):
            a = openStack.pop() #pops from stacks
            b = closeStack.pop()
            if a == '(' and b == ')' : #if each pop matches opening and closing delimiter add 1 to n
                n += 1
            elif a == '{' and b == '}':
                n += 1
            elif a == '[' and b == ']':
                n += 1
                
    else:
        return False #return false if sizes are unequal
    if n == x:
        return True #return true if N becomes equal to x
    else:
        return False # if n does not equal x, return false



openStack = Stack()
closeStack = Stack()
itscode = "["
itscode2 = "while{print(x) print(y) print(z)}"
itscode3 = "while{print(x) print(y) print(z)"
print(checkdelimiters(itscode))
print(checkdelimiters(itscode2))
print(checkdelimiters(itscode3))





