class TemaMusical():
    def __init__(self, codigo=None, nombre=None, duracion=0, interprete=None):
        self.codigo = codigo
        self.nombre = nombre
        self.duracion = duracion
        self.interprete = interprete
    
    def __str__(self):
        return (f'codigo: {self.codigo}\n\tnombre: {self.nombre}\n\tduracion: {self.duracion}\n\tinterprete: {self.interprete}\n')
    
    @property
    def codigo(self):
        return self._codigo
    
    @codigo.setter
    def codigo(self, valor):
        if valor == '':
            raise EmptyError('Error')
        else:
            self._codigo = valor
    
    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self, valor):
        if valor == '':
            raise EmptyError('Error')
        else:
            self._nombre = valor
    
    @property
    def duracion(self):
        return self._duracion
    
    @duracion.setter
    def duracion(self, valor):
        if valor < 0:
            raise ValueError
        else:
            self._duracion = valor
    
    @property
    def interprete(self):
        return self._interprete
    
    @interprete.setter
    def interprete(self, valor):
        if valor == '':
            raise EmptyError('Error')
        else:
            self._interprete = valor

    def input(self, state=False):
        if state is False:
            self.codigo = input('Agregue un codigo')
            self.nombre = input('Agregue un nombre')
            self.duracion = int(input('Agregue una duracion'))
            self.interprete = input('Agregue un interprete')
            return TemaMusical(self.codigo, self.nombre, self.duracion, self.interprete)
        else:
            self.nombre = input('Agregue un nombre')
            self.duracion = int(input('Agregue una duracion'))
            self.interprete = input('Agregue un interprete')
            return TemaMusical(self.codigo, self.nombre, self.duracion, self.interprete)

class EmptyError(Exception):
    def __init__(self, valor):
        self.valor = valor
    def __rpr__(self):
        return ('No puede estar vacio', self.valor)
