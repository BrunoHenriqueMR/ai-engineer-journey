import json
import dia03
import vistorias

# Treino Arquivos e JSON (API de LLM só chega em JSON)
with open("vistorias.json", "w", encoding="utf-8") as f:
    json.dump(dia03.vistorias, f, ensure_ascii=False, indent=2)

with open("vistorias.json", "r", encoding="utf-8") as f:
    dados = json.load(f)

print(dados)

print('-----------------------------------------------------------------')
print(vistorias.filtrar_criticas(dados, minimo=3))
print(vistorias.contar_por_local(dados))
print(vistorias.total_pendencias(dados))

# Os dados saíram do arquivo JSON e viraram lista de dicionários e usei nas funções que criei (Será o mesmo ciclo com as APIs de LLM)
