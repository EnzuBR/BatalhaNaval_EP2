def define_posicoes(linha, coluna, orientacao, tamanho):
    lista = []
    lista.append([linha,coluna])
    if orientacao == 1:
        orientacao = 'vertical'
    if orientacao == 2:
        orientacao = 'horizontal'
    if orientacao == 'vertical':
        for i in range(1,tamanho):
            linha+=1
            lista.append([linha,coluna])
    if orientacao == 'horizontal':
        for i in range(1,tamanho):
            coluna+=1
            lista.append([linha,coluna])
    return lista

def preenche_frota(frotas,navios,linha,coluna,orientacao,tamanho):
    lista_func=define_posicoes(linha,coluna,orientacao,tamanho)
    if navios not in frotas:
        frotas[navios]=[lista_func]
    else:
        frotas[navios]+=[lista_func]

    return frotas

def faz_jogada(tabuleiro,linha,coluna):
    if tabuleiro[linha][coluna]==1:
        tabuleiro[linha][coluna]='X'
    else:
        tabuleiro[linha][coluna]='-'
    return tabuleiro

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

def posicao_valida(dic,linha,coluna,orientacao,tamanho):
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

def posicionando_frota(frotas,tam,nome):
    print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome,tam))
    linha = int(input('Linha:'))
    coluna = int(input('Coluna:'))
    orientacao = 1
    if tam > 1:
        orientacao = int(input('[1] Vertical [2] Horizontal >'))
    valido = posicao_valida(frotas,linha,coluna,orientacao,tam)
    while not valido:
        print('Esta posição não está válida!')
        print('Insira as informações referentes ao navio {0} que possui tamanho {1}'.format(nome,tam))
        linha = int(input('Linha:'))
        coluna = int(input('Coluna:'))
        orientacao = 1
        if tam > 1:
            orientacao = int(input('[1] Vertical [2] Horizontal >'))
        valido = posicao_valida(frotas,linha,coluna,orientacao,tam)
    return preenche_frota(frotas,nome,linha,coluna,orientacao,tam)

frotas = {}

for i in range(1):
    frotas = posicionando_frota(frotas,4,'porta-aviões')

for i in range(2):
    frotas = posicionando_frota(frotas,3,'navio-tanque')

for i in range(3):
    frotas = posicionando_frota(frotas,2,'contratorpedeiro')

for i in range(4):
    frotas = posicionando_frota(frotas,1,'submarino')