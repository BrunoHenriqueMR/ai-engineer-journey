def filtrar_criticas(vistorias, minimo=2):
    criticas = [v for v in vistorias if v['pend'] > minimo]
    return(criticas)

def total_pendencias(vistorias):
    soma = sum(v['pend'] for v in vistorias)
    return(soma)

def contar_por_local(vistorias):
    contagem = {}
    for v in vistorias:
        local = v['local']
        contagem[local] = contagem.get(local, 0) + 1
    return contagem