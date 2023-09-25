from interface import *
while True:
    interface = menu(['Registrar novo estudante', 'Listar todos os estudantes', 'Listar estudantes com nota acima de um determinado valor', 'Editar a nota de um estudante', 'Sair'])
    if interface == 1:
        registrar()
    if interface == 2:
        exibir()
    if interface == 3:
        exibirnota('digite a nota corte: ')
    if interface == 4:
        alterar()
    if interface == 5:
        break
print('Obrigado, Volte sempre!')