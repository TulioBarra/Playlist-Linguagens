class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    def exibir_informacoes(self):
        return f"{self.titulo} - {self.artista} ({self.duracao})"

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)
        print(f"Música '{musica.titulo}' adicionada à playlist '{self.nome}'.")

    def exibir_playlist(self):
        print(f"Playlist: {self.nome}")
        if self.musicas:
            for musica in self.musicas:
                print(f"- {musica.exibir_informacoes()}")
        else:
            print("Nenhuma música na playlist.")

class Catalogo:
    def __init__(self):
        self.musicas = []

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def listar_musicas(self):
        print("Músicas disponíveis no catálogo:")
        for i, musica in enumerate(self.musicas, 1):
            print(f"{i}. {musica.exibir_informacoes()}")

    def selecionar_musica(self, indice):
        if 1 <= indice <= len(self.musicas):
            return self.musicas[indice - 1]
        else:
            print("Música inválida.")
            return None

# Configuração inicial
catalogo = Catalogo()
catalogo.adicionar_musica(Musica("Song 1", "Artist 1", "3:45"))
catalogo.adicionar_musica(Musica("Song 2", "Artist 2", "4:30"))
catalogo.adicionar_musica(Musica("Song 3", "Artist 1", "5:00"))
playlists = {}
musica_selecionada = None

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
        catalogo.listar_musicas()
    elif opcao == "2":
        catalogo.listar_musicas()
        musica_id = int(input("Digite o número da música para selecionar: "))
        musica_selecionada = catalogo.selecionar_musica(musica_id)
        if musica_selecionada:
            print(f"Música selecionada: {musica_selecionada.exibir_informacoes()}")
    elif opcao == "3":
        nome = input("Digite o nome da nova playlist: ")
        if nome in playlists:
            print(f"A playlist '{nome}' já existe.")
        else:
            playlists[nome] = Playlist(nome)
            print(f"Playlist '{nome}' criada com sucesso.")
    elif opcao == "4":
        nome = input("Digite o nome da playlist: ")
        if nome in playlists:
            if musica_selecionada:
                playlists[nome].adicionar_musica(musica_selecionada)
            else:
                print("Nenhuma música foi selecionada. Por favor, selecione uma música primeiro.")
        else:
            print(f"Playlist '{nome}' não encontrada.")
    elif opcao == "5":
        nome = input("Digite o nome da playlist: ")
        if nome in playlists:
            playlists[nome].exibir_playlist()
        else:
            print(f"Playlist '{nome}' não encontrada.")
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida.")