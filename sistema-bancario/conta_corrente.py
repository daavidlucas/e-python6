from conta import Conta


class ContaCorrente(Conta):
    TARIFA_MENSAL = 15.0

    def __init__(self, numero, titular, saldo_inicial=0.0, limite=500.0):
        self.limite = limite
        super().__init__(numero, titular, saldo_inicial)

    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError(f"Limite invalido: {valor}")
        self._limite = float(valor)

    @property
    def saldo_minimo(self):
        return -self.limite

    def calcular_resultado_mensal(self):
        return 0.0 - self.TARIFA_MENSAL

    def __str__(self):
        return f"{super().__str__()} | Limite: R$ {self.limite:.2f}"

    def __repr__(self):
        return f"{super().__repr__()[:-1]}, limite={self.limite!r})"
