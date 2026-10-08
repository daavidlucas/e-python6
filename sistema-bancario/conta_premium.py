from conta_corrente import ContaCorrente


class ContaPremium(ContaCorrente):
    TARIFA_MENSAL = 0.0

    def __init__(self, numero, titular, saldo_inicial=0.0, limite=2000.0):
        super().__init__(numero, titular, saldo_inicial, limite)

    def __str__(self):
        return f"{super().__str__()} | Sem tarifa mensal"
