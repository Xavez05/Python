import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            db = 'laraveldb'
        )

        self.cursor = self.connection.cursor()

        print('Conexion exitosa')

    def insert_tc(self, cod_socio, nombre, no_tc, fecha, monto, saldo):
        sql = "INSERT INTO laraveldb.tarjeta_creditos (cod_socio, nombre, no_tc, fecha_emision, monto, saldo) VALUES ({}, '{}', '{}', '{}', {}, {})".format(cod_socio, nombre, no_tc, fecha, monto, saldo)

        try:
            print(sql)
            self.cursor.execute(sql)
            self.cursor.connection.commit()
        except Exception as e:
            raise

database = DataBase()
