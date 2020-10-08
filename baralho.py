class Baralho():

    def __init__(self):
        self.baralho = []
        self.naipes = ['Paus', 'Ouros', 'Copas', 'Espadas']
        for i in range(4):
            for j in range(13):
                carta = [(j+1), self.naipes[i]]
                self.baralho.append(carta)
