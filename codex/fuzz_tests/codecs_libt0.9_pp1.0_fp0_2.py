import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Constantes
#Conexion = pyodbc.connect('DRIVER={SQL Server};SERVER=S00469-PC2019\SQLEXPRESS;DATABASE=DB_Auto;Trusted_Connection=yes;')

# Promedio maximo y minimo de la variable a monitorear
#promedioMaximo3 = 7000
#promedioMaximo2 = 5000
#promedioMinimo3 = 3000
#promedioMinimo2 = 1500

consumoActual = 0
consumoAnterior = list()

#Lectura de datos del arreglo
# Consulta SQL
#Fecha = time.strftime("%c")
fechaActual  = time.strftime("%c")
horaActual = time.strftime("%H")
minActual = time.strftime("%M")
diaActual = time.strftime("%A")
total = 0
for i
