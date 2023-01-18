resp = 'S'
total = int(input('Digite o total de pedidos: '))
while resp == 'S':
    meup = int(input('Digite seu pedido: '))
    fim = meup + total
    print(f'Total: {fim}')
    resp = input('Deseja alterar? [S/N]').strip().upper()
    if resp == 'N':
        break
    while resp != 'S' and 'N':
        print('Opção invalida.')
        resp = input('Deseja alterar? [S/N]').strip().upper()
print('fim')

