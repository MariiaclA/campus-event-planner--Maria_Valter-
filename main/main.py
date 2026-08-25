# 👥Estudante A: Módulo de Gerenciamento de Eventos

import os


listaDeEventos=[]

def limparTela():
    os.system= ("cls" if os.name == "nt" else "clear")


def adicionarEvento(listaDeEventos):

    if (procurarEventoPorNome == None):
        # cria um novo dicionário
        evento={}
        #   adciona um a chave e seu respctivo nome
        evento["nome"] = input("Informe o nome: ").strip().title()
        evento["data"] = input("Informe a data do evento: ").strip().title()
        evento["local"] = input("Informe o local do evento: ").strip().title()
        evento["Categoria"] = input("Informe a categoria do evento").strip().title()
        evento["status"]= input("Informe o status do evento como Participado ou Previsto.").strip().title()

        listaDeEventos.append(evento)
        print("Evento Cadastrado com sucesso")
    else: 
        return False


      
print("Evento adicionado com sucesso!")

# Estudante A: Listar todos os eventos
def listarEventos(listaEventos):
    if len(listaEventos) == 0:
        print("Nenhum evento cadastrado")
    else:
        for event in listaEventos:
            print(f"Evento: {event["nome"]}, Data: {event["data"]}, Local: {event["local"]}, Categoria: {event["categoria"]}")
            
#Estudante A: Filtrar eventos por categoria
def procurarEventoPorNome(listaEventos, nome):
    for event in listaEventos:
        if event["nome"].lower() == nome.lower():
            return event
    
    print("Evento não encontrado")
    return None 

    





'''========================================================================'''



# 👥 Estudante B: Módulo de Interação com Usuário e Relatórios


def menu():
    print("\n1. Adicionar Evento. \n")
    print("\n2. Ver todos os Eventos. \n")
    print("\n3. Filtrar Por Categoria. \n")
    print("\n4. Marcar Evento Como Participado. \n")
    print("\n5. Gerar Relatório. \n")
    print("\n6. Sair")


while True:

    menu()
    
    limparTela()



    try: 
        opcao = int(input())

        match opcao:

            case 1:

                pass
            case 2:
                pass
            case 3:        
                pass
            case 4:
                pass
            case 5:        
                pass
            case 6:
                print("Obrigado, volte sempre.")
                break

    except:
        print("opção inválida")
