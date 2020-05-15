from psycopg2 import connect, Error
from logger import escribir_al_log

class ConexionPG:

    db = None
    cursor = None

    def __init__(self, **parametros):
        try:
            self.db = connect(
                host=parametros['direccion_servidor'],
                user=parametros['usuario'],
                password=parametros['contrasena'],
                database=parametros['base_datos']
            )
            self.cursor = self.db.cursor()
        except Error as e:
            escribir_al_log(e, "Ocurrio un error al conectar a la base de datos")
        
    def _ejecutar_sql(
            self, sentencia_sql, parametros=None,
            escribir_en_bd=True
        ):
        try:
            self.cursor.execute(sentencia_sql, parametros)
            if escribir_en_bd:
                self.db.commit()
        except Exception as e:
            escribir_al_log(e, f"Ocurrio un error al ejecutar la sentencia SQL:\n\n{sentencia_sql}\n")
            if escribir_en_bd:
                self.db.rollback()

    def _leer_desde_sql(self):
        registros = []
        try:
            registros = self.cursor.fetchall()
        except Exception as e:
            escribir_al_log(e,f'Ocurrio un error al momento de leer desde la BD')
        return registros
    

    def insertar_productos(self, nombre, descripcion, precio, cantidad):
        self._ejecutar_sql(
            "INSERT INTO productos (nombre, descripcion, precio, cantidad) VALUES (%s, %s, %s, %s)",
            (nombre, descripcion, precio, cantidad )
        )

    def modificar_productos(self, nombre, descripcion, precio, cantidad, id_prod):
        self._ejecutar_sql(
            "update productos set nombre=%s, descripcion=%s, precio=%s, cantidad=%s where id_prod=%s ",
            (nombre, descripcion, precio, cantidad, id_prod)
        )

    def eliminar_productos(self, id_prod):
        self._ejecutar_sql(
            "DELETE FROM productos where id_prod =%s",
            (id_prod,)
        )
    def mostrar_factura(self):
        self._ejecutar_sql(
            "select * from factura"
        )