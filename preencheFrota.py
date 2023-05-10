def preenche_frota(frotas,navios,linha,coluna,orientacao,tamanho):
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
    lista_func=define_posicoes(linha,coluna,orientacao,tamanho)
    if navios not in frotas:
        frotas[navios]=[lista_func]
    else:
        frotas[navios]+=[lista_func]

    return frotas

    
