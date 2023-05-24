from reportlab.lib.pagesizes import A4, letter
from reportlab.pdfgen import canvas
from datetime import date


class Tienda:
    def __init__(self, nombre, ruc, ubicacion):
        self.nombre= nombre
        self.ruc= ruc
        self.ubicacion= ubicacion
        
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.ruc} - {self.ubicacion}"


class Inventario:
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
        self.stock += int(input('Ingrese la cantidad de producto añadido'))
            
        
class Producto:
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
                    
                
class Tipo_producto:
    def __init__(self, id, tipo, impuesto):
        self.id = id
        self.tipo = tipo
        self.impuesto = impuesto
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.impuesto}"
   
    
    
class Cliente:
    def _init_ (self, id, nombre = 'Consumidor final', cedula = '999999999'):
        self.id=id
        self.nombre= nombre
        self.correo= cedula
        
    def __str__( self):
        return f"{self.id}- {self.nombre} - {self.cedula}"
                        
class Venta:
    def __init__(self,id, cliente, fecha):
        self.id=id
        self.cliente = cliente
        self.detalle_venta = []
        self.fecha=fecha
        self.total_venta= 0
        self.total_producto= 0
        
    def __str__(self):
        return f" {self.id} - {self.detalle} - {self.fecha} - {self.totalVenta}"
    
    def detallar_venta(self):
        cantidad_producto = int(input("Ingrese la cantidad de producto"))
        detalle = Detalle_venta(self.id, cantidad_producto)
        self.detalle.calcular_subtotal()
        self.detalle_venta.append(detalle)
    
    
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
    
class Detalle_venta:
    def __init__(self, id, producto, cantidad):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = 0
        
    def __str__(self):
        return f"{self.id} - {self.producto} - {self.cantidad} - {self.subtotal}"

    def calcular_subtotal(self):
        self.subtotal = (self.producto.precio+self.producto.precio.tipo_producto.impuesto)*self.cantidad
        
        
class Reporte_tienda: 
    def __init__(self, id, fecha):
        self.id = id
        self.fecha = fecha
        self.ingresos = 0
        self.ventas = {'cliente': [], 'productos': [], "valor_venta": []}
        
    def calcular_producto_popular(self, id):
        contador_ventas += 1
        opcion = int(input('Ingrese un opción:\n1:Consumidor final\n2:Factura con datos'))
        match opcion:
            case 1:
                cliente = Cliente(id)
            case 2:
                nombre = input('Ingrese el nombre del cliente')
                cedula = int(input('Ingrese el número de cédula del cliente')) 
                cliente = Cliente( id, nombre, cedula)  
        self.ventas['cliente'].append(cliente.nombre)              
        venta = Venta(id, cliente, date.today())
        tienda = Tienda("Todo Barato", 1520423, "Milagro")
        venta.imprimir_factura(tienda.nombre, tienda.ruc, tienda.ubicacion)
    
                
    def calcular__producto_impopular(self, nombres_productos):
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
    print('***Menú***\n1:Crear nuevo producto\n2:Visualizar un producto\n3:Modificar un producto\n4:Abastecer un producto\n5:Vender un producto \n6:Calcular estadistica de venta\n7:Salir')
    opcion = int(input('Eliga un opción'))
    contador_producto = 0
    productos_registrados = []
    ventas_registradas = []
    contador_ventas = 0
    bodega = []
    contador_clientes = 0
    clientes_registrados = []
    historial_reportes = []
    contador_reportes = 0
    
    match opcion:
        case 1: 
            contador_producto += 1
            nombre = input('Ingrese el nombre del producto')
            precio = int(input('Ingrese el precio del producto'))
            tipo = input('Ingrese el tipo del producto ingresado')
            impuesto = int(input('Ingrese el valor del impuesto'))
            tipo_producto = Tipo_producto(contador_producto, tipo, impuesto)
            producto = producto(contador_producto, nombre, precio,tipo_producto )
            productos_registrados.append(producto)
            stock = int(input('Ingrese el stock del producto'))
            min_stock = int(input("Ingrese la cantidad mínima para abastecer"))
            inventario = Inventario(contador_producto, stock, min_stock, producto)
            bodega.append(inventario)
        case 2:
            indice = int(input('Ingrese el id del producto a visualizar'))
            productos_registrados[indice-1].visualizar_producto()
        case 3:
            indice = int(input('Ingrese el id del producto a modificar'))
            productos_registrados[indice-1].modificar_producto()
        case 4: 
            indice = int(input('Ingrese el id del producto a abastecer'))
            bodega[indice-1].abastecer()
        case 5: 
            
        case 6:
            contador_reportes += 1
            reporte_tienda = Reporte_tienda(contador_reportes, date.today())
            opcion = int(input('Qué desee calcular: 1:Producto popular\n2:Producto impopular\n3:Ingresos\n4:Promedio dinero x producto'))
            match opcion:
                case 1:
                    reporte_tienda.calcular_producto_popular()
        case 7:
            exit()
            
                    

if __name__ == "__main__":
    run()