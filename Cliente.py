# evolução de um dicionario e criaaçao
# __init__ > criar um molde dos dados do cliente, objetivo é conseguir transferir dados por todos os arquivos python
class Cliente:
    def __init__(self,nome_cliente,CPF,tipo_conta,numero_conta=0,agencia=400,extrato_bancario=0):
        self.nome_cliente=nome_cliente
        self.CPF=CPF
        self.tipo_conta=tipo_conta
        self.numero_conta = numero_conta
        self.agencia=agencia
        self.extrato_bancario=extrato_bancario
    def __str__(self):
        return f"nome: {self.nome_cliente} |{self.numero_conta} | CPF: {self.CPF} | agencia: {self.agencia} | extratobancario: {self.extrato_bancario}"   
    
    # metodo
    def dicionario_cliente(self):
        return{chave:[valor]for chave, valor in self.__dict__.items()}