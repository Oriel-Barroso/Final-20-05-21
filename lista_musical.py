class ListaMusical():
    def __init__(self, temas={}):
        self.temas = temas

    def add(self, obj):
        self.temas[obj.codigo] = obj
        if obj in self.temas:
            raise KeyError
    
    def update(self, obj, codigo):
        if obj.codigo in self.temas:
            self.temas[codigo] = obj
        else:
            raise KeyError
    
    def delete(self, cod):
        if cod in self.temas:
            del self.temas[cod]
        else:
            raise KeyError

           
    
    def find_by_id(self, codigo):
        for k,v in self.temas.items():
            if codigo == k:
                return v
            else:
                raise KeyError
    
    def find_all(self):
        lista = []
        for k,v in self.temas.items():
            lista.append(v)
        return lista
    

        
            
