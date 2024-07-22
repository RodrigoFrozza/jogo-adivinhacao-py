import os
from jogador import Jogador
from tela    import Tela

game_loop = True




def main():
    os.system('cls')
    main_menu = Tela('*      -  JOGO DA ADIVINHAÇÃO  -      *','*')
    player01 = Jogador(main_menu.draw_create_player_screen())


    os.system('cls')
    main_menu.draw_header()
    main_menu.draw_player_status(player01._experiencia, player01._nivel, player01.nome)
    main_menu.draw_numero_sorteado_screen()
    main_menu.draw_game_screen()

    


if __name__ == '__main__':
    main()