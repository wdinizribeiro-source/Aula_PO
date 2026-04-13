# evolução de um dicionario e criaaçao
# __init__ > criar um molde dos dados do cliente, objetivo é conseguir transferir dados por todos os arquivos python
class Cliente:
    def __init__(self,numero_conta,nome_cliente,CPF,tipo_conta,agencia,extrato_bancario):
        self.numero_conta = numero_conta
        self.nome_cliente=nome_cliente
        self.CPF=CPF
        self.tipo_conta=tipo_conta
        self.agencia=agencia
        self.extrato_bancario=extrato_bancario
    def __str__(self):
        return f"nome: {self.nome} |{self.numero_conta} | CPF: {self.CPF} | agencia: {self.agencia} | extratobancario: {self.extrato_bancario}"   