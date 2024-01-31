from Conta import Conta


class Corrente(Conta):
    def __init__(self, numero_da_conta, titular, saldo, tx_manutencao, limite):
        super().__init__(numero_da_conta, titular, saldo)
        self.tx_manutencao = tx_manutencao
        self.limite = limite

    def aumento_de_limite(self):
        if self.saldo >= 100:
            self.limite += 50
        else:
            pass


teste_conta = Corrente(123123, 'Rauã', 99, 0, 0)
teste_conta.aumento_de_limite()
print(teste_conta.limite)
