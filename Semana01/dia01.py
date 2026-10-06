v1 = 100

# Exemplo de if no python
if 101 < v1:
    print("Está dentro.")
else:
    print("Está fora!")

print("-----------------------------------------------------")
# Exemplo de for no python
palavras = ["Cachorro", "Gato", "Dinamo"]
for i in palavras:
    print(i, len(i))

print("-----------------------------------------------------")
# Exemplo de for + len (contador)
a = ["Bruno","Lorrayne", "Atenas", "Lancer"]
for n in range(len(a)):
    print(n, a[n])

# Exemplo de while no python
print("-----------------------------------------------------")
# Sequência de Fibonacci:
# a soma de dois elementos define a próxima
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# Definindo funções
print("-----------------------------------------------------")
def fib(n): # escreve série de Fibonacci menor que n
    """Imprime uma série de Fibonacci menor que n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Agora chamamos a função que acabamos de definir:
fib(2000)