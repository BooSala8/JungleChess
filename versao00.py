"""
tabuleiro = ['__#&#__', '___#___', '_______', 
             '_~~_~~_', '_~~_~~_', '_~~_~~_'
             ,'_______','___#___','__#&#__'] #_ espaco, # trap, & casa, ~agua

#E elefante, L leão, T tigre, R rato, C cão, 🐆s leopardo, W lobo, G gato// jogador 1 peças, jogador 2 peças
peças = [[('E', (2, 6)), ('L', (0,0)), ('T', (0,6)), ('R', (2,0)), ('C', (1,1)), ('🐆', (2,2)), ('W', (2,4)), ('G', (1,5))] , 
          [('E', (6, 0)), ('L', (8,6)), ('T', (8,0)), ('R', (6,6)), ('C', (7,5)), ('🐆', (6,4)), ('W', (6,2)), ('G', (7,1))] ]

for i in range(len(tabuleiro)): #ver possibilidade de otimização
    for j in peças:
        for peça in j:
            if peça[1][0]==i:
                tabuleiro[i]=tabuleiro[i][0:peça[1][1]]+peça[0]+tabuleiro[i][peça[1][1]+1:]
    print(tabuleiro[i])
"""

ffrom colorama import Fore, Style, init

# Inicializa o colorama para compatibilidade no Windows
init(autoreset=True)

# Tabuleiro inicial
tabuleiro = [['_','_','#','&','#','_','_'],['_','_','_','#','_','_','_'],['_','_','_','_','_','_','_'], 
             ['_~~_~~_', '_~~_~~_', '_~~_~~_',
             '_______', '___#___', '__#&#__']  # _ espaço, # trap, & casa, ~ água

# Peças dos jogadores (1: amarelo, 2: roxo claro)
peças = [[('E', (2, 6)), ('L', (0, 0)), ('T', (0, 6)), ('R', (2, 0)), ('C', (1, 1)), ('🐆', (2, 2)), ('W', (2, 4)), ('G', (1, 5))], 
         [('E', (6, 0)), ('L', (8, 6)), ('T', (8, 0)), ('R', (6, 6)), ('C', (7, 5)), ('🐆', (6, 4)), ('W', (6, 2)), ('G', (7, 1))]]

# Cores
cor_jogador_1 = Fore.YELLOW
cor_jogador_2 = Fore.LIGHTMAGENTA_EX
cor_agua = Fore.LIGHTBLUE_EX
cor_trap = Fore.LIGHTRED_EX  # Castanho claro não existe no colorama, então usei vermelho claro
cor_casa = Fore.GREEN  # Verde para "&"

reset = Style.RESET_ALL

# Criando uma cópia do tabuleiro para modificação
tabuleiro_modificado = []

for i in range(len(tabuleiro)):  
    linha_modificada = list(tabuleiro[i])  # Transforma a linha em uma lista mutável
    
    # Colorir água, traps e casas antes de adicionar peças
    for j in range(len(linha_modificada)):
        if linha_modificada[j] == '~':
            linha_modificada[j] = f"{cor_agua}~{reset}"
        elif linha_modificada[j] == '#':
            linha_modificada[j] = f"{cor_trap}#{reset}"
        elif linha_modificada[j] == '&':
            linha_modificada[j] = f"{cor_casa}&{reset}"
    
    # Adicionar peças ao tabuleiro
    for idx, jogador in enumerate(peças):
        cor = cor_jogador_1 if idx == 0 else cor_jogador_2  # Define a cor baseada no jogador
        
        for peça in jogador:
            if peça[1][0] == i:  # Verifica se a peça está na linha atual
                linha_modificada[peça[1][1]] = f"{cor}{peça[0]}{reset}"  # Substitui pela peça colorida
    
    tabuleiro_modificado.append("".join(linha_modificada))  # Adiciona linha modificada ao tabuleiro final

# Exibir o tabuleiro formatado
for linha in tabuleiro_modificado:
    print(linha)
