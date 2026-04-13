from Cliente import Cliente

import pandas as pd
import os 
class criar_conta:
    def __init__(self,nome_cliente,CPF,tipo_conta):
    #atributos
    # quais os atributos precisamos pra criar conta
        numero_conta = 0
        agencia = 400
        extrato_bancario = 0
        # instancia o cliente
        self.cliente = Cliente(nome_cliente,CPF, tipo_conta, numero_conta,agencia,extrato_bancario)

    def salvar_excel(self, caminho_excel):
    
        novo_cliente = {
        "numero_conta": [self.cliente.numero_conta],
        "nome": [self.cliente.nome_cliente],
        "CPF": [self.cliente.CPF],
        "Tipo_conta": [self.cliente.tipo_conta],
        "agencia": [self.cliente.agencia],
        "extrato": [self.cliente.extrato_bancario],
        }

        excel = pd.DataFrame (novo_cliente)
        return excel 