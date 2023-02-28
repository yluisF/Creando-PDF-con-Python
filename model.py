from Controlador.pdfController import PdfController
import json as js


class Model:

    def __init__(self):
        self.pdfController = PdfController

    def main(self):
        ruta = 'ciudad_a.json'
        self.datos(ruta)

    def datos(self, ruta):
        with open(ruta) as contenido:
            resultado = js.load(contenido)
            resultadoVivienda = str(resultado.get('fid'))
            resultadoPropietario = str(resultado.get('propietario'))
            resultadoLote = str(resultado.get('num_lote'))
            resultadoManzana = str(resultado.get('num_manzana'))
            resultadoSuelo = str(resultado.get('uso_suelo'))
            resultadoEstado = str(resultado.get('estado'))
            resultadoColonia = str(resultado.get('colonia'))
            resultadoCodigo_postal = str(resultado.get('codigo_postal'))
            resultadoArea = str(resultado.get('area'))
            resultadoPerimetro = str(resultado.get('perimetro'))

        pc = PdfController()
        pc.set_propietario(resultadoPropietario)
        pc.set_colonia(resultadoColonia)
        pc.set_estado(resultadoEstado)
        pc.set_area(resultadoArea)
        pc.set_usoSuelo(resultadoSuelo)
        pc.set_numLote(resultadoLote)
        pc.set_codigoPostal(resultadoCodigo_postal)
        pc.set_numManzana(resultadoManzana)
        pc.set_perimetro(resultadoPerimetro)


