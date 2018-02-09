
# stack

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def pop(self):
        t = top.data
        top = top.next
        return t

    def push(self, item)
        t = StackNode(item)
        t.next = top
        top = t

    def peek(self):
        if top == None:
            raise Exception("Empty Stack Exception")
        return top.data

    def is_empty(self):
        return top == None

