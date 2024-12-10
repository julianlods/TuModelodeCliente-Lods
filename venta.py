import csv

class Venta:
    def __init__(self, cliente, articulo, cantidad):
        self.cliente = cliente
        self.articulo = articulo
        self.cantidad = cantidad

    def guardar_venta(self, archivo="ventas.csv"):
        datos = {
            "cliente_id": self.cliente.obtener_datos()['id_cliente'],
            "cliente_nombre": f"{self.cliente.obtener_datos()['nombre']} {self.cliente.obtener_datos()['apellido']}",
            "cliente_email": self.cliente.obtener_datos()['email'],
            "articulo_id": self.articulo.id_articulo,
            "articulo_tipo": self.articulo.tipo,
            "articulo_marca": self.articulo.marca,
            "articulo_modelo": self.articulo.modelo,
            "cantidad": self.cantidad,
            "total": self.articulo.precio * self.cantidad,
            "moneda": self.articulo.moneda
        }
        with open(archivo, mode="a", newline="") as f:
            escritor = csv.DictWriter(f, fieldnames=datos.keys())
            if f.tell() == 0:  # Si el archivo está vacío, escribir el encabezado
                escritor.writeheader()
            escritor.writerow(datos)
