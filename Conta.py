"""-A classe base Conta deve ter atributos para o número da conta, o titular da conta e o saldo.

-Ela deve incluir métodos para depósitos, saques e exibição do saldo
atual. Classe Conta:

-A classe base Conta deve ter atributos para o número da conta, o titular da conta e o saldo.

-Ela deve incluir métodos para depósitos, saques e exibição do saldo
atual."""


class Conta:
    def __init__(self, numero_da_conta, titular, saldo):
        self.numero_da_conta = numero_da_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor_do_deposito):
        self.saldo += valor_do_deposito

    def sacar(self, valor_do_saque):
        self.saldo -= valor_do_saque

    def exibir_saldo(self):
        exibir = self.saldo
        print(exibir)

