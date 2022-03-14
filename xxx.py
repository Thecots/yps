def separador():
  print('*----------------------------------*')

class Cliente:
  def __init__(self,nombre,nif,direccion,cpostal,poblacion):
    self.nombre = nombre
    self.nif = nif
    self.direccion = direccion
    self.cpostal = cpostal
    self.poblacion = poblacion
  
  def getData(self):
    return self.nombre+' '+self.nif+' '+self.direccion+' '+self.cpostal+' '+self.poblacion


class Producto:
  def __init__(self,cantidad,denominacion,preioUnidad, descuento):
    self.cantidad = cantidad
    self.denominacion = denominacion
    self.preioUnidad = preioUnidad
    self.descuento = descuento
  
  def getProducts(self):
    return 'Cantidad: '+self.cantidad+'. Denominación: '+self.denominacion+'. Precio/u'+self.preioUnidad

  def setDescuento(self,e):
    self.descuento = e

  def getDescuento(self):
    return self.descuento

def main():
  factura = input('Número de factura: ')
  cliente = Cliente(input('Nombre: '),input('NIF: '),input('Dirección: '),input('Código postal: '),input('Población: '))

  arr = []
  b = 0
  while b == 0:
    separador()
    print('Añadir produto:')
    arr.append(Producto(input('Cantidad: '),input('Denominación: '),input('Precio/u: '),None))
    print('Producto añadido correctamente')
    separador()
    opt = input('1 = añadir otro producto\n2 = Terminar\n:')
    if opt != '1':
      b = 1
    

  for i in range(len(arr)):
    separador()
    print('Producto '+str(i+1)+' - '+arr[i].getProducts())
    arr[i].setDescuento(input('Descuento: '))
    separador()

  iva = input('IVA: ')

main()