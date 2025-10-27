class Conta:
    def __init__(self, numero, titular, saldo=0.0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'Conta {self.numero} - Titular: {self.titular} - Saldo: R$ {self.saldo:.2f}'


class Banco:
    def __init__(self):
        self.contas = []

    def cadastrar(self, conta):
        if self.procurar_conta(conta.numero):
            print('Já existe uma conta com esse número.')
        else:
            self.contas.append(conta)
            print('Conta cadastrada com sucesso.')

    def procurar_conta(self, numero):
        for conta in self.contas:
            if conta.numero == numero:
                return conta
        return None

    def creditar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            conta.saldo += valor
            print(f'Crédito de R$ {valor:.2f} realizado na conta {numero}')
        else:
            print('Conta não encontrada.')

    def debitar(self, numero, valor):
        conta = self.procurar_conta(numero)
        if conta:
            if conta.saldo >= valor:
                conta.saldo -= valor
                print(f'Débito de R$ {valor:.2f} realizado na conta {numero}')
            else:
                print('Saldo insuficiente.')
        else:
            print('Conta não encontrada.')

    def saldo(self, numero):
        conta = self.procurar_conta(numero)
        if conta:
            print(f'Saldo da conta {numero}: R$ {conta.saldo:.2f}')
        else:
            print('Conta não encontrada.')

    def transferir(self, origem, destino, valor):
        conta_origem = self.procurar_conta(origem)
        conta_destino = self.procurar_conta(destino)

        if not conta_origem or not conta_destino:
            print('Conta de origem ou destino não encontrada')
            return

        if conta_origem.saldo < valor:
            print('Saldo insuficiente para transferência')
            return

        conta_origem.saldo -= valor
        conta_destino.saldo += valor
        print(f'Transferência de R$ {valor:.2f} realizada de {origem} para {destino}')


def menu():
    banco = Banco()

    while True:
        print('\n=== MENU DO BANCO ===')
        print('1 - Cadastrar conta')
        print('2 - Consultar saldo')
        print('3 - Creditar valor')
        print('4 - Debitar valor')
        print('5 - Transferir valor')
        print('6 - Listar todas as contas')
        print('0 - Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            numero = int(input('Número da conta: '))
            titular = input('Nome do titular: ')
            saldo_inicial = float(input('Saldo inicial: '))
            conta = Conta(numero, titular, saldo_inicial)
            banco.cadastrar(conta)

        elif opcao == '2':
            numero = int(input('Número da conta: '))
            banco.saldo(numero)

        elif opcao == '3':
            numero = int(input('Número da conta: '))
            valor = float(input('Valor a creditar: '))
            banco.creditar(numero, valor)

        elif opcao == '4':
            numero = int(input('Número da conta: '))
            valor = float(input('Valor a debitar: '))
            banco.debitar(numero, valor)

        elif opcao == '5':
            origem = int(input('Conta de origem: '))
            destino = int(input('Conta de destino: '))
            valor = float(input('Valor da transferência: '))
            banco.transferir(origem, destino, valor)

        elif opcao == '6':
            if not banco.contas:
                print('Nenhuma conta cadastrada')
            else:
                for conta in banco.contas:
                    print(conta)

        elif opcao == '0':
            print('Saindo do sistema...')
            break

        else:
            print('Opção inválida. Tente novamente')


if __name__ == '__main__':
    menu()
