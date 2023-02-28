class PdfController:

    __propietario = ''
    __numLote = ''
    __numManzana = ''
    __usoSuelo = ''
    __estado = ''
    __area = ''
    __perimetro = 'No definido'
    __numVivienda = '0'
    __colonia = ''
    __codigoPostal = ''
    __niveles = 'No definido'
    __altura = ''
    __densidad = ''

    def __init__(self):
        self.numLote = ''
        self.numManzana = ''
        self.usoSuelo = ''
        self.estado = ''
        self.area = ''
        self.perimetro = ''
        self.numVivienda = ''
        self.colonia = ''
        self.codigoPostal = ''
        self.propietario = ''

    def get_numLote(self):
        return PdfController.__numLote

    def get_numManzana(self):
        return PdfController.__numLote

    def get_usoSuelo(self):
        return PdfController.__usoSuelo

    def get_estado(self):
        return PdfController.__estado

    def get_area(self):
        return PdfController.__area

    def get_perimetro(self):
        return PdfController.__perimetro

    def get_numVivienda(self):
        return PdfController.__numVivienda

    def get_colonia(self):
        return PdfController.__colonia

    def get_codigoPostal(self):
        return PdfController.__codigoPostal

    def get_propietario(self):
        return PdfController.__propietario

    def get_niveles(self):
        return PdfController.__niveles

    def get_altura(self):
        return PdfController.__altura

    def get_densidad(self):
        return PdfController.__densidad

    def set_numLote(self, lote):
        PdfController.__numLote = lote

    def set_numManzana(self, manzana):
        PdfController.__numManzana = manzana

    def set_usoSuelo(self, suelo):
        PdfController.__usoSuelo = suelo

    def set_estado(self, estado):
        PdfController.__estado = estado

    def set_area(self, area):
        PdfController.__area = area

    def set_perimetro(self, perimetro):
        PdfController.__perimetro = perimetro

    def set_numVivienda(self, vivienda):
        PdfController.__numVivienda = vivienda

    def set_colonia(self, colonia):
        PdfController.__colonia = colonia

    def set_codigoPostal(self, cp):
        PdfController.__codigoPostal = cp

    def set_propietario(self, propietario):
        PdfController.__propietario = propietario

    def set_niveles(self, niveles):
        PdfController.__niveles = niveles

    def set_altura(self, altura):
        PdfController.__altura = altura

    def set_densidad(self, densidad):
        PdfController.__densidad = densidad