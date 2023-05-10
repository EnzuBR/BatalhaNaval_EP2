import random

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

frota_oponente = {
    'porta-aviões': [
        [[9, 1], [9, 2], [9, 3], [9, 4]]
    ],
    'navio-tanque': [
        [[6, 0], [6, 1], [6, 2]],
        [[4, 3], [5, 3], [6, 3]]
    ],
    'contratorpedeiro': [
        [[1, 6], [1, 7]],
        [[0, 5], [1, 5]],
        [[3, 6], [3, 7]]
    ],
    'submarino': [
        [[2, 7]],
        [[0, 6]],
        [[9, 7]],
        [[7, 6]]
    ]
}
frota_jogador = frotas

tabuleiro_oponente = posiciona_frota(frota_oponente)

tabuleiro_jogador = posiciona_frota(frota_jogador)

jogando = True

def monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente):
    texto = ''
    texto += '   0  1  2  3  4  5  6  7  8  9         0  1  2  3  4  5  6  7  8  9\n'
    texto += '_______________________________      _______________________________\n'

    for linha in range(len(tabuleiro_jogador)):
        jogador_info = '  '.join([str(item) for item in tabuleiro_jogador[linha]])
        oponente_info = '  '.join([info if str(info) in 'X-' else '0' for info in tabuleiro_oponente[linha]])
        texto += f'{linha}| {jogador_info}|     {linha}| {oponente_info}|\n'
    return texto

pos_atacadas = []

while jogando == True:
    print(monta_tabuleiros(tabuleiro_jogador, tabuleiro_oponente))
    atq_valido = False
    while not atq_valido:

        l_valida = False
        c_valida = False
        while not l_valida:
            l_ataque = int(input('Jogador, qual linha deseja atacar?'))
            if l_ataque >= 0 and l_ataque <= 9:
                l_valida = True
            else:
                print('Linha inválida!')
        
        while not c_valida:
            c_ataque = int(input('Jogador, qual coluna deseja atacar?'))
            if c_ataque >= 0 and c_ataque <= 9:
                c_valida = True
            else:
                print('Coluna inválida!')

        lc_ataque = [l_ataque,c_ataque]
        if lc_ataque not in pos_atacadas:
            atq_valido = True
        else:
            print('A posição linha {0} e coluna {1} já foi informada anteriormente!'.format(l_ataque,c_ataque))

    pos_atacadas.append([l_ataque,c_ataque])
    tabuleiro_oponente = faz_jogada(tabuleiro_oponente,l_ataque,c_ataque)
    n_afundados = afundados(frota_oponente,tabuleiro_oponente)
    if n_afundados == 10:
        print('Parabéns! Você derrubou todos os navios do seu oponente!')
        jogando = False
    if jogando:
        atq_op_valido = False
        pos_op_atacadas = []
        while not atq_op_valido:
            l_op_ataque = random.randint(0,9)
            c_op_ataque = random.randint(0,9)
            if [l_op_ataque,c_op_ataque] not in pos_op_atacadas:
                atq_op_valido = True
        pos_op_atacadas.append([l_op_ataque,c_op_ataque])
        print('Seu oponente está atacando na linha {0} e coluna {1}'.format(l_op_ataque,c_op_ataque))
        tabuleiro_jogador = faz_jogada(tabuleiro_jogador,l_op_ataque,c_op_ataque)
        n_op_afundados = afundados(frota_jogador,tabuleiro_jogador)
        if n_op_afundados == 10:
            print('Xi! O oponente derrubou toda a sua frota =(')
            jogando = False