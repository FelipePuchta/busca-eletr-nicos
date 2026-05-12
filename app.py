import sys
sys.stdout.reconfigure(encoding='utf-8')
import os
from database import buscar_do_banco

notebooks=buscar_do_banco("notebooks")
celulares=buscar_do_banco("celulares")
tablets=buscar_do_banco("tablets")

def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

def categoria_celular():
    limpar_tela()
    print("Nessa aba, estão presentes apenas aparelhos celular")
    print("""A seguir estão os filtros que podem ser usados:
1. Custo-Benefício
2. Para trabalho
3. Para jogos
4. Sem filtro""")
    while True:
        try:
            escolha = int(input("Digite a sua opção de filtro: "))
            break
        except:
            print("Digite apenas números\n")
    limpar_tela()
    if escolha == 1:
        print("Aqui estão os aparelhos custo-benefício:")
        for celular in celulares:
            if celular["uso"] == "custo_beneficio":
                print(30*"-")
                print(f"Nome: {celular['nome']}")
                print(f"Marca: {celular['marca']}")
                print(f"Preço: {celular['preco']}")
                print(30*"-")
    elif escolha == 2:
        print("Aqui estão os aparelhos para trabalho:")
        for celular in celulares:
            if celular["uso"] == "trabalho":
                print(30*"-")
                print(f"Nome: {celular['nome']}")
                print(f"Marca: {celular['marca']}")
                print(f"Preço: {celular['preco']}")
                print(30*"-")
    elif escolha == 3:
        print("Aqui estão os melhores celulares para jogos:")
        for celular in celulares:
            if celular["uso"] == "jogos":
                print(30*"-")
                print(f"Nome: {celular['nome']}")
                print(f"Marca: {celular['marca']}")
                print(f"Preço: {celular['preco']}")
                print(30*"-")
    elif escolha == 4:
        print("Todos os celulares cadastrados:")
        for celular in celulares:
            print(30*"-")
            print(f"Nome: {celular['nome']}")
            print(f"Marca: {celular['marca']}")
            print(f"Preço: R$ {celular['preco']}")
            print(30*"-")
    else:
        print("Escolha inválida")
    
    voltar = input("\nDeseja voltar ao menu principal? (s/n): ")
    if voltar.lower() == "s":
        menu_principal()
    voltar=input("Deseja voltar ao menu principal [s/n]?")
def categoria_notebook():
    limpar_tela()
    print("Nessa aba, estão presentes apenas notebooks")
    print("""A seguir estão os filtros que podem ser usados:
1. Custo-Benefício
2. Para trabalho
3. Para jogos
4. Sem filtro""")
    while True:
        try:
            escolha = int(input("Digite a sua opção de filtro: "))
            break
        except:
            print("Digite apenas números\n")
    limpar_tela()
    if escolha == 1:
        print("Aqui estão os notebooks custo-benefício:")
        for notebook in notebooks:
            if notebook["uso"] == "custo_beneficio":
                print(30*"-")
                print(f"Nome: {notebook['nome']}")
                print(f"Marca: {notebook['marca']}")
                print(f"Preço: {notebook['preco']}")
                print(f"RAM: {notebook['ram_gb']} GB")
                print(f"Armazenamento: {notebook['armazenamento_gb']} GB")
                print(f"Processador: {notebook['processador']}")
                print(30*"-")
    elif escolha == 2:
        print("Aqui estão os melhores notebooks para trabalho:")
        for notebook in notebooks:
            if notebook["uso"] == "trabalho":
                print(30*"-")
                print(f"Nome: {notebook['nome']}")
                print(f"Marca: {notebook['marca']}")
                print(f"Preço: {notebook['preco']}")
                print(f"RAM: {notebook['ram_gb']} GB")
                print(f"Armazenamento: {notebook['armazenamento_gb']} GB")
                print(f"Processador: {notebook['processador']}")
                print(30*"-")
    elif escolha == 3:
        print("Aqui estão os melhores notebooks para jogos:")
        for notebook in notebooks:
            if notebook["uso"] == "jogos":
                print(30*"-")
                print(f"Nome: {notebook['nome']}")
                print(f"Marca: {notebook['marca']}")
                print(f"Preço: {notebook['preco']}")
                print(f"RAM: {notebook['ram_gb']} GB")
                print(f"Armazenamento: {notebook['armazenamento_gb']} GB")
                print(f"Processador: {notebook['processador']}")
                print(30*"-")
    elif escolha == 4:
        print("Todos os notebooks cadastrados:")
        for notebook in notebooks:
            print(30*"-")
            print(f"Nome: {notebook['nome']}")
            print(f"Marca: {notebook['marca']}")
            print(f"Preço: {notebook['preco']}")
            print(f"RAM: {notebook['ram_gb']} GB")
            print(f"Armazenamento: {notebook['armazenamento_gb']} GB")
            print(f"Processador: {notebook['processador']}")
            print(30*"-")
    else:
        print("Escolha inválida")
    
    voltar = input("\nDeseja voltar ao menu principal? (s/n): ")
    if voltar.lower() == "s":
        menu_principal()

def categoria_tablet():
    limpar_tela()
    print("Nessa aba, estão presentes apenas tablets/iPads")
    print("""A seguir estão os filtros que podem ser usados:
1. Custo-Benefício
2. Para trabalho
3. Para jogos
4. Sem filtro""")
    while True:
        try:
            escolha = int(input("Digite a sua opção de filtro: "))
            break
        except:
            print("Digite apenas números\n")
    limpar_tela()
    if escolha == 1:
        print("Aqui estão os tablets custo-benefício:")
        for tablet in tablets:
            if tablet["uso"] == "custo_beneficio":
                print(30*"-")
                print(f"Nome: {tablet['nome']}")
                print(f"Marca: {tablet['marca']}")
                print(f"Preço: {tablet['preco']}")
                print(f"RAM: {tablet['ram_gb']} GB")
                print(f"Armazenamento: {tablet['armazenamento_gb']} GB")
                print(30*"-")
    elif escolha == 2:
        print("Aqui estão os melhores tablets para trabalho:")
        for tablet in tablets:
            if tablet["uso"] == "trabalho":
                print(30*"-")
                print(f"Nome: {tablet['nome']}")
                print(f"Marca: {tablet['marca']}")
                print(f"Preço: {tablet['preco']}")
                print(f"RAM: {tablet['ram_gb']} GB")
                print(f"Armazenamento: {tablet['armazenamento_gb']} GB")
                print(30*"-")
    elif escolha == 3:
        print("Aqui estão os melhores tablets para jogos:")
        for tablet in tablets:
            if tablet["uso"] == "jogos":
                print(30*"-")
                print(f"Nome: {tablet['nome']}")
                print(f"Marca: {tablet['marca']}")
                print(f"Preço: {tablet['preco']}")
                print(f"RAM: {tablet['ram_gb']} GB")
                print(f"Armazenamento: {tablet['armazenamento_gb']} GB")
                print(30*"-")
    elif escolha == 4:
        print("Todos os tablets cadastrados:")
        for tablet in tablets:
            print(30*"-")
            print(f"Nome: {tablet['nome']}")
            print(f"Marca: {tablet['marca']}")
            print(f"Preço: {tablet['preco']}")
            print(f"RAM: {tablet['ram_gb']} GB")
            print(f"Armazenamento: {tablet['armazenamento_gb']} GB")
            print(30*"-")
    else:
        print("Escolha inválida")

    voltar = input("\nDeseja voltar ao menu principal? (s/n): ")
    if voltar.lower() == "s":
        menu_principal()

def menu_principal():
    limpar_tela()
    print("=" * 35)
    print("\nBEM VINDO AO BUSCA ELETRÔNICOS\n")
    print("=" * 35)
    print("Logo abaixo estão as categorias disponíveis:")
    print("""1. Celular
2. Notebook
3. Tablet/iPad""")
    while True:
        try:
            escolha = int(input("Qual opção deseja escolher? "))
            break
        except:
            print("Digite apenas números\n")
    if escolha == 1:
        categoria_celular()
    elif escolha == 2:
        categoria_notebook()
    elif escolha == 3:
        categoria_tablet()
    else:
        print("Escolha inválida")

menu_principal()















    

 