class ventas:
    def __init__(self, productos, clientes):
        self.productos = productos
        self.clientes = clientes
        self.historial = []

    def realizar_venta(self, cod_producto, id_cliente, cantidad):
        pos_prod = self.productos.buscar(cod_producto)
        pos_cli = self.clientes.buscar(id_cliente)

        if pos_prod == -1:
            return "producto no existe"
        if pos_cli == -1:
            return "cliente no existe"
        
        producto = self.productos.listado[pos_prod]
        cliente = self.clientes.listado[pos_cli]

        if producto["saldo"] < cantidad:
            return "no hay suficiente stock del producto"
        
        total = producto["precio"] * cantidad

        if cliente["saldo"] >= total:
           cliente["saldo"] -= total
        elif cliente["saldo"] + cliente["cupo_credito"] >= total:
            restante = total - cliente["saldo"]
            cliente["saldo"] = 0
            cliente["cupo_credito"] -= restante
        else:
            return "saldo y cupo insuficiente"
        
        producto["saldo"] -= cantidad

        venta = {
            "producto": cod_producto,
            "cliente": id_cliente,
            "cantidad": cantidad,
            "total": total

        }
        self.historial.append(venta)
        return "venta realizada"
