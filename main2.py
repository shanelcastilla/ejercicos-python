# Gestionar productos, órdenes de compra y cálculo de totales.

from dataclasses import dataclass, field
from datetime import datetime
from typing import List,Optional


# producto
@dataclass
class Schema_producto:
    id: int
    name: str
    price: float
    stoke: int
    


    def __str__(self):
        return f"Product( id:{self.id}, name:{self.name}, price:{self.price}, stoke:{self.stoke},)"



# orden
@dataclass   
class schema_orden():
    id: int
    list_product: List[Schema_producto] = field(default_factory=list)
    fecha: datetime = field(default_factory=datetime.now)
    total: int = 0
 


    def __str__(self):
        return f"Orden( id:{self.id}, Lista_producto:{self.list_product}, fecha:{self.fecha},)"
    




    
class Inventario:
    # database liata
    def __init__(self, lista: Optional[List[Schema_producto]] = None ):
        self.lista = lista if lista is not None else []


    # agregar una orden

    def Agregar_producto(self, esquema : Schema_producto):
        if any(prod.id == esquema.id for prod in self.lista):
            print("orden ya estaba agregado.")
            return

        self.lista.append(esquema)
        print("se agrego el producto.")


    # mostrar orden
    def Mostrar(self):
        if not self.lista:
            print("vacia")

        mostrar = "\n LISTADO DE PRODUCTOS"

        for lista in self.lista:
            mostrar += f"""

id : {lista.id},
NOMBRE : {lista.name},
PRICE : {lista.price},
STOK : {lista.stoke},
"""
        return mostrar
    

    # buscar
    def buscar_producto(self, id_producto: int) -> Optional[Schema_producto]:
        return next((p for p in self.lista if p.id == id_producto), None)


        

class OrdenService:
    def __init__(self, inventario: Inventario):
        self.inventario = inventario


    def crear_orden(self,id_orden: int) -> schema_orden:
            return schema_orden(id=id_orden)
        

    def agregar_orden(self,orden: schema_orden,id_product: int,cantidad:int):

        producto = self.inventario.buscar_producto(id_product)

        if not producto:
            raise ValueError("producto no encontrado")

        
        if producto.stoke < cantidad:
            raise ValueError("stoke insuficiente")

        producto_orden = Schema_producto(
            id=producto.id,
            name=producto.name,
            price=producto.price,
            stoke=cantidad
            
        )

        orden.list_product.append(producto_orden)
        orden.total += producto.price * cantidad
        producto.stoke -= cantidad


    def mostrar_orden(self,orden : schema_orden):
        if not orden:
            print("no orden creada.")

        if not orden.list_product:
            print("no hay una orde agregada")


        print("\n====== ORDEN ======")
        print(f"orden: {orden.id}")
        print(f"fecha: {orden.fecha}") 
        print("----------------------------")


        for prod in orden.list_product:
             print(
            f"ID: {prod.id} | "
            f"NOMBRE: {prod.name} | "
            f"PRECIO: {prod.price} | "
            f"CANTIDAD: {prod.stoke} | "
            f"SUBTOTAL: {prod.price * prod.stoke}"
        )
             


        print("-------------------")
        print(f"TOTAL: {orden.total}")
        print("===================\n")



        
        
        

def main2():
  lista = Inventario()
  order_server = OrdenService(lista)
  orden_actual = None


  while True:

    print("Seleciona una de las siguientes opciones")
    print("1. Agregar un producto")
    print("2. mostrar prodcutos")
    print("3. craer orden")
    print("4. agregar una orden")
    print("5. mostrar orden")
    print("6. salir")
    
    opciones = input("seleciona una de las opciones disponibles: ")


# produto insertar y mostrar
    match opciones:
        case "1":
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                precio = float(input("Precio: "))
                Stock = int(input("stock: ")) 


                nuevo = Schema_producto(
                    id=id_producto,
                    name=nombre,
                    price=precio,
                    stoke=Stock
                )

                lista.Agregar_producto(nuevo)
                

            
                
        case "2":
            print(lista.Mostrar())

        case "3":
            agregar_orden = input("agregar orden: ")
            orden_actual =  order_server.crear_orden(agregar_orden)
            print("se agrego la orden")

        case "4":
            if not orden_actual:
                print("debe agregar una orden primero")
            

            id_produ = int(input("ID: "))
            cantidad_produt = int(input("cantidad: "))


            order_server.agregar_orden(orden_actual,id_produ,cantidad_produt)
            print("se agrego la orden ")


        case "5":
            if not orden_actual:
                print("no hay una orden")


            order_server.mostrar_orden(orden_actual)

        case "6":
            break
    

      




if __name__ == "__main__":
    main2()

    




    





