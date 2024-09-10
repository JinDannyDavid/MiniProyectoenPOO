class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def mostrar_detalles(self):
        return f"Producto: {self.nombre}, Precio: {self.precio}, Cantidad: {self.cantidad}"

class Inventario:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise ValueError("El objeto debe ser una instancia de la clase Producto")

    def eliminar_producto(self, nombre_producto):
        self.productos = [p for p in self.productos if p.nombre != nombre_producto]

    def mostrar_inventario(self):
        if not self.productos:
            return "El inventario está vacío."
        return "\n".join([producto.mostrar_detalles() for producto in self.productos])
