from conta import Conta


class ContaNaoEncontradaError(Exception):
    pass


class Banco:
    def __init__(self, nome, contas=None):
        self.nome = nome
        self._contas = []
        if contas is not None:
            for conta in contas:
                self.adicionar_conta(conta)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("Nome do banco nao pode ser vazio")
        self._nome = valor.strip()

    @property
    def contas(self):
        return list(self._contas)

    def adicionar_conta(self, conta):
        if not isinstance(conta, Conta):
            raise TypeError("Apenas contas podem ser adicionadas ao banco")
        if conta in self._contas:
            raise ValueError(f"Conta {conta.numero} ja existe no banco")
        self._contas.append(conta)

    def buscar(self, numero):
        for conta in self._contas:
            if conta.numero == numero:
                return conta
        raise ContaNaoEncontradaError(f"Conta {numero} nao encontrada")

    def transferir(self, origem, destino, valor):
        conta_origem = self.buscar(origem)
        conta_destino = self.buscar(destino)
        conta_origem.sacar(valor)
        conta_destino.depositar(valor)

    def fechar_mes(self):
        for conta in self._contas:
            conta.fechar_mes()

    def saldo_total(self):
        return sum(conta.saldo for conta in self._contas)

    def __len__(self):
        return len(self._contas)

    def __str__(self):
        return f"{self.nome}: {len(self)} contas, saldo total R$ {self.saldo_total():.2f}"

    def __repr__(self):
        return f"Banco(nome={self.nome!r}, contas={len(self)})"
