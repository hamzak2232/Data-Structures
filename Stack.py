stack = []

def push(item):
    global stack
    stack[len(stack):] = [item]
    print(f"Pushed {item} to stack.")


def pop():
    if is_empty():
        print("Stack is empty. Cannot pop.")
        return None
    item = stack[-1]
    del stack[-1]
    return item

def peek():
    if is_empty():
        print("Stack is empty. Nothing to peek.")
        return None
    return stack[-1]

def is_empty():
    return len(stack) == 0

def size():
    count = 0
    for _ in stack:
        count += 1
    return count

print(f"Stack created. Is empty: {is_empty()}")

push(12)
push(32)
push(9)
push(47)
push(37)
push(99)
print(f"Top of stack: {peek()}")
print(f"Stack size: {size()}")
print(f"Popped item: {pop()}")
print(f"Top of stack after pop: {peek()}")
print(f"Stack size after pop: {size()}")
print(f"Popped item: {pop()}")
print(f"Popped item: {pop()}")
print(f"Popped item: {pop()}")

push(4)
push(5)
print(f"Stack size: {size()}")
print(f"Top of stack: {peek()}")
print(f"Popped item: {pop()}")
print(f"Stack is empty: {is_empty()}")
print(f"Stack size: {size()}")
