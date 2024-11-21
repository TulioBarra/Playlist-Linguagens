# Lista de músicas disponíveis no catálogo
catalogo = [
    {"titulo": "Song 1", "artista": "Artist 1", "duracao": "3:45"},
    {"titulo": "Song 2", "artista": "Artist 2", "duracao": "4:30"},
    {"titulo": "Song 3", "artista": "Artist 1", "duracao": "5:00"},
]

# Dicionário para armazenar playlists
playlists = {}

# Funções do sistema
def listar_catalogo():
    print("Músicas disponíveis no catálogo:")
    for i, musica in enumerate(catalogo, 1):
        print(f"{i}. {musica['titulo']} - {musica['artista']} ({musica['duracao']})")

def selecionar_musica():
    listar_catalogo()
    musica_id = int(input("Digite o número da música para selecionar: "))
    if 1 <= musica_id <= len(catalogo):
        musica = catalogo[musica_id - 1]
        print(f"Música selecionada: {musica['titulo']} - {musica['artista']} ({musica['duracao']})")
        return musica
    else:
        print("Número inválido.")
        return None

def criar_playlist(nome_playlist):
    if nome_playlist in playlists:
        print(f"A playlist '{nome_playlist}' já existe.")
    else:
        playlists[nome_playlist] = []
        print(f"Playlist '{nome_playlist}' criada com sucesso.")

def adicionar_musica_playlist(nome_playlist, musica):
    if nome_playlist not in playlists:
        print(f"Playlist '{nome_playlist}' não encontrada.")
    else:
        playlists[nome_playlist].append(musica)
        print(f"Música '{musica['titulo']}' adicionada à playlist '{nome_playlist}'.")

def mostrar_playlist(nome_playlist):
    if nome_playlist in playlists:
        print(f"Playlist: {nome_playlist}")
        for musica in playlists[nome_playlist]:
            print(f"- {musica['titulo']} - {musica['artista']} ({musica['duracao']})")
    else:
        print(f"Playlist '{nome_playlist}' não encontrada.")

# Interface com o usuário
while True:
    print("\nOpções:")
    print("1. Listar músicas do catálogo")
    print("2. Selecionar uma música")
    print("3. Criar uma playlist")
    print("4. Adicionar música a uma playlist")
    print("5. Mostrar uma playlist")
    print("6. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        listar_catalogo()
    elif opcao == "2":
        musica_selecionada = selecionar_musica()
    elif opcao == "3":
        nome = input("Digite o nome da nova playlist: ")
        criar_playlist(nome)
    elif opcao == "4":
        nome = input("Digite o nome da playlist: ")
        if 'musica_selecionada' in locals() and musica_selecionada:
            adicionar_musica_playlist(nome, musica_selecionada)
        else:
            print("Nenhuma música foi selecionada. Por favor, selecione uma música primeiro.")
    elif opcao == "5":
        nome = input("Digite o nome da playlist: ")
        mostrar_playlist(nome)
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")