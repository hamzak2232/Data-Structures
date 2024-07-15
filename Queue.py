from Stack import is_empty

queue = []

def enqueue(item):
    global queue
    queue[len(queue):] = [item]
    print(f"Enqueue {item} to queue.")

def pop():
    if is_empty():
        print("Queue is empty. Cannot pop.")
        return None
    item = queue[0]
    del queue[0]
    return item

def peek():
    if is_empty():
        print("Queue is empty. Nothing to peek.")
        return None
    print("\nFront and Rear: ")
    return queue[-1], queue[0]

enqueue(1)
enqueue(2)
enqueue(3)

print(queue)
print(f"Popped item: {pop()}")
print(f"Popped item: {pop()}")
print(f"Popped item: {pop()}")