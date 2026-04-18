import pandas as pd
from Cliente import Cliente
 
class acessar_conta:
    def __init__(self, CPF, numero_conta):
        self.cliente = Cliente(nome_cliente="",CPF=CPF,tipo_conta="",numero_conta=numero_conta,agencia=400,extrato_bancario=0)
        # nome_cliente, cpf, tipo_conta, numero_conta=0, agencia=400, extrato_bancario=0
 
    # Metodo
    def validar_banco(self, caminho_excel):
        df = pd.read_excel(caminho_excel)
 
        cliente_encontrado = df[
            (df["CPF"].astype(str)         == str(self.cliente.CPF)) &
            (df["numero_conta"].astype(str) == str(self.cliente.numero_conta))
        ]
 
        # Se o cliente for encontrado então mostrar a mensagem Bem-vindo e trazer os dados solicitados
        if not cliente_encontrado.empty:
            nome = cliente_encontrado.iloc[0]["nome_cliente"]
            print(f"Olá {nome} bem-vindo ao banco Tabajara")
            return True
        else:
            print("Usuário não encontrado, tentar novamente ou realizar o cadastro")
            return False
 