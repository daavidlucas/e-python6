import re


class Cliente:
    def __init__(self, nome, email, cpf):
        self.nome = nome
        self.email = email
        self.cpf = cpf

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or len(valor.strip()) < 3:
            raise ValueError("Nome deve ter pelo menos 3 caracteres")
        self._nome = valor.strip()

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, valor):
        if not isinstance(valor, str) or not re.match(r"^[\w.\-]+@[\w\-]+(\.[\w\-]+)+$", valor):
            raise ValueError(f"E-mail invalido: {valor}")
        self._email = valor

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, valor):
        if not isinstance(valor, str) or not re.match(r"^\d{3}\.\d{3}\.\d{3}-\d{2}$", valor):
            raise ValueError(f"CPF invalido: {valor}")
        self._cpf = valor

    def __str__(self):
        return f"{self.nome} ({self.email})"

    def __repr__(self):
        return f"Cliente(nome={self.nome!r}, email={self.email!r}, cpf={self.cpf!r})"

    def __eq__(self, outro):
        if not isinstance(outro, Cliente):
            return NotImplemented
        return self.cpf == outro.cpf

    def __hash__(self):
        return hash(self.cpf)
