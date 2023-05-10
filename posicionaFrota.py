def posiciona_frota(navios):
    tabuleiro = []

    for i in range(10):
        linha = []
        for j in range(10):
            linha.append(0)
        tabuleiro.append(linha)

    for posicoes in navios.values():
        for posicao in posicoes:
            for cordenada in posicao:
                tabuleiro[cordenada[0]][cordenada[1]]=1
    return tabuleiro
