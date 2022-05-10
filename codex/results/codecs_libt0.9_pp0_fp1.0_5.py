import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

lista_cidades=[]

for cidade in cidade_info.find():
    lista_cidades.append(cidade)

conn = psycopg2.connect(host="localhost",database="trabalho_python", user="postgres", password="123456")
selecionar = "INSERT INTO cidade (cid, geonameid, nome, pais) VALUES"
conn.autocommit = True
cursor = conn.cursor()

for cidades_pais in lista_cidades:
    insert_pais = selecionar + str((cidades_pais['_id'],cidades_pais['geoid'],cidades_pais['nome'],cidades_pais['pais']))
    cursor.execute(insert_pais)

for pais in lista_paises:
    insert_pais
