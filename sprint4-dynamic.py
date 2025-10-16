import random
from collections import deque

# -------------------------
# SIMULAÇÃO DE DADOS
# -------------------------
insumos = ["Reagente A", "Reagente B", "Reagente C", "Descartável X", "Descartável Y", "Descartável Z"]

# Simular consumo diário (insumo, quantidade, validade em dias)
def gerar_consumo(qtd_dias=10):
    consumo = []
    for dia in range(1, qtd_dias+1):
        insumo = random.choice(insumos)
        quantidade = random.randint(1, 20)
        validade = random.randint(5, 30)  # em dias
        consumo.append({"dia": dia, "insumo": insumo, "quantidade": quantidade, "validade": validade})
    return consumo

consumo_diario = gerar_consumo()

# -------------------------
# FILA (ordem cronológica)
# -------------------------
fila_consumo = deque(consumo_diario)

# -------------------------
# PILHA (ordem inversa)
# -------------------------
pilha_consumo = list(consumo_diario)

# -------------------------
# BUSCAS
# -------------------------
def busca_sequencial(lista, nome_insumo):
    for item in lista:
        if item["insumo"] == nome_insumo:
            return item
    return None

def busca_binaria(lista, nome_insumo):
    lista_ordenada = sorted(lista, key=lambda x: x["insumo"])
    esquerda, direita = 0, len(lista_ordenada) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista_ordenada[meio]["insumo"] == nome_insumo:
            return lista_ordenada[meio]
        elif lista_ordenada[meio]["insumo"] < nome_insumo:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return None

# -------------------------
# ORDENAÇÃO
# -------------------------
def merge_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio], chave)
    direita = merge_sort(lista[meio:], chave)
    return merge(esquerda, direita, chave)

def merge(esquerda, direita, chave):
    resultado = []
    i = j = 0
    while i < len(esquerda) and j < len(direita):
        if esquerda[i][chave] <= direita[j][chave]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    return resultado

def quick_sort(lista, chave):
    if len(lista) <= 1:
        return lista
    pivo = lista[0]
    menores = [x for x in lista[1:] if x[chave] <= pivo[chave]]
    maiores = [x for x in lista[1:] if x[chave] > pivo[chave]]
    return quick_sort(menores, chave) + [pivo] + quick_sort(maiores, chave)

# -------------------------
# RELATÓRIO
# -------------------------
def relatorio():
    print("\n==== RELATÓRIO DO SISTEMA ====\n")
    print("1. FILA (ordem cronológica do consumo):")
    for item in fila_consumo:
        print(item)

    print("\n2. PILHA (últimos consumos primeiro):")
    for item in reversed(pilha_consumo):
        print(item)

    print("\n3. Busca Sequencial por 'Reagente B':")
    print(busca_sequencial(consumo_diario, "Reagente B"))

    print("\n4. Busca Binária por 'Descartável X':")
    print(busca_binaria(consumo_diario, "Descartável X"))

    print("\n5. Ordenação por quantidade (Merge Sort):")
    print(merge_sort(consumo_diario, "quantidade"))

    print("\n6. Ordenação por validade (Quick Sort):")
    print(quick_sort(consumo_diario, "validade"))

# Executar relatório
relatorio()
