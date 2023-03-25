class Stack:
    # Initialize an empty stack
    def __init__(self):
        self.items = []

    # Check if the stack is empty
    def is_empty(self):
        return(self.items==[])

    # Add an item to the stack
    def push(self, item):
        self.items.append(item)

    # Remove an item from the top of the stack
    def pop(self):
        return(self.items.pop())

    # Return the number of items in the stack
    def size(self):
        return len(self.items)

    # Return the item at the top of the stack without removing it
    def peep(self):
        l = len(self.items) - 1
        return self.items[l]

# Create an instance of the Stack class
stack = Stack()

# Check if the stack is empty
is_empty = stack.is_empty()
if is_empty:
    print("The stack is empty.")

# Add items to the stack
for i in range(0, 15):
    stack.push(i)



print(f"The size of the stack is: {stack.size()}")

print(f"The items of the stack are: {stack.items}")
