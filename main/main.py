import random
from datetime import datetime
import os
# 👥Estudante A: Módulo de Gerenciamento de Eventos
#modelo de evento

def limparTela():
    os.system= ("cls" if os.name == "nt" else "clear")

evento=[]


def validar_data(data):
    try:
        datetime.strptime(data, "%d/%m/%Y")
        return True
    except ValueError:
        return False


def adicionarEvento(listaEventos, nome, data, local, categoria):
    validar = validar_data(data)

    if (validar == True):
        novoEvento = {
            "id": random.randint(1, 1000),
            "nome" : nome,
            "data" : data,
            "local" : local, 
            "categoria": categoria,
            "participado":False
        }

        listaEventos.append(novoEvento)

        print("Evento adicionado com sucesso!")
    else:
        print("Não foi possível validar a data do evento")

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
        if event["categoria"].lower() == nome.lower():
            return event
    
    print("Evento não encontrado")
    return None 

    

def deletarEvento(listaEventos, id):
    encontrado = {}
    for event in listaEventos:
        if event["id"] == id:
            encontrado = event
            break
    
    if (encontrado):
        listaEventos.remove(encontrado)
        return 1
    else:
        print("Evento não encontrado")
        return 0
    

def marcarEventoComoParticipado(listaEventos, nome):
    for event in listaEventos:
        if event["nome"].lower() == nome.lower():
            event["participado"] = True
            print("Evento marcado como participado!")
            return True

    print("Evento não encontrado.")
    return False


def gerarRelatorio(listaEventos):
    if len(listaEventos) == 0:
        print("Nenhum evento cadastrado.")
        return

    totalEventos = len(listaEventos)
    eventosParticipados = 0
    eventosNaoParticipados = 0

    print("\n========== RELATÓRIO DE EVENTOS ==========\n")

    print(f"Total de eventos: {totalEventos}")

    print("\n--- Eventos Participados ---")

    for event in listaEventos:
        if event["participado"] == True:
            eventosParticipados += 1

            print(
                f"Nome: {event['nome']} | "
                f"Data: {event['data']} | "
                f"Local: {event['local']} | "
                f"Categoria: {event['categoria']}"
            )

    print("\n--- Eventos Não Participados ---")

    for event in listaEventos:
        if event["participado"] == False:
            eventosNaoParticipados += 1

            print(
                f"Nome: {event['nome']} | "
                f"Data: {event['data']} | "
                f"Local: {event['local']} | "
                f"Categoria: {event['categoria']}"
            )

    print("\n========== RESUMO ==========")
    print(f"Eventos participados: {eventosParticipados}")
    print(f"Eventos não participados: {eventosNaoParticipados}")
    print(f"Total: {totalEventos}")


#========================================================================'''



# 👥 Estudante B: Módulo de Interação com Usuário e Relatórios


def menu():
    print("\n1. Adicionar Evento. ")
    print("\n2. Ver todos os Eventos.")
    print("\n3. Filtrar Por Categoria.")
    print("\n4. Marcar Evento Como Participado.")
    print("\n5. Gerar Relatório.")
    print("\n6. Sair")






while True:

    limparTela()
    menu()
    
    try: 
        opcao = int(input())

        match opcao:

            case 1:
                nome = input("Nome do evento: ")
                data = input("Data (DD/MM/AAAA): ")
                local = input("Local: ")
                categoria = input("Categoria: ")

                adicionarEvento(evento, nome, data, local, categoria) 

                continue              
            case 2:
                print("\n===== TODOS OS EVENTOS =====")

                listarEventos(evento)

                continue
            case 3:        

                nome = input("Digite o nome do evento: ")

                envetoEncontrado = procurarEventoPorNome(evento, nome)

                if envetoEncontrado != None:

                    print("\nEvento encontrado!")

                    print(f"ID: {envetoEncontrado['id']}")
                    print(f"Nome: {envetoEncontrado['nome']}")
                    print(f"Data: {envetoEncontrado['data']}")
                    print(f"Local: {envetoEncontrado['local']}")
                    print(f"Categoria: {envetoEncontrado['categoria']}")

                    if evento["participado"]:
                        print("Status: Participado")
                    else:
                        print("Status: Não participado")

                else:

                    print("Evento não encontrado.")

                continue
            case 4:
                 nome = input("Digite o nome do evento que você participou: ")
                 marcarEventoComoParticipado(evento, nome)
                 continue
                
            case 5:        
                gerarRelatorio(evento)
                continue
            case 6:
                print("Obrigado, volte sempre.")
                break

    except:
        print("opção inválida")
