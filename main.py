eventoBFD = {}

print("Bem-vindo ao sistema de gerenciamento de eventos BFD!")

def adicionarEvento(listaEventos, nome, data, local, categoria):
    evento = {
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }
    listaEventos.append(evento)
    
nome = input("Digite o nome do evento: ")
data = input("Digite a data do evento (DD/MM/AAAA): ")
local = input("Digite o local do evento: ")
categoria = input("Digite a categoria do evento: ")


print(f"Evento '{nome}' adicionado com sucesso!")