# Estudo sobre Dicionários {}
# Exemplo de uso:
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
#{'jack': 4098, 'sape': 4139, 'guido': 4127}
tel['jack']
#4098
# tel['irv'] -> ERROR
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#KeyError: 'irv'
print(tel.get('irv'))
#None
del tel['sape']
tel['irv'] = 4127
tel
#{'jack': 4098, 'guido': 4127, 'irv': 4127}
list(tel)
#['jack', 'guido', 'irv']
sorted(tel)
#['guido', 'irv', 'jack']
'guido' in tel
#True
'jack' not in tel
#False

print("--------------------------------------------------------")

# O construtor dict() produz dicionários diretamente de sequências de pares chave-valor:
dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])

print("--------------------------------------------------------")
# Exercício de fixação

vistorias = [
    {'local': 'Pampulha','data': '14/09/2026','pend': 5},
    {'local': 'Santa Tereza','data': '14/10/2026','pend': 4},
    {'local': 'Pompeia','data': '23/04/2026','pend': 2},
    {'local': 'Castelo','data': '08/09/2026','pend': 0},
    {'local': 'Pampulha','data': '14/04/2026','pend': 3}
    ]

# Minha solução
#for v in vistorias:
#    if v['pend'] > 2:
#        print(v)

# List Comprehension quais tem mais de 2 pendencias
criticas = [v for v in vistorias if v['pend'] > 2]
print(criticas)

# Soma das pendencias
soma = sum(v['pend'] for v in vistorias)
print(soma)

# Dicionário de quantas visotorias houve por local
contagem = {}
for v in vistorias:
    local = v['local']
    contagem[local] = contagem.get(local, 0) + 1

for local, qtd in contagem.items():
    print(f"{local}: {qtd} vistorias")

# Atalho Python da questão acima
print("--------------------------------------------------------")
from collections import Counter
Counter(v['local'] for v in vistorias)