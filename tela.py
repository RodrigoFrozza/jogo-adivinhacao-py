from gamemode import GameMode

class Tela:
    titulo = ''
    marcador = ''
    numero_sorteado = int
    game_mode = GameMode()

    def __init__(self,titulo, marcador) -> None:
        self.game_mode = GameMode()

        self.titulo = titulo
        self.marcador = marcador
        print(marcador*len(titulo))
        print(f'{titulo}')
        print(marcador*len(titulo))


    def draw_header(self):
        print(self.marcador*len(self.titulo))
        print(f'{self.titulo}')
        print(self.marcador*len(self.titulo))

    def draw_create_player_screen(self):
        print('\nDigite o nome do Jogador: ')
        nome_do_jogador = input()
        return nome_do_jogador
    
    def draw_player_status(self, experiencia, nivel, nome_jogador):
        print(f'EXP: {experiencia} | Level: {nivel} | Jogador: {nome_jogador}\n\n')

    def draw_numero_sorteado_screen(self):
        self.game_mode.sortear_numero()
        print(f'Chute um Número entre {self.game_mode.numero_minimo} e {self.game_mode.numero_maximo}\n\n')


    def draw_game_screen(self):

        while self.game_mode.chute != self.game_mode.numero_sorteado:
            print(f'N° de Tentativas: {self.game_mode.tentativas}')

            try:
                self.game_mode.chute = int(input('Chute > '))
            except:
                print('Número Inválido')
            
            if self.game_mode.chute > self.game_mode.numero_sorteado:
                print('O Número Secreto é MENOR que seu chute')
                self.game_mode.incrementa_tentativas()
            elif self.game_mode.chute < self.game_mode.numero_sorteado:
                print('O Número Secreto é MAIOR que seu chute')
                self.game_mode.incrementa_tentativas()
            else:
                print('Você Acertou!')


