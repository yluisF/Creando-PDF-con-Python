# Todo ira aqui, se ejecuta el controllador
from model import Model
from view import View
from Controlador.pdfController import PdfController


class Controller:

    def __init__(self):
        #Constructor de la clase
        self.model = Model()
        self.view = View(self)

    def main(self):
        self.model.main()
        self.view.main()


if __name__ == '__main__':
    imp = Controller()
    imp.main()
