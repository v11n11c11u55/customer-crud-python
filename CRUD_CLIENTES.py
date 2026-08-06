import json
from pathlib import Path

PASTA = Path(__file__).parent
ARQUIVO = PASTA / "clientes.json"


def carregar_clientes():
    if ARQUIVO.exists():
        # O "O UTF-8" É PARA PODER UTILIZAR AS LETRAS: "ÇÂÉ".
        with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    return []


def salvar_clientes(clientes):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=4, ensure_ascii=False)


clientes = carregar_clientes()

print("===== LISTA DE CLIENTES =====")

while True:

    print("\n[1] ADICIONAR")
    print("[2] VISUALIZAR")

    print("[3] DELETAR")
    print("[4] SAIR")

    opcao = input("\nSelecione uma opção: ")

    match opcao:

        case "1":

            novo_id = max((c["id"] for c in clientes), default=0) + 1

            nome = input("Nome: ")
            while True:
                try:
                    idade = int(input("Idade: "))
                    break
                except ValueError:
                    print("DIGITE APENAS NUMEROS!")
            produto = input("Produto: ")

            clientes.append(
                {"id": novo_id, "nome": nome, "idade": idade, "produto": produto}
            )

            salvar_clientes(clientes)

            print("\nCliente cadastrado com sucesso!")

        case "2":

            if not clientes:
                print("\nNenhum cliente cadastrado.")
            else:

                print()

                for cliente in clientes:
                    print(f"ID: {cliente['id']}")
                    print(f"NOME: {cliente['nome'].upper()}")
                    print(f"IDADE: {cliente['idade']}")
                    print(f"PRODUTO: {cliente['produto'].title()}")
                    print("-" * 30)

        case "3":

            nome = input("Nome completo do cliente: ").upper()

            for indice, cliente in enumerate(clientes):

                if cliente["nome"].upper() == nome:

                    del clientes[indice]
                    salvar_clientes(clientes)

                    print("Cliente removido!")
                    break

            else:
                print("Cliente não encontrado.")

        case "4":

            print("Sistema encerrado.")
            break

        case _:

            print("Opção inválida.")
