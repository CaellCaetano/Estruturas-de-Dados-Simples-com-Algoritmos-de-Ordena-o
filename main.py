
# ==========================================
# TRABALHO - ESTRUTURAS DE DADOS E ORDENACAO
# ==========================================


# VARIAVEIS GLOBAIS

dados = []
MAX = 0

ponteiro = -1

spos = 0
rpos = 0

quantidade = 0

estrutura_ativa = None


# ==========================================
# FUNCAO PARA LER NUMEROS INTEIROS
# ==========================================

def ler_inteiro(mensagem):
    while True:
        try:
            return int(input(mensagem))
        except ValueError:
            print("Digite um numero inteiro valido!")


# ==========================================
# PILHA
# ==========================================

def inicializa_pilha():
    global dados, ponteiro, MAX, estrutura_ativa

    MAX = ler_inteiro("Digite o tamanho da pilha: ")

    if MAX <= 0:
        print("O tamanho deve ser maior que zero!")
        return

    dados = []
    ponteiro = -1
    estrutura_ativa = "pilha"

    print("\nPilha criada com sucesso!")


def push_pilha(valor):
    global dados, ponteiro, MAX

    if ponteiro == MAX - 1:
        print("\nPilha Cheia!!!")
        return

    dados.append(valor)
    ponteiro = ponteiro + 1

    print("\nValor armazenado com sucesso!")


def pop_pilha():
    global dados, ponteiro

    if ponteiro < 0:
        print("\nPilha Vazia!!!")
        return None

    valor = dados[ponteiro]
    del dados[ponteiro]
    ponteiro = ponteiro - 1

    return valor


def show_pilha():

    if ponteiro < 0:
        print("\nPilha Vazia!!!")
        return

    print("\nConteudo da pilha:", dados)


# ==========================================
# FILA
# ==========================================

def inicializa_fila():
    global dados, spos, rpos, MAX, estrutura_ativa

    MAX = ler_inteiro("Digite o tamanho da fila: ")

    if MAX <= 0:
        print("O tamanho deve ser maior que zero!")
        return

    dados = []
    spos = 0
    rpos = 0
    estrutura_ativa = "fila"

    print("\nFila criada com sucesso!")


def push_fila(valor):
    global dados, spos, MAX

    if spos == MAX:
        print("\nFila Cheia!!!")
        return

    dados.append(valor)
    spos = spos + 1

    print("\nValor armazenado com sucesso!")


def pop_fila():
    global dados, spos, rpos

    if rpos == spos:
        print("\nFila Vazia!!!")
        return None

    valor = dados[rpos]
    rpos = rpos + 1

    return valor


def show_fila():

    if rpos == spos:
        print("\nFila Vazia!!!")
        return

    print("\nConteudo da fila:")

    for i in range(rpos, spos):
        print(dados[i])


# ==========================================
# FILA CIRCULAR
# ==========================================

def inicializa_fila_circular():
    global dados, spos, rpos, MAX
    global quantidade, estrutura_ativa

    MAX = ler_inteiro("Digite o tamanho da fila circular: ")

    if MAX <= 0:
        print("O tamanho deve ser maior que zero!")
        return

    dados = [None] * MAX

    spos = 0
    rpos = 0
    quantidade = 0

    estrutura_ativa = "fila circular"

    print("\nFila circular criada com sucesso!")


def push_fila_circular(valor):
    global dados, spos, quantidade, MAX

    if quantidade == MAX:
        print("\nFila Circular Cheia!!!")
        return

    dados[spos] = valor

    spos = (spos + 1) % MAX
    quantidade = quantidade + 1

    print("\nValor armazenado com sucesso!")


def pop_fila_circular():
    global dados, rpos, quantidade, MAX

    if quantidade == 0:
        print("\nFila Circular Vazia!!!")
        return None

    valor = dados[rpos]

    dados[rpos] = None

    rpos = (rpos + 1) % MAX
    quantidade = quantidade - 1

    return valor


def show_fila_circular():

    if quantidade == 0:
        print("\nFila Circular Vazia!!!")
        return

    print("\nConteudo da fila circular:")

    for i in range(quantidade):
        posicao = (rpos + i) % MAX
        print(dados[posicao])


# ==========================================
# BUBBLE SORT
# ==========================================

def ordenacao_bolha(A):
    n = len(A)

    for i in range(n):
        for j in range(0, n - 1 - i):

            if A[j] > A[j + 1]:
                temp = A[j]
                A[j] = A[j + 1]
                A[j + 1] = temp


# ==========================================
# SELECTION SORT
# ==========================================

def ordenacao_selecao(A):
    n = len(A)

    for i in range(n):

        minimo = i

        for j in range(i + 1, n):

            if A[minimo] > A[j]:
                minimo = j

        A[i], A[minimo] = A[minimo], A[i]


# ==========================================
# INSERTION SORT
# ==========================================

def ordenacao_insercao(A):
    n = len(A)

    for j in range(1, n):

        chave = A[j]
        i = j - 1

        while i >= 0 and A[i] > chave:

            A[i + 1] = A[i]
            i = i - 1

        A[i + 1] = chave


# ==========================================
# IDENTIFICAR POSICOES DOS DADOS
# ==========================================

def obter_posicoes():

    if estrutura_ativa == "pilha":
        return list(range(len(dados)))

    elif estrutura_ativa == "fila":
        return list(range(rpos, spos))

    elif estrutura_ativa == "fila circular":

        posicoes = []

        for i in range(quantidade):
            posicao = (rpos + i) % MAX
            posicoes.append(posicao)

        return posicoes

    return []


# ==========================================
# APLICAR ORDENACAO
# ==========================================

def ordenar_estrutura(algoritmo):
    global dados

    if estrutura_ativa is None:
        print("\nCrie primeiro uma estrutura!")
        return

    posicoes = obter_posicoes()

    if len(posicoes) == 0:
        print("\nNao existem valores para ordenar!")
        return

    valores = []

    for posicao in posicoes:
        valores.append(dados[posicao])

    print("\nAntes da ordenacao:", valores)

    if algoritmo == 1:
        ordenacao_bolha(valores)
        nome = "Bubble Sort"

    elif algoritmo == 2:
        ordenacao_selecao(valores)
        nome = "Selection Sort"

    elif algoritmo == 3:
        ordenacao_insercao(valores)
        nome = "Insertion Sort"

    for i in range(len(posicoes)):
        dados[posicoes[i]] = valores[i]

    print("\nAlgoritmo utilizado:", nome)
    print("Depois da ordenacao:", valores)


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu_principal():

    while True:

        print("\n***********************************")
        print("| Estruturas de Dados e Ordenacao |")
        print("-----------------------------------")
        print("| 1 - PILHA                       |")
        print("| 2 - FILA                        |")
        print("| 3 - FILA CIRCULAR               |")
        print("| 4 - ORDENAR                     |")
        print("| 5 - SAIR                        |")
        print("-----------------------------------")

        opt1 = ler_inteiro("Digite a opcao desejada: ")

        if opt1 >= 1 and opt1 <= 5:
            return opt1

        print("Opcao inexistente!")


# ==========================================
# MENU DA PILHA
# ==========================================

def pilha():

    while True:

        print("\n-----------------------------------")
        print("| PILHA                           |")
        print("-----------------------------------")
        print("| 1 - Criar estrutura             |")
        print("| 2 - Armazenar valor             |")
        print("| 3 - Extrair valor               |")
        print("| 4 - Imprimir conteudo           |")
        print("| 5 - Voltar ao menu anterior     |")
        print("-----------------------------------")

        opt2 = ler_inteiro("Digite a opcao desejada: ")

        if opt2 == 1:
            inicializa_pilha()

        elif opt2 == 2:

            if estrutura_ativa != "pilha":
                print("Crie primeiro a pilha!")
            else:
                valor = ler_inteiro("Digite o valor: ")
                push_pilha(valor)

        elif opt2 == 3:

            if estrutura_ativa != "pilha":
                print("Crie primeiro a pilha!")
            else:
                valor = pop_pilha()

                if valor is not None:
                    print("Valor extraido:", valor)

        elif opt2 == 4:

            if estrutura_ativa != "pilha":
                print("Crie primeiro a pilha!")
            else:
                show_pilha()

        elif opt2 == 5:
            print("Voltando ao menu anterior...")
            break

        else:
            print("Opcao inexistente!")


# ==========================================
# MENU DA FILA
# ==========================================

def fila():

    while True:

        print("\n-----------------------------------")
        print("| FILA                            |")
        print("-----------------------------------")
        print("| 1 - Criar estrutura             |")
        print("| 2 - Armazenar valor             |")
        print("| 3 - Extrair valor               |")
        print("| 4 - Imprimir conteudo           |")
        print("| 5 - Voltar ao menu anterior     |")
        print("-----------------------------------")

        opt2 = ler_inteiro("Digite a opcao desejada: ")

        if opt2 == 1:
            inicializa_fila()

        elif opt2 == 2:

            if estrutura_ativa != "fila":
                print("Crie primeiro a fila!")
            else:
                valor = ler_inteiro("Digite o valor: ")
                push_fila(valor)

        elif opt2 == 3:

            if estrutura_ativa != "fila":
                print("Crie primeiro a fila!")
            else:
                valor = pop_fila()

                if valor is not None:
                    print("Valor extraido:", valor)

        elif opt2 == 4:

            if estrutura_ativa != "fila":
                print("Crie primeiro a fila!")
            else:
                show_fila()

        elif opt2 == 5:
            print("Voltando ao menu anterior...")
            break

        else:
            print("Opcao inexistente!")


# ==========================================
# MENU DA FILA CIRCULAR
# ==========================================

def fila_circular():

    while True:

        print("\n-----------------------------------")
        print("| FILA CIRCULAR                   |")
        print("-----------------------------------")
        print("| 1 - Criar estrutura             |")
        print("| 2 - Armazenar valor             |")
        print("| 3 - Extrair valor               |")
        print("| 4 - Imprimir conteudo           |")
        print("| 5 - Voltar ao menu anterior     |")
        print("-----------------------------------")

        opt2 = ler_inteiro("Digite a opcao desejada: ")

        if opt2 == 1:
            inicializa_fila_circular()

        elif opt2 == 2:

            if estrutura_ativa != "fila circular":
                print("Crie primeiro a fila circular!")
            else:
                valor = ler_inteiro("Digite o valor: ")
                push_fila_circular(valor)

        elif opt2 == 3:

            if estrutura_ativa != "fila circular":
                print("Crie primeiro a fila circular!")
            else:
                valor = pop_fila_circular()

                if valor is not None:
                    print("Valor extraido:", valor)

        elif opt2 == 4:

            if estrutura_ativa != "fila circular":
                print("Crie primeiro a fila circular!")
            else:
                show_fila_circular()

        elif opt2 == 5:
            print("Voltando ao menu anterior...")
            break

        else:
            print("Opcao inexistente!")


# ==========================================
# MENU DE ORDENACAO
# ==========================================

def ordenar():

    while True:

        print("\n-----------------------------------")
        print("| ORDENAR                         |")
        print("-----------------------------------")
        print("| 1 - Bubble Sort                 |")
        print("| 2 - Selection Sort              |")
        print("| 3 - Insertion Sort              |")
        print("| 4 - Voltar ao menu anterior     |")
        print("-----------------------------------")

        opt2 = ler_inteiro("Digite a opcao desejada: ")

        if opt2 == 1:
            ordenar_estrutura(1)

        elif opt2 == 2:
            ordenar_estrutura(2)

        elif opt2 == 3:
            ordenar_estrutura(3)

        elif opt2 == 4:
            print("Voltando ao menu anterior...")
            break

        else:
            print("Opcao inexistente!")


# ==========================================
# PROGRAMA PRINCIPAL
# ==========================================

while True:

    opt1 = menu_principal()

    if opt1 == 5:
        break

    elif opt1 == 1:
        pilha()

    elif opt1 == 2:
        fila()

    elif opt1 == 3:
        fila_circular()

    elif opt1 == 4:
        ordenar()

print("\nPrograma finalizado!")
