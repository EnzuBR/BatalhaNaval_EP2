def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    lista.append([linha,coluna])
    if orientacao == 'vertical':
        for i in range(1,tamanho):
            linha+=1
            lista.append([linha,coluna])
    if orientacao == 'horizontal':
        for i in range(1,tamanho):
            coluna+=1
            lista.append([linha,coluna])
    return lista