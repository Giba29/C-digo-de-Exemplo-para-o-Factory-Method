class RelatorioBase(Relatorio):
    def gerar(self):
        return "Conteúdo do Relatório"


class CabecalhoDecorator(Relatorio):
    def __init__(self, relatorio):
        self.relatorio = relatorio

    def gerar(self):
        return "Cabeçalho\n" + self.relatorio.gerar()

class RodapeDecorator(Relatorio):
    def __init__(self, relatorio):
        self.relatorio = relatorio

    def gerar(self):
        return self.relatorio.gerar() + "\nRodapé"

class LogotipoDecorator(Relatorio):
    def __init__(self, relatorio):
        self.relatorio = relatorio

    def gerar(self):
        return "Logotipo\n" + self.relatorio.gerar()
