class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def push(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def print_queue(self):
        current = self.front
        if not current:
            print("La cola está vacía")
            return
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

def manejar_cola():
    cola = Queue()
    while True:
        print("\nMenú de Cola:")
        print("1. Push (Agregar o Encolar)")
        print("2. Imprimir Cola")
        print("3. Regresar al menú anterior")
        print("4. Salir")
        opcion = input("Ingrese su opción: ")
        if opcion == "1":
            nuevo_elemento = input("Ingrese el elemento a encolar: ")
            cola.push(nuevo_elemento)
            print(f"Elemento {nuevo_elemento} agregado a la cola.")
        elif opcion == "2":
            print("Cola actual:")
            cola.print_queue()
        elif opcion == "3":
            break
        elif opcion == "4":
            print("Saliendo del programa...")
            exit()
        else:
            print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    while True:
        print("\nMenú de Opciones:")
        print("1. Manejar Cola")
        print("2. Salir")
        opcion = input("Seleccione una opción (1/2): ")
        if opcion == "1":
            manejar_cola()
        elif opcion == "2":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Por favor, seleccione 1 o 2.")
