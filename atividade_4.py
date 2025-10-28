# ============================================
# 🧮 Atividade Prática 04 – Aula 08
# ============================================

# ====== 1️⃣ CALCULADORA COM TRATAMENTO DE ERROS ======

def calculadora():
    print("\n=== Calculadora com Tratamento de Erros ===")

    while True:
        try:
            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            if operacao not in ['+', '-', '*', '/']:
                print("⚠️ Operação inválida! Tente novamente.\n")
                continue

            if operacao == '+':
                resultado = n1 + n2
            elif operacao == '-':
                resultado = n1 - n2
            elif operacao == '*':
                resultado = n1 * n2
            elif operacao == '/':
                if n2 == 0:
                    raise ZeroDivisionError
                resultado = n1 / n2

            print(f"\nResultado: {n1} {operacao} {n2} = {resultado}")
            print("✅ Operação concluída com sucesso!\n")
            break

        except ValueError:
            print("⚠️ Entrada inválida! Digite apenas números.\n")
        except ZeroDivisionError:
            print("❌ Erro: divisão por zero não é permitida.\n")


# ====== 2️⃣ REGISTRO DE NOTAS DA TURMA ======

def registrar_notas():
    print("\n=== Registro de Notas da Turma ===")
    notas = []

    while True:
        entrada = input("Digite uma nota (ou 'fim' para encerrar): ").lower()

        if entrada == 'fim':
            break

        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("⚠️ Nota inválida! Digite um valor entre 0 e 10.")
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número ou 'fim'.")

    if notas:
        media = sum(notas) / len(notas)
        print(f"\nMédia da turma: {media:.2f}\n")
    else:
        print("\nNenhuma nota válida foi inserida.\n")


# ====== 3️⃣ VERIFICADOR DE SENHA FORTE ======

def verificar_senha():
    print("\n=== Verificador de Senha Forte ===")
    while True:
        senha = input("Digite uma senha (ou 'sair' para encerrar): ")

        if senha.lower() == 'sair':
            print("Programa encerrado.\n")
            break

        if len(senha) < 8:
            print("⚠️ Senha fraca! Deve conter pelo menos 8 caracteres.\n")
            continue

        if not any(char.isdigit() for char in senha):
            print("⚠️ Senha fraca! Deve conter pelo menos um número.\n")
            continue

        print("✅ Senha forte! Registro concluído.\n")
        break


# ====== 4️⃣ VERIFICADOR DE NÚMEROS PARES E ÍMPARES ======

def verificar_par_ou_impar():
    print("\n=== Verificador de Números Pares e Ímpares ===")
    pares = 0
    impares = 0

    while True:
        entrada = input("Digite um número inteiro (ou 'fim' para encerrar): ").lower()

        if entrada == 'fim':
            break

        try:
            numero = int(entrada)
            if numero % 2 == 0:
                print(f"{numero} é PAR.\n")
                pares += 1
            else:
                print(f"{numero} é ÍMPAR.\n")
                impares += 1
        except ValueError:
            print("⚠️ Entrada inválida! Digite um número inteiro.\n")

    print(f"\nTotal de números pares: {pares}")
    print(f"Total de números ímpares: {impares}\n")


# ====== MENU PRINCIPAL ======

def menu():
    while True:
        print("===== MENU DE OPÇÕES =====")
        print("1 - Calculadora com Tratamento de Erros")
        print("2 - Registro de Notas da Turma")
        print("3 - Verificador de Senha Forte")
        print("4 - Verificador de Números Pares e Ímpares")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            calculadora()
        elif opcao == '2':
            registrar_notas()
        elif opcao == '3':
            verificar_senha()
        elif opcao == '4':
            verificar_par_ou_impar()
        elif opcao == '0':
            print("\nSaindo do programa... Até mais! 👋")
            break
        else:
            print("⚠️ Opção inválida! Escolha um número entre 0 e 4.\n")


# ====== EXECUÇÃO DO PROGRAMA ======
if __name__ == "__main__":
    menu()
