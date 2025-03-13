pip install dbfread pandas

from dbfread import DBF
import pandas as pd


# Cargar las tablas DBF en dataframes
tabla1 = pd.DataFrame(DBF("C:\\SISPER\\ingresos_concepto_2023.dbf", encoding="latin1"))
tabla2 = pd.DataFrame(DBF("C:\\SISPER\\202311-REMUNERACIONES-NORMAL_dattrab.dbf", encoding="latin1"))

#Cargar datos de las columnas de las tablas
print(tabla1.columns)
print(tabla2.columns)

# Unir las tablas en base al campo 'ID'
tabla_final = tabla1.merge(tabla2, on="TRABAJADOR", how="left")


# Guardar en Excel
tabla_final.to_excel("tabla_unificada.xlsx", index=False)

print(tabla_final.head())  # Ver las primeras filas
print(tabla_final.info())  # Ver tipos de datos y valores nulos

#------------------------------------------------------------------------------------------

pip install dbfread pandas openpyxl  # Agrega openpyxl para escribir en Excel

from dbfread import DBF
import pandas as pd

# Cargar las tablas DBF en dataframes
tabla1 = pd.DataFrame(DBF("C:\\SISPER\\ingresos_concepto_2023.dbf", encoding="latin1"))
tabla2 = pd.DataFrame(DBF("C:\\SISPER\\202311-REMUNERACIONES-NORMAL_dattrab.dbf", encoding="latin1"))

# Si hay problemas probar con encoding="utf-8" o encoding="cp1252"


# Verificar columnas disponibles
print("Columnas en tabla1:", tabla1.columns)
print("Columnas en tabla2:", tabla2.columns)

# Asegurar que no haya valores nulos en la columna clave
if tabla1["TRABAJADOR"].isnull().sum() > 0 or tabla2["TRABAJADOR"].isnull().sum() > 0:
    print("⚠️ Advertencia: Hay valores nulos en la clave de unión TRABAJADOR.")

# Unir las tablas en base al campo 'TRABAJADOR'
tabla_final = tabla1.merge(tabla2, on="TRABAJADOR", how="left")

# Guardar en Excel
tabla_final.to_excel("tabla_unificada.xlsx", index=False)

# Mostrar información de la tabla final
print(tabla_final.head())  
print(tabla_final.info()) 