from Cliente import Cliente
import pandas as pd
from criar_conta import criar_conta
from Adicionar_conta import adicionar_conta
from acessar_conta import acessar_conta
import os 

caminho_excel = "cliente_banco_tabajara.xlsx"

print("================================================")
print("        BEM - VINDO AO BANCO TABAJARA")
print("================================================\n")
print("1 > Criar conta")
print("2 > Acessar conta")

opcao = int(input("R: "))

if opcao == 1:
    print("opção 1 selecionada")
    nome_cliente = input("Digite seu nome: ")
    CPF = str(input("Digite seu CPF: "))
    tipo_conta = input("Digite tipo de conta: ")

    if os.path.exists(caminho_excel):
        print("Arquivo já existe")
        df = pd.read_excel(caminho_excel)

        adicionar = adicionar_conta(nome_cliente, CPF, tipo_conta)
        novo_dado = adicionar.adicionar(df)

        df = pd.concat([df, novo_dado], ignore_index=True)

    else:
        print("Arquivo não existe")

        conta = criar_conta(nome_cliente, CPF, tipo_conta)
        df = conta.salvar_excel(caminho_excel)

    # salva apenas uma vez
    df.to_excel(caminho_excel, index=False)

elif opcao == 2:
    print("Opção 2 selecionada")

    CPF = str(input("CPF: "))
    numero_conta = int(input("Digite o número da conta: "))

    acesso = acessar_conta(CPF, numero_conta)
    resultado =acesso.validar_banco(caminho_excel)

    if resultado == True
    print ("========================================\n")
    print (" Escolha as opções abixo \n")
    print (" 1  - Saque")
    print (" 2  - Deposito ")
    print (" 3  - Slado  ")
    print ("========================================\n")

    # crie uma classe pra saque com suas regras e validações
    # crie uma classe para depoisto
    # crie uma classe para saldo
    

else:
    print("Opção inválida!")