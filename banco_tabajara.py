from Cliente import Cliente
import pandas as pd
from criar_conta import criar_conta

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
    nome_cliente=input("Digite seu nome: ")
    CPF =str(input("Digite seu CPF: "))
    tipo_conta=input("Digite tipo de conta: ")

    if os.path.exists(caminho_excel): # true
        print("arquivo ja existe")
        df =pd.read_excel(caminho_excel)
    else:
        print("Arquivo não existe")
        df=pd.DataFrame()
        # instancio para manipular os dados adicionados
        conta = criar_conta(nome_cliente,CPF, tipo_conta)
        #identifico o caminho do excel e chamo gunção salvar
        novo_dado = conta.salvar_excel(caminho_excel)
    df.to_excel(caminho_excel, index = False)

elif opcao == 2:
    print("opção2 selecionada")


