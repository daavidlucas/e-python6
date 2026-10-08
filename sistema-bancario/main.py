from banco import Banco, ContaNaoEncontradaError
from cliente import Cliente
from conta import Conta, SaldoInsuficienteError
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca
from conta_premium import ContaPremium


def cabecalho(titulo):
    print(f"\n=== {titulo} ===")


def main():
    maria = Cliente("Maria Silva", "maria.silva@email.com", "123.456.789-09")
    joao = Cliente("João Pereira", "joao.pereira@email.com", "987.654.321-00")
    ana = Cliente("Ana Souza", "ana.souza@email.com", "111.222.333-44")
    carlos = Cliente("Carlos Lima", "carlos.lima@email.com", "222.333.444-55")
    beatriz = Cliente("Beatriz Costa", "beatriz.costa@email.com", "333.444.555-66")
    pedro = Cliente("Pedro Alves", "pedro.alves@email.com", "444.555.666-77")

    contas = [
        ContaCorrente(1001, maria, 1500.0, 800.0),
        ContaCorrente(1002, joao, 300.0, 500.0),
        ContaCorrente(1003, ana, 50.0),
        ContaPoupanca(2001, maria, 5000.0, 0.006),
        ContaPoupanca(2002, carlos, 1200.0),
        ContaPoupanca(2003, beatriz, 800.0),
        ContaPremium(3001, pedro, 10000.0, 3000.0),
        ContaPremium(3002, beatriz, 2500.0),
    ]

    banco = Banco("Banco POO")
    for conta in contas:
        banco.adicionar_conta(conta)

    cabecalho("Banco e contas criadas")
    print(banco)
    for conta in banco.contas:
        print(conta)

    cabecalho("Clientes")
    for cliente in (maria, joao, ana, carlos, beatriz, pedro):
        print(cliente)

    cabecalho("Polimorfismo: resultado mensal de cada conta")
    for conta in banco.contas:
        print(f"{type(conta).__name__:<15} {conta.numero}  R$ {conta.calcular_resultado_mensal():>8.2f}")

    cabecalho("Operacoes")
    banco.buscar(1001).depositar(500.0)
    print("Deposito de R$ 500.00 na conta 1001")
    banco.buscar(1002).sacar(700.0)
    print("Saque de R$ 700.00 na conta 1002 (usa o limite)")
    banco.transferir(3001, 1003, 1000.0)
    print("Transferencia de R$ 1000.00 da conta 3001 para a 1003")
    for numero in (1001, 1002, 1003, 3001):
        print(banco.buscar(numero))

    cabecalho("Fechamento do mes")
    banco.fechar_mes()
    for conta in banco.contas:
        print(conta)
    print(banco)

    cabecalho("Metodos especiais")
    print(f"repr: {contas[0]!r}")
    print(f"repr: {contas[3]!r}")
    print(f"repr: {maria!r}")
    print(f"repr: {banco!r}")
    print(f"contas[0] == buscar(1001): {contas[0] == banco.buscar(1001)}")
    print(f"contas[0] == contas[1]: {contas[0] == contas[1]}")
    print(f"contas[2] < contas[0]: {contas[2] < contas[0]}")
    print("Contas por saldo crescente:")
    for conta in sorted(banco.contas):
        print(f"  {conta.numero}: R$ {conta.saldo:.2f}")
    print(f"Maior saldo: {max(banco.contas).numero}")
    print(f"Menor saldo: {min(banco.contas).numero}")

    cabecalho("Tratamento de excecoes")
    testes = [
        ("E-mail invalido", lambda: Cliente("Teste Silva", "email_invalido", "555.666.777-88")),
        ("CPF invalido", lambda: Cliente("Teste Silva", "teste@email.com", "12345678900")),
        ("Nome curto", lambda: Cliente("Al", "teste@email.com", "555.666.777-88")),
        ("Deposito negativo", lambda: banco.buscar(1001).depositar(-50.0)),
        ("Saque acima do saldo", lambda: banco.buscar(2002).sacar(99999.0)),
        ("Saldo negativo na poupanca", lambda: setattr(banco.buscar(2001), "saldo", -10.0)),
        ("Taxa de rendimento invalida", lambda: ContaPoupanca(2009, maria, 100.0, 0.5)),
        ("Limite negativo", lambda: ContaCorrente(1009, maria, 0.0, -100.0)),
        ("Instanciar classe abstrata", lambda: Conta(9999, maria)),
        ("Conta duplicada", lambda: banco.adicionar_conta(contas[0])),
        ("Conta inexistente", lambda: banco.buscar(404)),
    ]
    for descricao, acao in testes:
        try:
            acao()
        except (ValueError, TypeError, SaldoInsuficienteError, ContaNaoEncontradaError) as erro:
            print(f"{descricao}: {type(erro).__name__} - {erro}")
        else:
            print(f"{descricao}: nenhum erro")


if __name__ == "__main__":
    main()
