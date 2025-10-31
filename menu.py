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
