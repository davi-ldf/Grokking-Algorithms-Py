def buscaMenor(arr):
    # Inicializa 'menor' com o primeiro elemento do array
    menor = arr[0]
    # Inicializa 'menor_indice' com 0 (posição do menor até agora)
    menor_indice = 0
    # Percorre os índices de 1 até o final do array
    for i in range(1, len(arr)):
        # Se o elemento atual for menor que o menor conhecido
        if arr[i] < menor:
            # Atualiza o valor de 'menor'
            menor = arr[i]
            # Atualiza o índice do menor elemento
            menor_indice = i
    # Retorna o índice do menor elemento encontrado
    return menor_indice


def ordenacaoPorSelecao(arr):
    # Cria um array novo para armazenar os elementos ordenados
    novoArr = []
    # Laço que roda N vezes, onde N é o tamanho inicial de 'arr'
    for i in range(len(arr)):
        # Encontra o índice do menor elemento do array restante
        menor = buscaMenor(arr)
        # Remove o menor de 'arr' e adiciona ao final de 'novoArr'
        novoArr.append(arr.pop(menor))
    # Retorna o array totalmente ordenado
    return novoArr


# Exemplo de uso: imprime [2, 3, 5, 6, 10]
print(ordenacaoPorSelecao([5, 3, 6, 2, 10]))
