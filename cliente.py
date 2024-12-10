class Cliente:
    def __init__(self, id_cliente, nombre, apellido, email, dni):
        self.__id_cliente = id_cliente
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__dni = dni

    def obtener_datos(self):
        return {
            "id_cliente": self.__id_cliente,
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "email": self.__email,
            "dni": self.__dni
        }

    def verificar_id(self, id_cliente):
        return self.__id_cliente == id_cliente
