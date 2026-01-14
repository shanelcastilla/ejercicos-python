from dataclasses import dataclass, field
from datetime import datetime
from typing import List,Optional



@dataclass
class Product:
    id: int
    name : str
    category: str
    price: float
    stock: int
    date_the_product: datetime = field(default_factory=datetime.now)


    def __str__(self):
        return f"Product(id={self.id}, name={self.name}, category={self.category}, price={self.price}, stock={self.stock}, date_the_product={self.date_the_product})"

class Inventory:
    # base de datos 
    def __init__(self,listado : Optional[List[Product]] = None):
        self.listado = listado  if listado is not  None else []

    
    # agregar productos
    def agregar(self, esquema : Product):
        if any(a.id == esquema.id for a in self.listado):
            print ("Este producto con el ID ya existe")
            return
        
        self.listado.append(esquema)
        print("se agrego el producto")

    
    
    # mostrar producto
    def productos(self):
        if not self.listado:
            print("lista vacia")
            return
        
        mostrar = "\n LISTADO DE PRODUCTOS"

        for lista in self.listado:
            mostrar += f"""

ID : {lista.id}
NOMBRE : {lista.name}
CATEGORIA : {lista.category}
PRECIO : {lista.price}
STOCK : {lista.stock}
FECHA : {lista.date_the_product}
"""
            
        return mostrar
    
    def Actualizar_stock(self, id_producto: int, nuevo_stock: int):
        producto =  next((prod for prod in self.listado if prod.id == id_producto), None)

        if producto is None:
            print("ID no encontrado")  
            return
               
        producto.stock = int(nuevo_stock)
        producto.date_the_product = datetime.now()
        
        print("Stock actualizado correctamente")

    # actualizar todo el producto
    def Actualizar_producto(self, id_producto : int, esquema : Product):
        producto = next(prod for prod in self.listado if prod.id == id_producto)

        if producto is None:
            print("ID del producto no encontrado")
            return
        

        # se actualiza cada campo del `producto` con los valores del `esquema`
        producto.id = esquema.id
        producto.name = esquema.name
        producto.category = esquema.category
        producto.price = esquema.price
        producto.stock = esquema.stock       
        producto.date_the_product = datetime.now()
        print("se actualizo el producto")
        
    # eliminar producto completo
    def Eliminar_producto(self, id_producto: int):
        producto = next((prod for prod in self.listado if prod.id == id_producto), None)

        if producto is None:
            print("ID no encontrado")
            return
        
        self.listado.remove(producto)
        print("- se elimino correctamente -")






def main():
 lista = Inventory()
    
 while True:

    
    print("Bienvenido")
    print("1. mostrar Productos")
    print("2. insertar producto")
    print("3. actualizar STOCK")
    print("4. salir")
    print("5. eliminar producto")
    print("6. actualizar todo el producto")
    opciones = input("seleciona una de las opciones (1-5)😊:  ")

    match opciones:
        case "1":
            # mostrar
            print(lista.productos())

        case "2":
            # insertar
            try:
                id_producto = int(input("ID: "))
                nombre = input("Nombre: ")
                categoria = input("categoria: ")
                precio = float(input("Precio: "))
                Stock = int(input("stock: ")) 

                nueva = Product(
                   id=id_producto,
                   name=nombre,
                   category=categoria,
                   price=precio,
                   stock=Stock
                )

                lista.agregar(nueva)
            except ValueError as e:
                print(f"Error al insertar el dato ")

           

        case "3":
            # actualizar stock
            id_producto = int(input("ID del producto a actualizar: "))
            nuevo_stock = input("Nuevo stock: ")

            lista.Actualizar_stock(id_producto, nuevo_stock)
        case "4":
            print("Saliendo del programa...")
            break

        case "5":
            id_producto = int(input("ID del producto a eliminar:  "))
            lista.Eliminar_producto(id_producto)

        case "6":
            id_producto = int(input("ID del producto a eliminar:  "))

            nuevo_id_producto = int(input("ID: "))
            nuevo_nombre = input("Nombre: ")
            nuevo_categoria = input("categoria: ")
            nuevo_precio = float(input("Precio: "))
            nuevo_Stock = int(input("stock: ")) 
             
            actualizar = Product(
                id=nuevo_id_producto,
                name=nuevo_nombre,
                category=nuevo_categoria,
                price= nuevo_precio,
                stock=nuevo_Stock 
            )
            lista.Actualizar_producto(id_producto,actualizar)
            
            

        case _:
            print("Opcion no valida")



           

if __name__ == "__main__":
    main()









        
    
        
    
    











    



    




    


