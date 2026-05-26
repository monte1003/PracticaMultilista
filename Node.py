class Node():
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.prev = None
        self.sub_list = None
        
    
    def __str__(self):
        return f"{self.__class__.__name__}(ID: {self.id}, Name: {self.name})"