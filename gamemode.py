import random

class GameMode:
    tentativas      = 0
    numero_minimo   = 0
    numero_maximo   = 10
    chute           = int
    numero_sorteado = 0

    def incrementa_tentativas(self):
        self.tentativas = self.tentativas + 1

    def sortear_numero(self):
        self.numero_sorteado = random.randint(self.numero_minimo, self.numero_maximo)
        return self.numero_sorteado
    
    

