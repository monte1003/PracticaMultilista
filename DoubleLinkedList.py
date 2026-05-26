from Node import Node
class DoubleLinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_child(self, parent:Node, child:Node):
        if parent.sub_list is None:
            sublist = DoubleLinkedList()
            sublist.head = child
            sublist.tail = child
            parent.sub_list = sublist
        else:
            current = parent.sub_list.tail
            current.next = child
            child.prev = current
            parent.sub_list.tail = child
        
        return parent.sub_list
    
    def append (self, new_node): # Para añadir nuevos nodos en el mismo nivel de una lista, es decir, no hijos, sino hermanos
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.prev = None  # Asegurar que no arrastre basura
            new_node.next = None
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = None
            
    def print_multilist(self, level=0):
        if self.head is None:
            print("Empty list")
            return

        current = self.head

        while current:
            print("  " * level + str(current))

            if current.sub_list:
                current.sub_list.print_multilist(level + 1)
            current = current.next

    def get_markers(self, multilist):
        markers = []

        current_country = multilist.head

        while current_country:
            if current_country.sub_list:
                current_department = current_country.sub_list.head

                while current_department:
                    if current_department.sub_list:
                        current_city = current_department.sub_list.head

                        while current_city:
                            # aquí se procesa cada ciudad
                            current_city = current_city.next

                    current_department = current_department.next

            current_country = current_country.next

        return markers
    
    def delete_value(self, search_value):
        current = self.head
        while current:
            # Caso Base: Si encontramos el nodo en el nivel actual, lo desvinculamos
            if current.id == search_value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True
            
            # Caso Recursivo: Si el nodo actual tiene una sublista, buscamos ahí abajo
            if current.sub_list:
                # Llamamos recursivamente al método en la sublista
                eliminado = current.sub_list.delete_value(search_value)
                if eliminado:
                    # Si la sublista quedó completamente vacía tras borrar el nodo, 
                    # limpiamos el puntero para no dejar una lista fantasma
                    if current.sub_list.head is None:
                        current.sub_list = None
                    return True
            
            current = current.next
            
        return False