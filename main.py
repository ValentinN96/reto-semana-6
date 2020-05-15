from conexion import ConexionPG


def main():
    
    conexion_pg = ConexionPG(
        direccion_servidor='127.0.0.1',  # localhost
        usuario='postgres',
        contrasena='passwod',
        base_datos='dbfactura'
    )
    print("\n\t\t\t<<<<< ¡Bienvenido a Minimarket Donnas! >>>>>>>\n")
    opc = True
    while opc == True:
        print("Ingrese los productosa comprar:\n ")
        nombre = input("Nombre: ")
        descripcion = input('Descripcion: ')
        precio = input('Precio: ')
        cantidad = input('Cantidad: ')
        id_prod = input('Ingrese el id del producto a modificar')
        #conexion_pg.insertar_productos( 
        #    nombre, descripcion, precio, cantidad    
        #)
        conexion_pg.modificar_productos(
            nombre, descripcion, precio, cantidad, id_prod
        )
        opc = input('Desea continuar s/n: ').lower() == 's'


    

main()
