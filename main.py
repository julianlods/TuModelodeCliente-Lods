from cliente import Cliente
from articulo import Articulo
from venta import Venta

def cargar_clientes():
    #Genero la lista de clientes
    return [
        Cliente(1, "Julian", "Lods", "julian.lods@gmail.com", "30592245"),
        Cliente(2, "Mariana", "Perez", "mariana.perez@yahoo.com", "31767256"),
        Cliente(3, "Dave", "Mustaine", "dave@gmail.com", "28767923")
    ]

def cargar_articulos():
    #Genero la lista de artículos de venta
    return [
        Articulo(1, "Guitarra", "Fender", "Stratocaster", "Guitarra de 6 cuerdas", 1500, "USD"),
        Articulo(2, "Guitarra", "Jackson", "American SOLOIST", "Guitarra de 6 cuerdas", 1300, "USD"),
        Articulo(3, "Guitarra", "Ibanez", "JEM", "Guitarra de 6 cuerdas", 1700, "USD"),
        Articulo(4, "Bajo", "Fender", "Meteora", "Bajo eléctrico de 4 cuerdas", 1200, "USD")
    ]

def seleccionar_cliente(clientes):
    #Solicito y valido id_cliente
    while True:
        try:
            id_cliente = int(input("Por favor, ingrese su ID de cliente: "))
            cliente = next((c for c in clientes if c.verificar_id(id_cliente)), None)
            if cliente:
                print(f"Bienvenido/a, {cliente.obtener_datos()['nombre']} {cliente.obtener_datos()['apellido']}.")
                return cliente
            else:
                print("ID de cliente no encontrado. Intente nuevamente.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

def confirmar_compra():
    #Pregunto si confirma compra
    while True:
        confirmar = input("\n¿Desea confirmar la compra? (s/n): ").strip().lower()
        if confirmar in ['s', 'n']:
            return confirmar == 's'
        print("Opción inválida. Por favor, ingrese 's' o 'n'.")

def main():
    print("Venta de instrumentos musicales")
    clientes = cargar_clientes()
    cliente = seleccionar_cliente(clientes)
    
    articulos = cargar_articulos()
    carrito = []  # Lista para almacenar las ventas

    while True:
        print("\nArtículos disponibles:")
        for articulo in articulos:
            datos = articulo.obtener_datos()
            print(f"{datos['id_articulo']} - {datos['tipo']} {datos['marca']} {datos['modelo']} - {datos['precio']} {datos['moneda']}")
        
        try:
            opcion = int(input("\nSeleccione el ID del artículo que desea comprar: "))
            cantidad = int(input("Ingrese la cantidad: "))
        except ValueError:
            print("Por favor, ingrese valores válidos.")
            continue

        articulo_seleccionado = next((a for a in articulos if a.id_articulo == opcion), None)
        if articulo_seleccionado:
            carrito.append(Venta(cliente, articulo_seleccionado, cantidad))
            print("\nArtículo agregado al carrito.")
        else:
            print("\nArtículo no encontrado.")
        
        while True:
            continuar = input("\n¿Desea seguir comprando? (s/n): ").strip().lower()
            if continuar in ['s', 'n']:
                break
            print("Opción inválida. Por favor, ingrese 's' o 'n'.")

        if continuar == 'n':
            break

    #Confirmar la compra al finalizar
    if carrito:
        if confirmar_compra():
            for venta in carrito:
                venta.guardar_venta()
            print(f"\n¡Pedido realizado con éxito! Se enviará un correo electrónico a {cliente.obtener_datos()['email']} con la facturación.")
        else:
            print("\nCompra cancelada. No se procesó el pedido.")
    else:
        print("\nNo se realizaron compras.")

if __name__ == "__main__":
    main()
