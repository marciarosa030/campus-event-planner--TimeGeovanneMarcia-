print ("Ola mundo")

from typing import List, Dict, Any

Event = Dict[str, Any]

def addEvent(lista_eventos: List[Event], nome: str, data: str, local: str, categoria: str):
    novo_id = max([ev.get("id", 0) for ev in lista_eventos], default=0) + 1
    evento = {
        "id": novo_id,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria
    }
    lista_eventos.append(evento)

def filtrarEvento(lista_eventos: List[Event]):
    for ev in lista_eventos:
        status = "Sim" if ev.get('participado', False) else "Não"
        print(
            f"ID: {ev.get('id')} | Nome: {ev.get('nome')} | Data: {ev.get('data')} | "
            f"Participou: {status}"
        )

def procurarEvento(listEventos: List[Event], nome: str) -> List[Evento]:
    termo = nome.strip().lower()
    return [
        ev for ev in listEventos
        if termo in ev.get("nome", "").lower()
    ]

def deleteEvento(lista_eventos: List[Event], id_evento: int) -> bool:
    for i, ev in enumerate(lista_eventos):
        if ev.get("id") == id_evento:
            del lista_eventos[i]
            return True
    return False

def displayMenu():
    print("\n===== MENU =====")
    print("1. Adicionar evento")
    print("2. Filtrar eventos")
    print("3. Procurar eventos")
    print("4. Filtrar por categoria")
    print("5. Deletar evento")
    print("0. Sair")

def getEscolhaDoUsuario():
    try:
        return int(input("Escolha: "))
    except ValueError:
        return -1

def filtrarPorCategoria(eventos, categoria):
    filtrados = [e for e in eventos if e["categoria"].lower() == categoria.lower()]
    if not filtrados:
        print("Nenhum evento nessa categoria.")
    else:
        for e in filtrados:
            status = "✔️" if e["participado"] else "❌"
            print(f"{e['id']}. {e['nome']} {status}")

def marcarEvento(eventos, id_evento):
    for e in eventos:
        if e["id"] == id_evento:
            e["participado"] = True
            print("Evento marcado como participado!")
            return
    print("ID não encontrado.")

def gerarRelatorio(eventos):
    if not eventos:
        print("Nenhum evento para relatar.")
        return
    total = len(eventos)
    participados = sum(e["participado"] for e in eventos)
    categorias = {}
    for e in eventos:
        categorias[e["categoria"]] = categorias.get(e["categoria"], 0) + 1
    print("\n===== RELATÓRIO =====")
    print(f"Total: {total}")
    print(f"Participados: {participados} ({participados/total*100:.1f}%)")
    for c, q in categorias.items():
        print(f"{c}: {q}")

def main():
    eventos = []
    while True:
        displayMenu()
        op = getEscolhaDoUsuario()
        if op == 1:
            adicionarEvento(eventos)
        elif op == 2:
            visualizarEventos(eventos)
        elif op == 3:
            filtrarEventosPorCategoria(eventos, input("Categoria: "))
        elif op == 4:
            try:
                marcarEventoAtendido(eventos, int(input("ID: ")))
            except ValueError:
                print("ID inválido.")
        elif op == 5:
            gerarRelatorio(eventos)
        elif op == 0:
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()