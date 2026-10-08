from vistorias import filtrar_criticas, total_pendencias, contar_por_local

vistorias = [
    {'local': 'Pampulha','data': '14/09/2026','pend': 5},
    {'local': 'Santa Tereza','data': '14/10/2026','pend': 4},
    {'local': 'Pompeia','data': '23/04/2026','pend': 2},
    {'local': 'Castelo','data': '08/09/2026','pend': 0},
    {'local': 'Pampulha','data': '14/04/2026','pend': 3}
    ]

print(filtrar_criticas(vistorias))
print(filtrar_criticas(vistorias, minimo=4))
print(total_pendencias(vistorias))

for local, qtd in contar_por_local(vistorias).items():
        print(f"{local}: {qtd} vistorias")