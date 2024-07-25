def notas(valores):
    resultado = dict()
    resultado['notas'] = valores[:]
    resultado['maior'] = max(valores)
    resultado['menor'] = min(valores)
    resultado['media'] = sum(valores) / len(valores)
    resultado['situacao'] = 'REPROVADO' if resultado['media'] < 6 else 'APROVADO'

    return resultado


print(notas([1, 2, 4, 5, 3, 2]))
