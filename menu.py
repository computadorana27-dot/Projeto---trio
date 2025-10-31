from Banco import Gerenciador

def mostrar_titulo():
    """
    Mostra o título do sistema.
    """
    print("=" * 40)
    print("   🐶 SISTEMA DE BANCO🐱")
    print("=" * 40)
    print()
def menu():
    """
    Menu principal do sistema, com opções pré-condicionadas por perfil de usuário.
    """
    sistema = Gerenciador()
    perfil = ""

    # Seleção de perfil
    while perfil not in ["admin", "normal"]:
        perfil = input("Digite seu perfil (admin/normal): ").lower().strip()
        if perfil not in ["admin", "normal"]:
            print("❌ Perfil inválido! Digite 'admin' ou 'normal'.")
    continuar = True
    while continuar:
        mostrar_titulo()
        print("1️⃣  Cadastrar/Adicionar Animal" if perfil=="admin" else "")
        print("2️⃣  Remover Animal" if perfil=="admin" else "")
        print("3️⃣  Buscar Animal")
        print("4️⃣  Listar Animais")
        print("0️⃣  Sair")

        opcao = input("\n👉 Escolha uma opção: ").strip()
        # Opções para admin
        if perfil == "admin":
            if opcao == "1":
                sistema.cadastrar_animal()
            elif opcao == "2":
                sistema.remover_animal()
            elif opcao == "3":
                sistema.buscar_animal()
            elif opcao == "4":
                sistema.listar_animais()
            elif opcao == "0":
                print("Saindo do sistema... 👋")
                break
            else:
                print("❌ Opção inválida!")
