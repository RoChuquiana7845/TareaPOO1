from datetime import date


class Inventario: 
    def __init__(self, id, stock, min_stock, producto):
        self.id = id
        self.stock = stock
        self.min_stock = min_stock
        self.producto = producto
    
    def __str__(self):
        return f"{self.id} - {self.stock} - {self.min_stock} - {self.producto}"
    
    def actualizar(self, productos_vendidos):
        self.stock -= productos_vendidos
    
    def abastecer(self, nuevo_stock):
        self.stock += nuevo_stock


class Producto: 
    def __init__(self, id, nombre, precio, tipo_producto):
        self.id = id
        self.nombre = nombre
        self.precio = precio
        self.tipo_producto = tipo_producto
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.precio} - {self.tipo_producto}"
    
    def modificar_producto(self, nombre = '', precio = 0, tipo =''):
        if nombre != '':
            self.nombre = nombre
        if precio != 0:
            self.precio = precio    
        if tipo != '':
            self.tipo_producto.tipo = tipo 
            self.tipo_producto.impuesto = int(input('Ingrese el impuesto del producto'))
        
        
class TipoProducto:
    def __init__(self, id, tipo, impuesto):
        self.id = id
        self.tipo = tipo
        self.impuesto = impuesto
        
    def __str__(self):
        return f"{self.id} - {self.tipo} - {self.impuesto}"
    


class Tienda:
    def __init__(self, nombre, ruc, direccion):
        self.nombre = nombre
        self.ruc = ruc
        self.direccion = direccion
    
    def __str__(self):
        return f"{self.nombre} - {self.ruc} - {self.direccion}"
    

class Venta:
    def __init__(self, id, cliente, fecha):
        self.id = id
        self.cliente = cliente
        self.fecha = fecha
        self.detalle_venta = []
        self.total_venta = 0
    
    def __str__(self):
        return f"{self.id} - {self.cliente} - {self.detalle_venta} - {self.fecha} - {self.total_venta}"
    
    def detallar_venta(self, producto, cantidad):
        detalle = DetalleVenta(self.id, producto, cantidad)
        self.detalle_venta.append(detalle)
        self.total_venta = detalle.subtotal + detalle.subtotal * detalle.producto.tipo_producto.impuesto
        
    def mostrar(self, nombre, ruc, direccion):
        print(f"Empresa: {nombre}\nRuc: {ruc}\nDirección: {direccion}")
        print(f"Número de venta: {self.id} fecha: {self.fecha} Cliente: {self.cliente.nombre} Total de venta: {self.total_venta}")


class DetalleVenta:
    def __init__(self, id, producto, cantidad):
        self.id = id
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad
    
    def __str__(self):
        return f"{self.id} - {self.producto} - {self.cantidad} - {self.subtotal}"
        

class EstadisticaTienda: 
    def __init__(self, id, fecha):
        self.id = id
        self.fecha = fecha
        self.prod_popular = ''
        self.prod_impopular = ''
        self.ingresos = 0
        self.prom_diner_prod = 0
    
    def __str__(self):
        return f"{self.id} - {self.fecha} - {self.prod_popular} - {self.prod_impopular} - {self.ingresos} - {self.prom_diner_prod}"

    def calcular_ingresos(self, *args):
        for n in args:
            self.ingresos += n
        print(f"Los ingresos de la tienda son {self.ingresos}")
    
    def determinar_prod_popular(self,**kargs):
        maxi = 0
        indice = 0
        for value in kargs.values():
            if maxi < value:
                maxi = value
                indice = list(kargs.values()).index(maxi)
        self.prod_popular = list(kargs.keys())[indice]
        print(f"El producto mas vendido es {self.prod_popular}")
             
    def determinar_prod_impopular(self, **kargs):
        mini = 0
        indice = 0
        for value in kargs.values():
            if mini > value:
                mini = value
                indice = list(kargs.values()).index(mini)
        self.prod_impopular = list(kargs.keys())[indice]
        print(f"El producto menos vendido es {self.prod_impopular}")
        
    def promedio(self, *args):
        suma = 0
        for num in args:
            suma += num
        print(f"El promedio de dinero por producto vendido es {self.ingresos/suma}")
        

class Cliente:
    def __init__(self, id, nombre, cedula):
        self.id = id
        self.nombre = nombre
        self.cedula = cedula 
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.cedula}"


#Crear un producto
#Supermercado
tipo1 = TipoProducto(1, "Supermercado", 0.04)
prod1 = Producto(1,"Pepsi", 0.50, tipo1)
#Visualizar un producto
print(prod1)
#Papelería
tipo2 = TipoProducto(2, 'Papelería', 0.16)
prod2 = Producto(2, "cuaderno", 1.20, tipo2)
#Visualizar un producto
print(prod2)
#Droguería
tipo3 = TipoProducto(3, 'Droguería', 0.12)
prod3 = Producto(3, 'Paracetamol', 7.50, tipo3)
#Visualizar un producto
print(prod3)


#Abastecer la tienda con un producto.
invetario1 = Inventario(1,150, 40, prod1)
invetario1.abastecer(120)
invetario2 = Inventario(2, 450, 100, prod2)
invetario2.abastecer(450)
invetario3 = Inventario(3, 784, 150, prod3)
invetario3.abastecer(561)


#Vender un producto
#Venta 1
tienda = Tienda('Barato o Nada', "1204512345", "AV. Narnia y Gandalf")
cliente1 = Cliente(1, 'Roberto', '1204578457')
venta1 = Venta(1, cliente1, date.today())
venta1.detallar_venta(prod1, 150)
#Mostrar venta
venta1.mostrar(tienda.nombre, tienda.ruc, tienda.direccion)
invetario1.actualizar(150)

#Venta 2
cliente2 = Cliente(2,'Alan Backer', '06457456120')
venta2 = Venta(2, cliente2, date.today())
venta2.detallar_venta(prod2, 451)
#Mostrar venta
venta2.mostrar(tienda.nombre, tienda.ruc, tienda.direccion)
invetario2.actualizar(451)

cliente3 = Cliente(3, 'Morocho', '45120784120')
venta3 = Venta(3, cliente3, date.today())
venta3.detallar_venta(prod3,  1200)
#Mostrar venta
venta3.mostrar(tienda.nombre, tienda.ruc, tienda.direccion)
invetario3.actualizar(120)

#Modificar un producto
prod1.modificar_producto(precio=0.55)
print(prod1)
prod2.modificar_producto(precio=1.70)
print(prod2)
prod3.modificar_producto(precio=8.90)
print(prod3)

#Estadisticas de venta
estadistica = EstadisticaTienda(1, date.today())
#Producto más vendido
estadistica.determinar_prod_popular(Pepsi = 150, Cuaderno= 451, Paracetamol=1200)
#Producto menos vendido
estadistica.determinar_prod_impopular(Pepsi = 150, Cuaderno= 451, Paracetamol=1200)
#Ingresos totales
estadistica.calcular_ingresos(venta1.total_venta, venta2.total_venta, venta3.total_venta) 
#Cantidad de dinero promedio obtenido por unidad de producto vendida
estadistica.promedio(venta1.detalle_venta[-1].cantidad, venta2.detalle_venta[-1].cantidad, venta3.detalle_venta[-1].cantidad)