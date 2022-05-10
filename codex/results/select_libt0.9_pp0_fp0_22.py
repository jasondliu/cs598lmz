import selectData

print("Consulta pelo CEP")
print("Digite o CEP")
cep = input()
data = selectData.getDataByCEP(cep)
if data == []:
    print("CEP invalido")
else:
    print(data[0][0])
    print(data[0][4])
    print(data[0][5])

print("")
print("Consulta pelo Logradouro")
print("Digite o Logradouro")
logradouro = input()
data = selectData.getDataByLogradouro(logradouro)
if data == []:
    print("Logradouro invalido")
else:
    for row in data:
        print(row[0])
        print(row[4])
        print(row[5])
        print("------------------")
