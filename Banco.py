
from time import sleep
resp = ''
nsal = 0
lenb = str([])
sad = 0
cont = 0
print('Crie sua conta no banco!')
print('instruções: o nome de usuario deve ter mais de 4 caracteres,')
print('a senha deve conter mais de 3 caracteres')
usuario = str(input('Digite o nome de usuario: ')).strip()
senha = str(input('Digite sua senha: ')).strip()
while len(senha) <= 3:
    print('Sua senhar é fraca!')
    senha = str(input('Digite uma senha mais forte: ')).strip()
    print('Verificando nova senha...')
    sleep(0.5)
#Area de login################################################
print('Cadastro concluido com sucesso!')
print('===============================')
print('LOGIN ')
user = str(input('Digite seu nome de usuario: ')).strip()
senh = str(input('Digite sua senha: ')).strip()
while usuario != user or senh != senha:
        user = str(input('Digite seu nome de usuario: '))
        senh = str(input('Digite sua senha: '))
#if user == usuario and senh == senha:
while True:
    print('========================')
    print('     Dados Bancarios    ')
    print('========================')
    print('presione "1" para alterar o saldo.')
    print('Presione "2" para checar os lembretes.')
    print('Precione "3" para checar o saldo de Emergencia.')
    print('Precione "4" para sair')
    resp = input('Qual das opções acima? ')
    if resp == '1':
        print(f'Seu saldo atual é de R${nsal}')
        q = input(('Deseja alterar o saldo? [S/N]')).upper()
        if q == 'S':
            print('Configurações de saldo')
            nsal = input('Informe seu novo saldo: ')
            print('Saldo atualizado!')
        elif q == 'N':
            pass
        else:
            print('Erro opção invalida.')
        sleep(0.4)
    elif resp == '2':
        print('LEMBRETES: ')
        print(lenb[0:cont+1])
        w = input('Deseja adicionar mais algo? [S/N]').upper().strip()
        if w == 'S':
            lenb = input('Digite seus lembretes aqui: ')
            cont += 1
            sleep(0.2)
            print('Salvo.')
        elif w == 'N':
            pass
        else:
            print('ERRO! OPÇÃO INVALIDA.')
        sleep(0.2)
    elif resp == '3':
        print('Saldo de Emergencia: ')
        print(f'R${sad}')
        e = input('Deseja alterar: [S/N]').strip().upper()
        if e == 'S':
            sad = input('Digite aqui seu saldo de emergencia: ')
            print('Concluido')
            sleep(0.2)
        elif e == 'N':
            pass
        else:
            print('Opção invalida! tente novamente.')
        sleep(0.2)
    else:
        if resp == '4':
            print('Volte sempre!, BYEEEEEE')
            exit()
