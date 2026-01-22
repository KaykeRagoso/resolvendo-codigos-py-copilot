string = input("Digite a string: ")

numero_repeticoes = int(input("Digite o número de vezes para repetir a string: "))

if numero_repeticoes < 0:
    print("O número de repetições deve ser um inteiro não negativo.")
else:
    resultado = string * numero_repeticoes

    print("A string repetida", numero_repeticoes, "vezes é:", resultado)

    