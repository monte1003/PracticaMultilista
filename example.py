def search_by_attr(self, attr, value):
        """
        Busca un nodo en profundidad (recursivo) comparando el valor 
        de un atributo específico de forma dinámica usando getattr().
        """
        current = self.head
        while current:
            # Caso Base: Compara el atributo en el nivel actual de forma reflexiva
            # El tercer parámetro (None) evita errores si el atributo no existe en el nodo
            if getattr(current, attr, None) == value:
                return current
            
            # Caso Recursivo: Si el nodo tiene una sublista, busca ahí abajo
            if current.sub_list:
                nodo_encontrado = current.sub_list.search_by_attr(attr, value)
                if nodo_encontrado:
                    return nodo_encontrado # Si lo encuentra abajo, lo va retornando
            
            current = current.next
        return None

def update_value(self, search_value, **attrs):
        """
        Localiza un nodo por su ID (en cualquier nivel) y actualiza 
        dinámicamente uno o múltiples atributos usando setattr().
        """
        # 1. Buscamos el nodo en toda la estructura usando nuestro método reflexivo
        node = self.search_by_attr('id', search_value)
        
        # 2. Si el nodo existe, modificamos solo los atributos que nos pasaron
        if node:
            # attrs.items() convierte los argumentos clave=valor en un diccionario iterable
            for k, v in attrs.items():
                # setattr(objeto, propiedad, valor) modifica el atributo sin romper los enlaces de la lista
                setattr(node, k, v)
            return True # Modificación exitosa
            
        return False # El ID no existía en ningún nivel