"""
Se trata de escribir un programa con un CRUD para productos
Cada producto debe tener los siguientes datos:
Codigo (string), Nombre (string), precio (float), saldo (int)
"""
class Productos:
    def __init__(self, listado):
        self.listado = listado
    
    def buscar(self, cod):
        posicion = -1
        for i in range(len(self.listado)):
            if self.listado[i]["codigo"]==cod:
                posicion = i
                break
        return posicion
    
    def agregar(self,prod):
        pos = self.buscar(prod["codigo"])
        if pos==-1:
            self.listado.append(prod)
            return 0
        else:
            return 1
    
    def eliminar(self, cod):
        pos = self.buscar(cod)
        if pos==-1:
            return 1
        else:
            del self.listado[pos]
            return 0
    
    def modificar(self, prod):
        pos = self.buscar(prod["codigo"])
        if pos==-1:
            return 1
        else:
            self.listado[pos] = prod
            return 0
    
    def listar(self):
        return self.listado
    
def crear_producto(codigo, nombre, precio, saldo):
    return {
        "codigo": codigo,
        "nombre": nombre,
        "precio": precio,
        "saldo": saldo
    }

productos = Productos([])