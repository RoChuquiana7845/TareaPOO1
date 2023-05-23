from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas
from datetime import date


class tienda:
    def __init__(self,id, nombre, ruc, ubicacion):
        self.id= id
        self.nombre= nombre
        self.ruc= ruc
        self.ubicacion= ubicacion
        
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.ruc} - {self.ubicacion}"


class inventario:
    def __init__(self, id, stock, min_stock, producto):
        self.id = id
        self.stock = stock 
        self.min_stock = min_stock 
        self.producto
    
    def __str__(self):
        return f"{self.id} - {self.stock} - {self.min_stock} - {self.producto}"
    
    def actualizar(self, productos_vendidos, tipo):
        if tipo == self.producto.tipo_producto.tipo:
            self.stock -= productos_vendidos
        
    def abastecer(self):
        if self.stock < self.min_stock:
            print("****ALERTA***\nCantidad de producto de {self.producto.nombre} esta por debajo del minimo, llamar al proveedor :'c")
        
        
class producto:
    def _init_(self, id , nombre, precio, tipo_producto):
        self.id=id
        self.nombre= nombre
        self.precio= precio
        self.tipo_producto = tipo_producto
        
    def __str__( self):
        return f"{self.id} - {self.nombre} - {self.precio}"
    
    def modificar_producto(self):
        print('Ingresa el número de la opción')
        while True:
            try:
                opcion = int(input('Qué desea modificar?:\n1:nombre\n2:precio'))
            except ValueError:
                print('Entrada invalida, solo se acepta números')
            else: 
                if 1 <= opcion <= 2:
                    match opcion: 
                        case 1:
                            self.nombre = input('Ingrese el nuevo nombre del producto: ')
                        case 2:
                            self.precio = input('Ingrese el nuevo precio del producto: ')
                else:
                    print('Opcion fuera de rango')
        
    def visualizar_producto(self):
        print(f'***Producto***\n Nombre: {self.nombre} \n Precio_sinIVA: {self.precio} \n Tipo: {self.tipo_producto.tipo} \n Impuesto: {self.tipo_producto.impuesto} ')
                    
                
class tipo_producto:
    def __init__(self, id, tipo, impuesto):
        self.id = id
        self.tipo = tipo
        self.impuesto = impuesto
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.impuesto}"
   
    
    
class cliente:
    def _init_ (self, id, nombre, cedula):
        self.id=id
        self.nombre= nombre
        self.correo= cedula
        
    def __str__( self):
        return f"{self.id}- {self.nombre} - {self.cedula}"
                        
class venta:
    def __init__(self,id, cliente, detalle_venta, fecha, total_venta, total_producto):
        self.id=id
        self.cliente = cliente
        self.detalle_venta = detalle_venta
        self.fecha=fecha
        self.total_venta= total_venta
        self.total_producto= total_producto
        
    def __str__(self):
        return f" {self.id} - {self.detalle} - {self.fecha} - {self.totalVenta}"
    
    def imprimir_factura(self, nombre, ruc, correo): 
        w, h = letter
        datos_tienda = [nombre, ruc, correo]
        metadatos_venta = {'50': "Producto", '200': 'Cantidad', '300': 'Precio Unitario', '400': 'Impuesto', '500': 'Subtotal'}
        values_venta = {'50': self.detalle_venta.producto.nombre, '200': self.detalle_venta.cantidad, '300': self.detalle_venta.producto.tipo_producto.impuesto, '400': self.detalle_venta.producto.tipo_producto.impuesto, '500': self.detalle_venta.subtotal}
        factura = canvas.Canvas("Factura.pdf", pagesize =letter) 
        factura.drawImage('./img/carrito_de_supermercado.png', 50, h-50, width=65, height=65)
        factura.setFont('Times-Roman', 15)
        i = 1
        for x in datos_tienda:
            factura.drawString(w/2, h-(50+i*16), f"{x}")
            i += 1
            if datos_tienda.index(x) == -1:
                factura.drawString(50, h-(50+i*16), f"Cliente -> Nombre:{self.cliente.nombre} CI: {self.cliente.cedula}")
                i += 1
        factura.line(50, h-(50+i*16), w-50, h-(50+i*16))
        i += 1
        for key, value in metadatos_venta.items():
            factura.drawString(key, h-(50+i*16), f"{value}")
        factura.line(50, h-(50+(i+1)*16), w-50, h-(50+(i+1)*16))
        
        for key, value in values_venta.items():
            factura.drawString(key, h-(50+(i+2)*16), f"{value}")
        
        print('**Factura realizada**')
    
class detalle_venta:
    def __init__(self, id, producto, cantidad, subtotal):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = subtotal 
        
    def __str__(self):
        return f"{self.id} - {self.producto} - {self.cantidad} - {self.subtotal}"

class reporte_tienda: 
    def __init__(self, id, fecha, venta):
        self.id = id
        self.fecha = fecha
        self.venta = venta
        self.ingresos = 0
    
    def calcular_producto_popular(self, nombres_productos):
        productos_vendidos = []
        productos_vendidos.append(self.venta.detalle_venta.producto)
        ocurrencias_producto = {}
        contador = 0
        for x in nombres_productos: 
            if x == nombres_productos[contador]:
                ocurrencias_producto[x] = productos_vendidos.count(x)
                contador += 1
        max = 0
        for values in ocurrencias_producto.values():
            if max < values:
                max = values
                
        for key, item in ocurrencias_producto.items():
            if max == item: 
                self.producto_popular = key 
                print(f"El producto más popular es {self.producto_popular}")
    
                
                
        
    def calcular_producto_impopular(self, nombres_productos):
        productos_vendidos = []
        productos_vendidos.append(self.venta.detalle_venta.producto)
        ocurrencias_producto = {}
        contador, min = 0
        for x in nombres_productos: 
            if x == nombres_productos[contador]:
                ocurrencias_producto[x] = productos_vendidos.count(x)
                contador += 1
                
        for values in ocurrencias_producto.values():
            if min < values:
                min = values
                
        for key, item in ocurrencias_producto.items():
            if max == item: 
                self.producto_popular = key 
                print(f"El producto impopular es {self.producto_popular}")
    
    def calcular_ingresos(self):
        self.ingresos += self.venta.total_venta
        
    
    def promedio_dinero_x_producto(self):
        self.promedio_dinero_x_producto = self.ingresos / self.venta.total_producto
        

def run(): 
    print('hELLO')

if __name__ == "__main__":
    run()