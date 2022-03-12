from json.tool import main
import pandas as pd
import main
from datetime import datetime

database = main.database

xls = pd.read_excel("C:\\Users\\anton\\Downloads\\python-master (1)\\python-master\\DataPrueba.xlsx", "Datos")

for x in range(62385):
    database.insert_tc(xls['COD_SOCIO'][x], xls['NOMBRE'][x] +' '+ xls['APELLIDO1'][x] +' '+ xls['APELLIDO2'][x], xls['#_TC'][x], xls['FCH_CON'][x].strftime('%Y-%m-%d %H:%M:%S'), xls['MONTO'][x], xls['SALDO'][x])
