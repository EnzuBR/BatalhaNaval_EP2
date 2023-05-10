def posicao_valida(dic,linha,coluna,orientacao,tamanho):
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
    lista=define_posicoes(linha,coluna,orientacao,tamanho)
    for a in lista:
        if a[0]>9 or a[1]>9:
            return False
        for posicoes in dic.values():
            for posicao in posicoes:
                for cordenada in posicao:
                    if a==cordenada:
                        return False
    if dic=={}:
            return True
    return True
