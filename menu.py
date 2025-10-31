from animal import Animal

def mostrar_titulo():
    print("=" * 40)
    print("   🐶 SISTEMA DE BANCO🐱")
    print("=" * 40)
    print()
def menu():

    sistema = Animal()
    perfil = ""

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

        else:
            if opcao == "3":
                sistema.buscar_animal()
            elif opcao == "4":
                sistema.listar_animais()
            elif opcao == "0":
                print("Saindo do sistema... 👋")
                break
            else:
                print("❌ Opção inválida!")

        if opcao in ["1","2","3","4"]:
            while True:
                resposta = input("\n Deseja continuar no sistema? (s/n): ").lower().strip()
                if resposta == "s":
                    break
                elif resposta == "n":
                    print("Saindo do sistema...👋")
                    continuar = False
                    break
                else:
                    print("❌ Opção inválida! Digite 's' ou 'n'.")
if __name__ == "__main__":
    menu()