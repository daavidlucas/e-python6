from abc import ABC, abstractmethod

from cliente import Cliente


class SaldoInsuficienteError(Exception):
    pass


class Conta(ABC):
    def __init__(self, numero, titular, saldo_inicial=0.0):
        self.numero = numero
        self.titular = titular
        self._saldo = 0.0
        self.saldo = saldo_inicial

    @property
    def numero(self):
        return self._numero

    @numero.setter
    def numero(self, valor):
        if not isinstance(valor, int) or valor <= 0:
            raise ValueError(f"Numero de conta invalido: {valor}")
        self._numero = valor

    @property
    def titular(self):
        return self._titular

    @titular.setter
    def titular(self, valor):
        if not isinstance(valor, Cliente):
            raise TypeError("Titular deve ser um Cliente")
        self._titular = valor

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError(f"Saldo invalido: {valor}")
        if valor < self.saldo_minimo:
            raise ValueError(f"Saldo abaixo do minimo permitido ({self.saldo_minimo:.2f}): {valor:.2f}")
        self._saldo = round(valor, 2)

    @property
    def saldo_minimo(self):
        return 0.0

    @staticmethod
    def _validar_valor(valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError(f"Valor deve ser positivo: {valor}")

    def depositar(self, valor):
        self._validar_valor(valor)
        self.saldo = self.saldo + valor

    def sacar(self, valor):
        self._validar_valor(valor)
        if self.saldo - valor < self.saldo_minimo:
            raise SaldoInsuficienteError(
                f"Saldo insuficiente na conta {self.numero}: saldo R$ {self.saldo:.2f}, saque R$ {valor:.2f}"
            )
        self.saldo = self.saldo - valor

    @abstractmethod
    def calcular_resultado_mensal(self):
        pass

    def fechar_mes(self):
        resultado = self.calcular_resultado_mensal()
        self.saldo = max(self.saldo + resultado, self.saldo_minimo)
        return resultado

    def __str__(self):
        return f"{type(self).__name__} {self.numero} | Titular: {self.titular.nome} | Saldo: R$ {self.saldo:.2f}"

    def __repr__(self):
        return f"{type(self).__name__}(numero={self.numero!r}, titular={self.titular.nome!r}, saldo={self.saldo!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.numero == outro.numero

    def __hash__(self):
        return hash(self.numero)

    def __lt__(self, outro):
        if not isinstance(outro, Conta):
            return NotImplemented
        return self.saldo < outro.saldo
