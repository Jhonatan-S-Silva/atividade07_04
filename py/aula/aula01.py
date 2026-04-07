#arrays & listas
''''
numeros = [1,2,3,4,5,]
txt = ["ooi", "tchau", "feliz natal"]
booleans = [ True, False]
variadas = [[1,2,3],["oi" , "tuduu bom"], [True , False]]
lista_geral = [numeros, textos, booleanos, variada, lista]
'''
'''sequencia = 1
total = 0

ala_fusca = [309,310,311,312,313,314,315,316,317,318,319,320,321,]

for quarto in ala_fusca:
    print(f"quarto n -   {quarto}")

alas_residencial_masculino = ['Fusca', 'maclaren', 'ferrari', 'BMW', 'porshe', 'kombi', 'lamborghini', 'audi', ' Maverick']
alas_residencial_feminino = ['tulipa','lirio','jasmim','rosa','popular','','','','',]

for ala in alas_residencial_feminino:
    print("residenciais feminino")
    print(f'ala: {ala}')

for ala in alas_residencial_masculino:
    print("residenciais masculino")
    print(f'ala {ala}')

lista_numeros = [1,2,3,4,5]

sequencia_numero = 1
for numero in lista_numeros:
    print('sequencia n: [{sequencia_numeros}]')
    sequencia_numero = sequencia_numero + 1


minha_lista = []
minha_lista.append('carrinho')
minha_lista.append('noix')

minha_lista.extend('!','meus ovos')
print(minha_lista)
'''

carrinho = []
print(carrinho)

for i in range(0, 6):
    produto =  input("adicione um item atravez do nome: ")
    carrinho.append(produto)

print(carrinho)

#carrinho.pop()
print(carrinho)

indice_arroz = carrinho.find('arroz')
print(f'indice do arroz: ')
