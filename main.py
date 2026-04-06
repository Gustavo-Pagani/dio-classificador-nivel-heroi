
while True:
    nome = input("Digite o nome do herói: ")
    
    try:
        xp = int(input("Digite a quantidade de XP: "))
    except ValueError:
        print(" Por favor, digite um número válido para XP.\n")
        continue

    if xp < 1000:
        nivel = "Ferro"
    elif xp <= 2000:
        nivel = "Bronze"
    elif xp <= 5000:
        nivel = "Prata"
    elif xp <= 7000:
        nivel = "Ouro"
    elif xp <= 8000:
        nivel = "Platina"
    elif xp <= 9000:
        nivel = "Ascendente"
    elif xp <= 10000:
        nivel = "Imortal"
    else:
        nivel = "Radiante"

    print(f"\n O Herói de nome {nome} está no nível de {nivel}\n")

    continuar = input("Deseja classificar outro herói? (s/n): ").lower()
    if continuar != 's':
        print("Encerrando o programa...")
        break