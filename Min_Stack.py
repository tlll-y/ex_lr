class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack:
            self.min_stack.append(value)
        else:
            m = min(self.min_stack[-1],value)
            self.min_stack.append(m)

    def pop(self):
        if not self.stack:
            raise IndexError("Пустой стек")
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
        if not self.stack:
            raise IndexError("Пустой стек")
        return self.stack[-1]

    def get_min(self):
        if not self.stack:
            raise IndexError("Пустой стек")
        return self.min_stack[-1]

stack = MinStack()

stack.push(-2)
stack.push(0)
stack.push(-3)

print(stack.get_min())

stack.pop()

print(stack.top())
print(stack.get_min())
