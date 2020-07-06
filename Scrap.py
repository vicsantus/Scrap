listatrabs = []
pessoascampo = ['Gleidson', 'Horste', 'Antônio', 'Max']
dicttrabalho = {'trabalho': None, 'nome': None}
historic_list_hoje = []
historic_list_todos = []


class Trabalho:

    def __init__(self):
        self.camp = Campo()

    def add_trab(self, trab, tec):
        dicttrabalho['trabalho'] = trab
        dicttrabalho['nome'] = tec
        listatrabs.append(dicttrabalho.copy())
        dicttrabalho.clear()

    def listar(self):
        if len(listatrabs) <= 0:
            print('\nNão existem trabalhos a fazer!')
        else:
            print('-' * 46)
            for index, nome in enumerate(listatrabs):
                print(f'{index:<2}-{listatrabs[index]["trabalho"]:>30}: {listatrabs[index]["nome"]}')
            print('-' * 46)

    def excluir(self):
        if len(listatrabs) > 1:
            while True:
                try:
                    qt = int(input('\nQuantos trabalhos você deseja excluir? [0 para excluir todos]: '))
                    break
                except Exception:
                    print('\nOpção inválida!')
            if qt == 0:
                listatrabs.clear()
            while qt != 0:
                Trabalho.listar(self)
                while True:
                    try:
                        excluir = int(input('\nDigite a posição do trabalho que você deseja excluir? '))
                        break
                    except Exception:
                        print('\nDigite uma posição válida!')
                if certeza() == 'S':
                    listatrabs.pop(excluir)
                qt -= 1
        else:
            if certeza() == 'S':
                listatrabs.pop(0)

    def editar(self):
        if len(listatrabs) == 1:
            while True:
                try:

                    novotrab = str(input(f'\nDigite o novo trabalho que ficará na posição 0: ')).strip().upper()
                    break
                except Exception:
                    print('\nOpção inválida!')
            listatrabs[0]["trabalho"] = novotrab
        else:
            while True:
                try:
                    Trabalho.listar(self)
                    editar = int(input('\nDigite a posição que deseja editar: '))
                    teste = listatrabs[editar]
                    novotrab = str(input(f'\nDigite o novo trabalho que ficará na posição {editar}: ')).strip().upper()
                    break
                except Exception:
                    print('\nOpção inválida!')
            listatrabs[editar]["trabalho"] = novotrab

    def add(self):
        while True:
            try:
                totaltrab = int(input('\nDeseja adicionar quantos trabalhos? '))
                break
            except Exception:
                print('Opção inválida!')
        for n in range(totaltrab):
            Trabalho.add_trab(self, str(input(f'\nDigite o {n + 1}º trabalho: ')).strip().upper(),
                              self.camp.tec_add())


class Campo:

    def add(self):
        while True:
            try:
                nome = str(input('\nQual o nome do novo técnico de campo?: ')).strip().title()
                break
            except Exception:
                print('\nOpção inválida!')
        if certeza() == 'S':
            pessoascampo.append(nome)

    def excluir(self):
        while True:
            try:
                Campo.listar(self)
                excluir = int(input('\nDeseja excluir qual técnico de campo (escolha pelo indice)?: '))
                break
            except Exception:
                print('\nOpção inválida!')
        if certeza() == 'S':
            pessoascampo.pop(excluir)

    def listar(self):
        print()
        print('-' * 33)
        for index, tec in enumerate(pessoascampo):
            print(f'{index:<2} - {tec:>28}')
        print('-' * 33)

    def editar(self):
        if len(pessoascampo) == 1:
            while True:
                try:
                    Campo.listar(self)
                    novotec = str(
                        input(f'\nDigite o nome que ficará no lugar de "{pessoascampo[0]}": ')).strip().title()
                    break
                except Exception:
                    print('\nOpção inválida!')
            pessoascampo[0] = novotec
        else:
            while True:
                try:
                    Campo.listar(self)
                    editar = int(input('\nDigite a posição que deseja editar: '))
                    teste = pessoascampo[editar]
                    novotec = str(input(f'\nDigite o novo técnico que ficará na posição {editar}: ')).strip().title()
                    break
                except Exception:
                    print('\nOpção inválida!')
            pessoascampo[editar] = novotec

    def tec_add(self):
        Campo.listar(self)
        while True:
            while True:
                try:
                    index = int(input('Digite o index do técnico à adicionar: '))
                    break
                except Exception:
                    print('\nOpção inválida!')
            if index >= len(pessoascampo) or index < 0:
                print('\nOpção inválida!')
            else:
                break
        return pessoascampo[index]

"""
class Historico:

    def historico_hoje(self):
        from datetime import date

        historic_list_hoje = listatrabs.copy()
        for i in range(len(historic_list_hoje)):
            historic_list_hoje[i]["data"] = date.today()

#    def historico_total(self):
"""


def certeza():
    while True:
        try:
            teste = str(input(f'\nVocê tem certeza disso? [S/N]: ')).strip().upper()
            if teste in 'SN':
                break
            else:
                print('\nOpção inválida!')
        except Exception:
            print('\nOpção inválida!')
    if teste == 'S':
        return 'S'
    return 'N'


def op1_op2():
    while True:
        try:
            opcao = int(input('''1 - Trabalho
2 - Técnico de campo
Escolha uma opção: '''))
            if opcao == 1 or opcao == 2:
                break
            else:
                print('\nOpção inválida!')
        except Exception:
            print('\nOpção inválida!')
    return opcao


trabclass = Trabalho()
campclass = Campo()
while True:
    trabclass.listar()
    print('''
1 - Adicionar
2 - Editar
3 - Listar
4 - Excluir
5 - Sair
0 - Limpar tela''')
    while True:
        try:
            cmd = int(input('Digite uma das opções: '))
            break
        except Exception:
            print('\nOpção inválida!')
    if cmd == 5:
        break
    elif cmd == 4:
        print('\nDeseja excluir?: ')
        if op1_op2() == 1:
            if len(listatrabs) > 0:
                trabclass.excluir()
            else:
                print('\nNão existem trabalhos à excluir!')
        else:
            if len(pessoascampo) > 0:
                campclass.excluir()
            else:
                print('\nNão existem técnicos de campo à excluir!')
    elif cmd == 0:
        print('\n' * 150)
    elif cmd == 2:
        print('\nDeseja editar?: ')
        if op1_op2() == 1:
            if len(listatrabs) > 0:
                trabclass.editar()
            else:
                print('\nNão existem trabalhos à editar!')
        else:
            if len(pessoascampo) > 0:
                campclass.editar()
            else:
                print('\nNão existem técnicos de campo à editar!')
    elif cmd == 1:
        print('\nDeseja adicionar?: ')
        if op1_op2() == 1:
            trabclass.add()
        else:
            campclass.add()
    elif cmd == 3:
        print('\nDeseja listar?:')
        if op1_op2() == 1:
            pass
        else:
            campclass.listar()
    else:
        print('\nOpção inválida!')
