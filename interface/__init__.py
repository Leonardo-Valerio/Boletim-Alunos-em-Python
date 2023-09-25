def linha():
    print('-'*30)

def menu(msg):
    linha()
    print('Seja bem vindo!')
    linha()
    c=1
    for i in msg:
        print(f'Opção {c} = {i}')
        c+=1
    linha()
    opcao = intmenu('Escolha uma das opções: ')
    return opcao

def intmenu(n):
    while True:
        try:
            entrada = int(input(n))
            if entrada < 1 or entrada > 5:
                print('Opção invalida')
                continue
        except:
            print('Erro, opção invalida!')
        else:
            return entrada
def intnota(notaa):
    while True:
        try:
            entradan = int(input(notaa))
            if entradan < 1 or entradan > 10:
                continue
        except:
            print('digite um numero inteiro')
        else:
            return entradan

def intidade(idade):
    while True:
        try:
            entradai = int(input(idade))
            if entradai < 1 or entradai > 100:
                continue
        except:
            print('digite uma idade possivel')
        else:
            return entradai
def lerint(inteiro):
    while True:
        try:
            i = int(input(inteiro))
        except:
            print('digite um numero inteiro')
        else:
            return i


lst = [{'nome': 'Julia', 'idade': '14', 'Nota': 7}, {'nome': 'Lucas', 'idade': '13', 'Nota': 8}, {'nome': 'Gabriel', 'idade': '15', 'Nota': 3}, {'nome': 'Luiza', 'idade': '16', 'Nota': 6}, {'nome': 'Henrrique', 'idade': '17', 'Nota': 10}]

def exibir():
    global lst
    for i in lst:
        print(f'Nome: {i["nome"]}', end=' /')
        print(f'Idade: {i["idade"]}', end=' /')
        print(f'Nota: {i["Nota"]}')
def exibirnota(nota):
    global lst
    nota = intnota(nota)
    print(f'Aqui estão os alunos com nota maior que {nota}')
    for i in lst:
        if i['Nota'] > nota:
            print(f'Nome: {i["nome"]}', end=' /')
            print(f'Idade: {i["idade"]}', end=' /')
            print(f'Nota: {i["Nota"]}')

def registrar():
    global lst
    aluno = {}
    linha()
    print('Registrando novo estudante: ')
    linha()
    aluno['nome'] = input('digite o nome do aluno: ')
    aluno['idade'] = intidade('digite a idade do aluno: ')
    aluno['Nota'] = intnota('digite a nota do aluno: ')
    linha()
    lst.append(aluno.copy())

def alterar():
    global lst
    for i,v in enumerate(lst):
        print(i, end=' = ')
        print(f'Nome: {v["nome"]}', end=' /')
        print(f'Nota: {v["Nota"]}')
    escolha = lerint('digite o codigo do aluno que deseja alterar a nota: ')
    escolhanota = intnota('digite a nota a ser alterada: ')
    lst[escolha]['Nota'] = escolhanota







