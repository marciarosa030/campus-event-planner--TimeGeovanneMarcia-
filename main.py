print ("Ola mundo")

import gerenciador_eventos as ge
import interface_usuario as iu
import os
import time
from typing import List, Dict, Any

Event = Dict[str, Any]

def addEvent(lista_eventos: List[Event], nome: str, data: str, local: str, categoria: str) -> None:
    novo_id = max([ev.get("id", 0) for ev in lista_eventos], default=0) + 1
    evento = {
        "id": novo_id,
        "nome": nome,
        "data": data,
        "local": local,
        "categoria": categoria,
        "participado": False
    }
    lista_eventos.append(evento)

def filtrarEvento(lista_eventos: List[Event]) -> None:
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
    print("4. Deletar evento")
    print("0. Sair")