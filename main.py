def pedir_numero(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            return float(entrada)
        except ValueError:
            print("Entrada inválida. Digite um número.")


def main():
    numero1 = pedir_numero("Digite o primeiro número: ")
    numero2 = pedir_numero("Digite o segundo número: ")
    resultado = numero1 + numero2
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
