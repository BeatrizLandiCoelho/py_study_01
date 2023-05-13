class Carro:
    def __init__(self,marca,modelo,cor,combustivel):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.combustivel = combustivel

        self.ligado = False
        self.velocidade = 0

    def ligar(self):
        if self.ligado:
         print("carro ja esta ligaado, nada aconece")

        else: 
          print("carro ligado")
          self.ligado = True

    def desligar(self):
        if self.ligado:
            print("carro desligado")
            self.ligado = False

        else:
            print("carro ja esta desligado nada acontece") 

    def acelerar(self):
        if self.ligado:
              self.velocidade += 1
              print(f"{self.velocidade}km/h")
        else:
            print("nao e possivel acelerar carro desligado") 

    def frear(self):
        if self.ligado:
            self.velocidade -= 1
            print(f"{self.velocidade}km/h")
        else:
            print("nao e possivel frear carro desligado") 
               

              
            
