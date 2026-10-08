from conta import Conta


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo_inicial=0.0, taxa_rendimento=0.005):
        super().__init__(numero, titular, saldo_inicial)
        self.taxa_rendimento = taxa_rendimento

    @property
    def taxa_rendimento(self):
        return self._taxa_rendimento

    @taxa_rendimento.setter
    def taxa_rendimento(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0 or valor > 0.05:
            raise ValueError(f"Taxa de rendimento invalida (use entre 0 e 0.05): {valor}")
        self._taxa_rendimento = float(valor)

    def calcular_resultado_mensal(self):
        return round(self.saldo * self.taxa_rendimento, 2)

    def __str__(self):
        return f"{super().__str__()} | Rendimento: {self.taxa_rendimento:.2%} ao mes"

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, taxa_rendimento={self.taxa_rendimento!r})"
