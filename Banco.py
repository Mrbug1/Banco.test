from time import sleep
resp = 'Tudo certo' 
print('Crie sua conta no banco!')
print('instruções: o nome de usuario deve ter mais de 4 caracteres,')
print('a senha deve conter mais de 3 caracteres')
usuario = str(input('Digite o nome de usuario: ')).strip()
senha = str(input('Digite sua senha: ')).strip()
ss = len(senha)
while ss <= 3:
    print('Sua senhar é fraca!')
    senha = str(input('Digite uma senha mais forte: ')).strip()
    ss = len(senha)
    print('Verificando nova senha...')
    sleep(0.5)
#Area de login################################################
print('Cadastro concluido com sucesso!')
print('===============================')
print('Entrar na conta: ')
user = str(input('Digite seu nome de usuario: '))
senh = str(input('Digite sua senha: '))
while usuario != user and senh != senha:
    user = str(input('Digite seu nome de usuario: '))
    senh = str(input('Digite sua senha: '))
while resp != '4':
    print('========================')
    print('     Dados Bancarios    ')
    print('========================')
    print('presione "1" para alterar o saldo.')
    print('Presione "2" para checar os lembretes.')
    print('Precione "3" para checar o saldo de Emergencia.')
    print('Precione "4" para sair.')
    resp = input('Qual das opções acima? ')
    if resp == '1':
        print('Configurações de saldo')
        nsal = input('Informe seu novo saldo: ')
        print('Saldo atualizado!')
    elif resp == '2':
        print('Lembretes: ')
        lenb = input('Digite seus lembretes aqui: ')
        print('Salvo.')
    elif resp == '3':
        print('Saldo de emergencia: ')
        sad = input('Digite aqui seu saldo de emergencia: ')
    else:
        if resp == '4':
            exit()
#else:
        #print('Não foi possivel criar sua conta.')

