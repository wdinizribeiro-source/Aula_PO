from Cliente import Cliente
import pandas as pd

class adicionar_conta:
    def __init__(self,nome_cliente,CPF,tipo_conta,):

    
        # criando cmolde de classe cliente pra manipular dados digitados
        self.cliente = Cliente(nome_cliente,CPF,tipo_conta,)

    def adicionar(self,caminho_excel):
        nova_linha = len(caminho_excel) # visão da nova linha
        ultima_linha = caminho_excel.iloc[-1]

        novo_cliente = self.cliente.dicionario_cliente()

        novo_cliente["numero_conta"] = ultima_linha["numero_conta"] + 1    
        novo_cliente["agencia"] = ultima_linha["agencia"] + 1   
        novo_dado = pd.DataFrame(novo_cliente)
        return novo_dado
