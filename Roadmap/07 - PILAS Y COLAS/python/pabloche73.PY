# Pila/stack (LIFO)

stack = []
stack.append("1") # Push
stack.append("2")
stack.append("3")
print (stack)

stack_item = stack[len(stack) - 1] # Pop
del stack[len(stack) - 1] # Pop

stack.pop() # Pop (equivalent to the previous two lines)

print (stack_item)
print (stack)

# Cola/queue (FIFO)
queue = []
queue.append("1") # Push
queue.append("2")
queue.append("3")

print (queue)

# deque (double-ended queue)
print(queue.pop(0))

print(queue)

# Extra

def navegacion():

    stack = []
    while True:

        action = input("Añade una web, navega hacia adelante (f) o hacia atrás (b)? (o 'q' para salir): ")   
        if action == "q":
            print("Saliendo...")
            break
        elif action == "f":
            pass
        elif action == "b":
            if len(stack) > 0:
                stack.pop() 
        else:
            stack.append(action)

        if len(stack) > 0:
            print(f"Has navegado a la web: {(stack[len(stack) - 1])}")
        else:
            print("Estas en la pagina de inicio")
        
    
navegacion()

def shared_printer():
    queue = []
    while True:
        action = input("Añade un documento a la cola, imprime (p) o sale (q): ")
        if action == "q":
            print("Saliendo...")
            break
        elif action == "p":
            if len(queue) > 0:
                print(f"Imprimiendo: {queue.pop(0)}")
            else:
                print("No hay documentos en la cola")
        else:
            queue.append(action)
        print(f"Cola: {queue}")

shared_printer()