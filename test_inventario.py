import unittest
from inventario import Producto, Inventario


class TestInventario(unittest.TestCase):

    def setUp(self):
        """Configura el entorno de pruebas antes de cada prueba."""
        self.inventario = Inventario()

    def test_agregar_producto(self):
        """Prueba agregar un producto al inventario."""
        producto = Producto("Manzana", 1.0, 10)
        self.inventario.agregar_producto(producto)
        self.assertEqual(len(self.inventario.productos), 1)
        self.assertEqual(self.inventario.productos[0].nombre, "Manzana")

    def test_eliminar_producto(self):
        """Prueba eliminar un producto del inventario."""
        producto1 = Producto("Manzana", 1.0, 10)
        producto2 = Producto("Banana", 0.5, 20)
        self.inventario.agregar_producto(producto1)
        self.inventario.agregar_producto(producto2)
        self.inventario.eliminar_producto("Manzana")
        self.assertEqual(len(self.inventario.productos), 1)
        self.assertEqual(self.inventario.productos[0].nombre, "Banana")

    def test_mostrar_inventario(self):
        """Prueba mostrar todos los productos en el inventario."""
        producto1 = Producto("Manzana", 1.0, 10)
        producto2 = Producto("Banana", 0.5, 20)
        self.inventario.agregar_producto(producto1)
        self.inventario.agregar_producto(producto2)

        expected_output = (
            "Producto: Manzana, Precio: 1.0, Cantidad: 10\n"
            "Producto: Banana, Precio: 0.5, Cantidad: 20"
        )
        self.assertEqual(self.inventario.mostrar_inventario(), expected_output)

    def test_mostrar_inventario_vacio(self):
        """Prueba mostrar inventario vacío."""
        self.assertEqual(self.inventario.mostrar_inventario(), "El inventario está vacío.")

    def test_agregar_producto_invalid(self):
        """Prueba agregar un objeto no válido al inventario."""
        with self.assertRaises(ValueError):
            self.inventario.agregar_producto("No es un producto")


if __name__ == '__main__':
    unittest.main()
