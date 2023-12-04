class Stack:
    def __init__(self):
        self.stack=[]
    def push(self,x):
        self.stack.append(x)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Empty"
    def is_empty(self):
        return len (self.stack)==0
def perform_operations(operations):
    stack=Stack()
    results=[]
    for a in operations:
        if a[0]=="push":
            stack.push(int(a[1]))
        elif a[0]=="pop":
            results.append(stack.pop())
    return results
T=int(input())
operations=[input().split() for _ in range(T)]
output=perform_operations(operations)
for result in output:
    print(result)


        
