class inventario:
    def __init__(self, id, stock, min_stock):
        self.id = id
        self.stock = stock 
        self.min_stock = min_stock
        
    def __str__(self):
        return f"{self.id} - {self.stock} - {self.min_stock}"
    
class tienda:
    def __init__(self,id, nombre, ruc, ubicacion):
        self.id= id
        self.nombre= nombre
        self.ruc= ruc
        self.ubicacion= ubicacion
        
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.ruc} - {self.ubicacion}"


class cliente:
    def _init_ (self, id, nombre, correo):
        self.id=id
        self.nombre= nombre
        self.correo= correo
        
    def __str__( self):
        return f"{self.id}- {self.nombre} - {self.correo}"

class producto:
    def _init_(self, id , nombre, precio):
        self.id=id
        self.nombre= nombre
        self.correo= precio
        
    def __str__( self):
        return f"{self.id} - {self.nombre} - {self.coreo}"
    
    
class tipo_producto:
    def __init__(self, id, tipo, impuesto):
        self.id = id
        self.tipo = tipo
        self.impuesto = impuesto
    
    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.impuesto}"
                        
class venta:
    def __init__(self,id, detalle, fecha, total_venta, total_producto):
        self.id=id
        self.detalle=detalle
        self.fecha=fecha
        self.total_venta= total_venta
        self.total_producto= total_producto
        
    def __str__(self):
        return f" {self.id} - {self.detalle} - {self.fecha} - {self.totalVenta}"