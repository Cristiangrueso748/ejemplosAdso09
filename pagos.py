import json

class pagos:

    def __init__(self, pagos):
        self.pagos = pagos
    def buscar(self, ident):
        posicion = -1
        for i in range(len(self.pagos)):
            if self.pagos[i]["identificacion"]==ident:
                posicion = i
                break
        return posicion

    def agregar(self, pago):
        pos = self.buscar(pago["identificacion"])
        if pos==-1:
            self.pagos.append(pago)
        else:
            return 1
        
    def modificar(self, ident, pago):
        pos = self.buscar(ident)
        if pos != -1:
            self.pagos[pos] = pago
        else:
            return 1
        else:
            self.listado[pos] = pagos
            return 0
    
    def listar(self):
        return self.listado
        
    def mostrar_pagos(self):
        for pagos in self.pagos:
            print(pagos)


    