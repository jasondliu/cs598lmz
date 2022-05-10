import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)
print 'Ingrese el directorio de trabajo donde se encuentra la carpeta de datos'
wrkdir = raw_input()
gc.collect()
#wrkdir = 'e:/dispersao/dados_boa'
globalregr = re.compile('[0-9]{4,5}')
globalregr2 = re.compile('[a-zA-Z]+\s*[a-zA-Z]*\,\s*[a-zA-Z]*')

'''
m3 = glob.glob(wrkdir+'\\materia3_*.txt')
m3l = [i.replace('\\','/') for i in m3]

m3 = open('materia3.csv','w')
m3.writelines(';'.join(['nome','id','turma','tipo','disciplina','data/hora','valor\n']))
for file in m3l:

