class Jogador():
    nome             = ''
    _experiencia     = 0
    _nivel           = 1

    def __init__(self,nome) -> None:
        self.nome = nome
    

    def incrementa_experiencia(self,valor_incremento=int):
        self._experiencia = self._experiencia + valor_incremento
        self.set_nivel()
    
    def set_nivel(self):
        if(self._experiencia < 1000):
            self._nivel = 1
        else:
            self._nivel = round(self._experiencia / 1000,0)



          