"""
Se trata de escribir un programa con un CRUD para clientes
Cada producto debe tener los siguientes datos:
Identificación (string), Nombre (string), saldo (float), 
cupo_crédito (float)
"""

class Clientes:
    def __init__(self, listado_clientes):
        self.listado_clientes = listado_clientes

    def buscar(self, ident):
        posicion = -1
        for i in range(len(self.listado_clientes)):
            if self.listado_clientes[i]["identificacion"]==ident:
                posicion = i
                break
        return posicion

    def agregar(self, cliente):
        pos = self.buscar(cliente["identificacion"])
        if pos==-1:
            self.listado_clientes.append(cliente)
        else:
            return 1

    def modificar(self, ident, cliente):
        pos = self.buscar(ident)
        if pos != -1:
            self.listado_clientes[pos] = cliente
        else:
            return 1

    def eliminar(self, ident):
        pos = self.buscar(ident)
        if pos != -1:
            del self.listado_clientes[pos]
            return 0
        else:
            return 1

    def listar(self):
        return self.listado_clientes
    
    def mostrar_clientes(self):
        for cliente in self.listado_clientes:
            print(cliente)

def crear_cliente(identificacion, nombre, saldo, cupo_credito):
    return {
        "identificacion": identificacion,
        "nombre": nombre,
        "saldo": saldo,
        "cupo_credito": cupo_credito
    }
