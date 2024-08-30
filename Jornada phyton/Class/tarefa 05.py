class Area:
    def __init__(self):
        self.comodos = ["sala", "cozinha", "banheiro", "quarto", "lavanderia", "closet"]
        self.largura = float(input("Insira a largura em metros: "))
        self.altura = float(input("Insira a altura em metros: "))
        self.area = self.altura * self.largura

        print(self.comodos)
        selection = int(input("Escolha o número correspondente ao cômodo: "))

        if 0 <= selection < len(self.comodos):
            selected_comodo = self.comodos[selection]
            print(f"O cômodo selecionado foi {selected_comodo} e a área é {self.area} metros quadrados.")
        else:
            print("Seleção inválida!")

class Iluminacao:
    def __init__(self, area):
        self.lumens = int(input("Número de lumens oferecido pela lâmpada: "))
        self.lux = int(input("Quantidade de lux determinada para o cômodo: "))
        self.area = area
    
    def calcularLampadas(self):
        lumi = self.area * self.lux
        num_lampadas = lumi / self.lumens
        return num_lampadas


areaComodo = Area()  # Calcula a área
iluminacaoComodo = Iluminacao(areaComodo.area)  # Passa a área calculada para a classe Iluminacao

numero_de_lampadas = iluminacaoComodo.calcularLampadas()
print(f"A quantidade de lâmpadas necessária será: {numero_de_lampadas:.2f}")
