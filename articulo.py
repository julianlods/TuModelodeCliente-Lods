class Articulo:
    def __init__(self, id_articulo, tipo, marca, modelo, descripcion, precio, moneda):
        self.id_articulo = id_articulo
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.descripcion = descripcion
        self.precio = precio
        self.moneda = moneda

    def obtener_datos(self):
        return {
            "id_articulo": self.id_articulo,
            "tipo": self.tipo,
            "marca": self.marca,
            "modelo": self.modelo,
            "descripcion": self.descripcion,
            "precio": self.precio,
            "moneda": self.moneda
        }
