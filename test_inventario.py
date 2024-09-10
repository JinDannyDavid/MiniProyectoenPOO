import unittest
from io import StringIO
import sys
from inventario import Producto, Inventario


class TestInventario(unittest.TestCase):

    def setUp(self):
        self.inventario = Inventario()

    def test_agregar_producto(self):
        producto = Producto("Manzana", 1.0, 10)
        self.inventario.agregar_producto(producto)
        self.assertEqual(len(self.inventario.productos), 1)
        self.assertEqual(self.inventario.productos[0].nombre, "Manzana")

    def test_eliminar_producto(self):
        producto1 = Producto("Manzana", 1.0, 10)
        producto2 = Producto("Banana", 0.5, 20)
        self.inventario.agregar_producto(producto1)
        self.inventario.agregar_producto(producto2)
        self.inventario.eliminar_producto("Manzana")
        self.assertEqual(len(self.inventario.productos), 1)
        self.assertEqual(self.inventario.productos[0].nombre, "Banana")

    def test_mostrar_inventario(self):
        producto1 = Producto("Manzana", 1.0, 10)
        producto2 = Producto("Banana", 0.5, 20)
        self.inventario.agregar_producto(producto1)
        self.inventario.agregar_producto(producto2)

        captured_output = StringIO()
        sys.stdout = captured_output
        self.inventario.mostrar_inventario()
        sys.stdout = sys.__stdout__

        output = captured_output.getvalue().strip().split('\n')
        self.assertIn("Producto: Manzana, Precio: 1.0, Cantidad: 10", output)
        self.assertIn("Producto: Banana, Precio: 0.5, Cantidad: 20", output)


if __name__ == '__main__':
    unittest.main()
