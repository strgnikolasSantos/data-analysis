class ContorleReomoto:
    def __init__(self, cor , altura, profundidade, largura):
        self.cor = cor
        self.altura = altura 
        self.profundidade = profundidade
        self.largura = largura
    
    def passar_canal(self, botao):
        if botao == "+":
            print("Aumentar o canal")
        elif botao == "-":
            print("Diminuir canal")    


controle_remoto = ContorleReomoto("preto", "10cm", "2cm", "2cm")
print(controle_remoto.cor)
controle_remoto.passar_canal("+")

controle_remoto2 = ContorleReomoto("cinza", "10cm", "2cm", "2cm")
print(controle_remoto2.cor)
controle_remoto.passar_canal("-")