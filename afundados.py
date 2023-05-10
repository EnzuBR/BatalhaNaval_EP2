def afundados(navios,tabuleiro):
    navio_afundado=0
    for tipos,posicoes in navios.items():
        for posicao in posicoes:
            contador=0
            for cordenada in posicao:
                if tabuleiro[cordenada[0]][cordenada[1]]=='X':
                    contador+=1
                    if tipos=='submarino':
                        navio_afundado+=1
                if contador==len(posicao) and tipos !='submarino':
                    navio_afundado+=1
    return navio_afundado
