PESO_MIN, PESO_MAX = 95.0, 105.0
COMPRIMENTO_MIN, COMPRIMENTO_MAX = 10.0, 20.0
CORES_VALIDAS = {'azul', 'verde'}
CAPACIDADE_CAIXA = 10

pecas_cadastradas = []
caixas_fechadas = []
caixa_atual = []


def exibir_menu():
    print("\n" + "="*30)
    print("SISTEMA DE GESTÃO DE PEÇAS")
    print("="*30)
    print("1. Cadastrar nova peça")
    print("2. Listar peças cadastradas")
    print("3. Remover peça cadastrada")
    print("4. Listar caixas fechadas")
    print("5. Gerar relatório final")
    print("0. Sair do programa")
    print("="*30 + "\n")


def validar_peca(peso, cor, comprimento):
    motivos = []
    if not (PESO_MIN <= peso <= PESO_MAX):
        motivos.append(f"Peso fora do padrão ({peso}g)")
    if cor not in CORES_VALIDAS:
        motivos.append(f"Cor inválida ({cor})")
    if not (COMPRIMENTO_MIN <= comprimento <= COMPRIMENTO_MAX):
        motivos.append(f"Comprimento fora do padrão ({comprimento}cm)")
    return motivos


def adicionar_a_caixa(peca):
    caixa_atual.append(peca)
    if len(caixa_atual) == CAPACIDADE_CAIXA:
        caixas_fechadas.append(caixa_atual.copy()) # Usamos .copy() para salvar uma cópia exata antes de esvaziar
        caixa_atual.clear()
        print("Caixa cheia! Abrindo mais uma caixa...")


def reorganizar_caixas():
    caixas_fechadas.clear()
    caixa_atual.clear()
    for peca in pecas_cadastradas:
        if peca['status'] == "Aprovada":
            adicionar_a_caixa(peca)


def cadastrar_peca():
    print("\nIniciando cadastro de nova peça...\n")
    id_peca = input("Digite o ID da peça: ")
    peso = float(input("Digite o peso da peça (g): "))
    cor = input("Digite a cor da peça: ").strip().lower()
    comprimento = float(input("Digite o comprimento da peça (cm): "))

    motivos = validar_peca(peso, cor, comprimento)
    status = "Aprovada" if not motivos else "Reprovada"

    peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "motivos": motivos,
        "status": status,
    }
    pecas_cadastradas.append(peca)

    if status == "Aprovada":
        adicionar_a_caixa(peca)
        print(f"\n✔ Peça {id_peca} aprovada e adicionada.")
    else:
        print(f"\n✘ ATENÇÃO! Peça {id_peca} não passou no teste de qualidade.")
        print("Nem todos os requisitos de qualidade foram alcançados:")
        for motivo in motivos:
            print(f"  - {motivo}")


def listar_pecas():
    if not pecas_cadastradas:
        print("\nNenhuma peça cadastrada até o momento.")
        return
    for peca in pecas_cadastradas:
        print(f"\nID: {peca['id']} | Status: {peca['status']}")
        print(f"Medidas: {peca['peso']}g, {peca['cor'].capitalize()}, {peca['comprimento']}cm") # O capitalize transforma o primeiro caractere em maiúscula e todos os outros em minúscula
        if peca['status'] == "Reprovada":
            print(f"  Falhas encontradas: {', '.join(peca['motivos'])}") # O join transforma a lista de motivos em um texto separado por vírgulas



def remover_peca():
    id_remover = input("Digite o ID da peça que você deseja remover: ")
    peca_encontrada = next((p for p in pecas_cadastradas if p['id'] == id_remover), None)

    if peca_encontrada is None:
        print(f"\nPeça ID {id_remover} não encontrada.")
        return

    pecas_cadastradas.remove(peca_encontrada)
    print(f"\nPeça ID {id_remover} removida com sucesso!")
    reorganizar_caixas()
    print(f"Caixas reorganizadas após a remoção da peça {id_remover}.")


def listar_caixas():
    if not caixas_fechadas:
        print("\nNenhuma caixa foi fechada ainda.")
        print(f"\nStatus da caixa atual: {len(caixa_atual)} de {CAPACIDADE_CAIXA} peças.")
        return
    for indice, caixa in enumerate(caixas_fechadas): # O enumerate ajuda a contar as caixas (1, 2, 3...) enquanto percorremos a lista

        print(f"CAIXA {indice + 1} ({CAPACIDADE_CAIXA} peças):")
        for peca in caixa:
            print(f"  Peça ID: {peca['id']}; Cor: {peca['cor'].capitalize()}")


def gerar_relatorio():
    if not pecas_cadastradas:
        print("\n" + "="*30)
        print("\nNão há dados suficientes para gerar o relatório.")
        print("\n" + "="*30)
        return

    total_aprovadas = sum(1 for p in pecas_cadastradas if p['status'] == "Aprovada")
    total_reprovadas = len(pecas_cadastradas) - total_aprovadas
    total_caixas = len(caixas_fechadas) + (1 if caixa_atual else 0)

    print("\n" + "="*30)
    print(f"\n Total de peças cadastradas: {len(pecas_cadastradas)}")
    print(f"✔ Total de peças aprovadas: {total_aprovadas}")
    print(f"✘ Total de peças reprovadas: {total_reprovadas}")
    print(f"📦 Total de caixas utilizadas (fechadas e em uso): {total_caixas}")
    print("\n" + "="*30)

    if total_reprovadas > 0:
        contador_motivos = {}
        for peca in pecas_cadastradas:
            if peca['status'] == "Reprovada":
                for motivo in peca['motivos']:
                    contador_motivos[motivo] = contador_motivos.get(motivo, 0) + 1
        print("\nOs motivos para reprovação registrados são:")
        for motivo, quantidade in contador_motivos.items():
            print(f"  {motivo}: {quantidade} vez(es)")


OPCOES = {
    '1': cadastrar_peca,
    '2': listar_pecas,
    '3': remover_peca,
    '4': listar_caixas,
    '5': gerar_relatorio,
}


def main():
    while True:
        exibir_menu()
        opcao = input("Selecione uma das seguintes opções: \n")

        if opcao == '0':
            print("\nSistema encerrado!")
            break
        elif opcao in OPCOES:
            OPCOES[opcao]()
        else:
            print("\n✘ Opção inválida! Por favor, digite um número entre 0 e 5.")


if __name__ == "__main__":
    main()
