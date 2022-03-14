from datetime import date

def separador():
  print('*----------------------------------*')

class Cliente:
  def __init__(self,nombre,nif,direccion,cpostal,poblacion):
    self.nombre = nombre
    self.nif = nif
    self.direccion = direccion
    self.cpostal = cpostal
    self.poblacion = poblacion
  
  def getData(self,e):
    if(e == 'nombre'):
     return self.nombre
    if(e == 'nif'):
      return self.nif
    if(e == 'direccion'):
      return self.direccion
    if(e == 'cposal'):
      return self.cpostal
    if(e == 'poblacion'):
      return self.poblacion
    return 'error, faltan parametros'


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

  def getData(self,e):
    if(e == 'cantidad'):
     return self.cantidad
    if(e == 'denominación'):
      return self.denominacion
    if(e == 'preioUnidad'):
      return self.preioUnidad
    if(e == 'descuento'):
      return self.descuento
    return 'error, faltan parametros'

factura = input('Número de factura: ')
def main(factura,empresa,ciudad):
  print('Cliente: ')
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

  separador()
  print('Factura:')
  print('\nCliente: '+cliente.getData('nombre')+'\nNIF: '+cliente.getData('nif')+'\nDirección: '+cliente.getData('direccion')+'\nPoblacion: '+cliente.getData('cposal')+'\nPoblacion: '+cliente.getData('poblacion'))
  print('\nN  Quantitat Denominació Preu  Total€')

  pt = 0
  for i in range(len(arr)):
    q = int(arr[i].getData('cantidad'))
    p = int(arr[i].getData('preioUnidad'))
    d = int(arr[i].getData('descuento'))
    total = (q*p)-((q*p)*(d/100))
    pt += total
    print(str((i+1))+' '+arr[i].getData('cantidad')+' '+arr[i].getData('denominación')+' '+arr[i].getData('preioUnidad')+' '+arr[i].getData('descuento')+'% '+str(total)+'€')
  separador()
  today = date.today()
  print('EMPRESA: '+empresa+', Ciudad: '+ciudad+', Fecha:'+today.strftime("%m/%d/%y"))
  print('Num factura:'+str(factura))
  print('BASE IMPOSABLE: '+str(pt))
  print('IVA: '+str(pt*(int(iva)/100)))
  print('TOTAL:'+str((pt+(pt*(int(iva)/100)))))
  separador()
  if input('1 = Volver a introducir una factura, 2 = Salir: ') == '1':
    main(int(factura)+1,empresa,ciudad)




main(factura,input('Nombre empresa: '),input('Ciudad: '))