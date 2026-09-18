# PROVA PRÁTICA AV2 - 3º BIMESTRE
# Arquivo: av2_sistema_modular.py
# Nome do Aluno: Leonardo carreon
# Data: 18/09/26

dados_brutos = [
    "  leonardo carreon;dsigner;11988887777  ",
    "  bruna biancadi;analista de valores;21977776666  ",
    "  sergio siqueira;gerente de dados;31966665555  "
]

def limpar_e_formatar_texto(texto):
    texto = texto.strip()
    texto = texto.upper()
    return texto

def extrair_codigo_ou_ddd(dado):
    dado = dado.strip()
    return dado[0:2]

def processar_e_exibir_cadastros(lista_dados):
    total = 0

    for dado in lista_dados:
        partes = dado.split(";")

        nome = partes[0]
        cargo = partes[1]
        telefone = partes[2]

        nome = limpar_e_formatar_texto(nome)
        cargo = limpar_e_formatar_texto(cargo)
        ddd = extrair_codigo_ou_ddd(telefone)

        print(f"Nome: {nome} | Cargo: {cargo} | DDD: {ddd}")

        total += 1

    return total

def main():
    print("==================================================")
    print("     SISTEMA DE GESTÃO MODULARIZADO - AV2")
    print("==================================================")
    print()

    print("Iniciando o processamento dos dados...")
    print()

    total_processado = processar_e_exibir_cadastros(dados_brutos)

    print()
    print(f"Total de registros processados: {total_processado}")

    print()
    print("==================================================")
    print("             PROCESSAMENTO CONCLUÍDO")
    print("==================================================")


if __name__ == "__main__":
    main()
