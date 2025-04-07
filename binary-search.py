def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        # Log do passo atual
        print(f"Baixo: {baixo}, Alto: {alto}, Meio: {meio}, Chute: {chute}")

        if chute == item:
            print("Item encontrado!")
            return meio
        elif chute > item:
            print(f"{chute} é maior que {item}, procurando na metade esquerda.")
            alto = meio - 1
        else:
            print(f"{chute} é menor que {item}, procurando na metade direita.")
            baixo = meio + 1
    print("Item não encontrado.")
    return None

# Exemplo
minha_lista = [1, 3, 5, 7, 9]
print("\nResultado final:", pesquisa_binaria(minha_lista, 3))
