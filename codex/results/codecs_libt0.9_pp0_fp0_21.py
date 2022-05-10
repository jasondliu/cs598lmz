import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

# Parsear argumentos de linea de comando
parser = argparse.ArgumentParser(description='Utilidades de Etiquetado')
parser.add_argument('-ob', '--obtener', dest='obtener', type=lambda x: (str(x).lower() == 'true'),help='Obtener datos', required=True)
parser.add_argument('-g', '--guardar', dest='guardar', type=lambda x: (str(x).lower() == 'true'),help='Guardar datos', required=False)
parser.add_argument('-d', '--data', dest='data',help='Tipo de dato', required=False)
parser.add_argument('-f', '--fecha', dest='fechaDesde',help='Fecha Desde', required=False)
parser.add_argument('-t', '--to', dest='fechaHasta',help='Fecha Hasta
