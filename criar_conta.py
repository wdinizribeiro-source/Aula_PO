from Cliente import Cliente

import pandas as pd
import os 
class criar_conta:
    def __init__(self,nome_cliente,CPF,tipo_conta,):
    #atributos
    # quais os atributos precisamos pra criar conta
    
        # instancia o cliente
        self.cliente = Cliente(nome_cliente,CPF,tipo_conta,)

    def salvar_excel(self, caminho_excel):
    
        novo_cliente = self.cliente.dicionario_cliente()
       
        excel = pd.DataFrame (novo_cliente)
        return excel 