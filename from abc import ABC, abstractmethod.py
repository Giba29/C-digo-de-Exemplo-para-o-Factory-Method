from abc import ABC, abstractmethod

# Interface RelatorioFactory
class RelatorioFactory(ABC):
    @abstractmethod
    def criar_relatorio(self):
        pass

# Implementações concretas para cada tipo de relatório
class RelatorioPDFFactory(RelatorioFactory):
    def criar_relatorio(self):
        return RelatorioPDF()

class RelatorioExcelFactory(RelatorioFactory):
    def criar_relatorio(self):
        return RelatorioExcel()

class RelatorioHTMLFactory(RelatorioFactory):
    def criar_relatorio(self):
        return RelatorioHTML()

# Interface Relatorio
class Relatorio(ABC):
    @abstractmethod
    def gerar(self):
        pass

# Implementações concretas de Relatorio
class RelatorioPDF(Relatorio):
    def gerar(self):
        return "Gerando relatório em PDF"

class RelatorioExcel(Relatorio):
    def gerar(self):
        return "Gerando relatório em Excel"

class RelatorioHTML(Relatorio):
    def gerar(self):
        return "Gerando relatório em HTML"