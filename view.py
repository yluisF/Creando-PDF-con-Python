import datetime
from fpdf import FPDF
import geopandas as gpd
import matplotlib.pyplot as plt
from os import remove
import contextily as cx
from Controlador.pdfController import PdfController
from model import Model

pdf = FPDF(orientation='P', unit='mm', format='Letter')


class View:
    def __init__(self, controller):
        self.model = Model()
        self.controller = controller

    def main(self):
        print('Iniciando...')
        self.definirFiguras()
        self.datosPredio()
        self.asignacionContenido()
        self.asignacionContenido2()

    def definirFiguras(self):
        acuna = "nuevo_acuna_completo.geojson"
        map_data = gpd.read_file(acuna)
        map_data.head()
        index = map_data.set_index("fid")
        casa = map_data.loc[1, "geometry"]
        # casa = map_data.query("fid==1")
        geom = gpd.GeoSeries([casa])
        # Control del tamaño de la figura del mapa
        fig = plt.figure(figsize=(5, 4), dpi=100, frameon=False)
        ax = plt.Axes(fig, [0.1, 0.1, 0.8, 0.8])
        fig.add_axes(ax)
        # Control del título y los ejes
        ax.set_title('CIUDAD ACUÑA',
                     pad=10,
                     fontdict={'fontsize': 10, 'color': '#4873ab'})
        ax.set_xlabel('Longitud')
        ax.set_ylabel('Latitud')
        # obteniendo coordenadas y haciendo zoom
        valores = geom.total_bounds
        print(valores)
        minx, miny, maxx, maxy = geom.total_bounds
        ax.set_xlim(minx - 0.0005, maxx + 0.0005)
        ax.set_ylim(miny - 0.0005, maxy + 0.0005)
        # Mostrar el mapa finalizado
        map_data.plot(ax=ax, edgecolor="k", cmap='OrRd', alpha=0.1)
        geom.plot(ax=ax, color="gray", alpha=0.8)
        # utilizando libreria para basemap para mostrear calles
        cx.add_basemap(ax=ax, zoom=19, crs=map_data.crs.to_string(), source=cx.providers.OpenStreetMap.Mapnik, )
        plt.savefig('map.png')

        pdf.add_page()
        pdf.rect(x=13, y=45, w=87.5, h=110)
        pdf.rect(x=20, y=124, w=73.5, h=25)
        pdf.rect(x=105, y=45, w=97.5, h=110)
        pdf.rect(x=13, y=160, w=190, h=50)
        pdf.rect(x=13, y=220, w=190, h=50)

    def encabezado(self):
        ahora = datetime.datetime.now()
        pdf.set_font('Arial', '', 7)
        pdf.set_fill_color(r=255, g=255, b=255)
        pdf.text(x=13, y=10, txt=ahora.strftime('%d/%m/%Y %H:%M'))
        pdf.text(x=105, y=10, txt='Normatividad Uso de Suelo')
        pdf.set_font('Arial', 'B', 8)
        # imagenes

    def asignacionContenido(self):
        pdf.image('./img/banner-acuna.png', x=15, y=14, w=50, h=25)
        pdf.image('./img/escudo-acuna.png', x=185, y=14, w=20, h=20)
        pdf.image('map.png', x=110, y=55, w=87.5, h=50)

        self.encabezado()
        # Datos
        pdf.text(x=16, y=48, txt='Información General')
        pdf.text(x=16, y=60, txt='Cuenta Catastral')
        pdf.text(x=16, y=68, txt='Dirección')
        pdf.text(x=19, y=76, txt='Propietario:')
        pdf.text(x=19, y=80, txt='Colonia:')
        pdf.text(x=19, y=84, txt='Código Postal:')
        pdf.text(x=19, y=88, txt='Superficie del Predio:')
        pdf.text(x=108, y=48, txt='Ubicación del Predio')

        pdf.set_font('Arial', 'B', 8)
        pdf.text(x=16, y=163, txt='Zonificación')
        pdf.set_font('Arial', 'B', 7.5)
        pdf.text(x=30, y=166, txt='Uso del suelo 1:')
        pdf.text(x=60, y=166, txt='Niveles:')
        pdf.text(x=75, y=166, txt='Altura:')
        pdf.text(x=90, y=166, txt='% Área')

        pdf.text(x=106, y=166, txt='M2 min.')
        pdf.text(x=125, y=166, txt='Densidad:')

        pdf.text(x=145, y=166, txt='Superficie')
        pdf.text(x=145, y=169, txt='Maxima de')
        pdf.text(x=145, y=172, txt='Construcción')
        pdf.text(x=145, y=175, txt='(Sujeta a')
        pdf.text(x=145, y=178, txt='restricciones)')

        pdf.text(x=165, y=166, txt='Número de')
        pdf.text(x=166, y=169, txt='Viviendas')
        pdf.text(x=165, y=172, txt='Permitidas:')
        pdf.set_font('Arial', 'B', 8)
        pdf.text(x=13, y=216, txt='Normas por Ordenación:')

        pdf.set_font('Arial', 'B', 8)
        pdf.text(x=16, y=223, txt='Generales')
        pdf.set_text_color(201, 186, 64)
        pdf.text(x=16, y=227, txt='Inf. de la Norma')
        pdf.text(x=16, y=230.5, txt='Inf. de la Norma')
        pdf.text(x=16, y=234, txt='Inf. de la Norma')
        pdf.text(x=16, y=237.5, txt='Inf. de la Norma')
        pdf.text(x=16, y=241, txt='Inf. de la Norma')
        pdf.text(x=16, y=244.5, txt='Inf. de la Norma')
        pdf.text(x=16, y=248, txt='Inf. de la Norma')
        pdf.text(x=16, y=251.5, txt='Inf. de la Norma')
        pdf.text(x=16, y=255, txt='Inf. de la Norma')
        pdf.text(x=16, y=258.5, txt='Inf. de la Norma')
        pdf.text(x=16, y=265, txt='Inf. de la Norma')
        pdf.set_font('Arial', '', 8)
        pdf.set_text_color(0, 0, 0)
        pdf.text(x=40, y=227,
                 txt='1. Coeficiente de Ocupación del Suelo (COS) y Coeficiente de Utilización del Suelo (CUS).')
        pdf.text(x=40, y=230.5, txt='4. Área libre de construcción y recarga de aguas pluviales al subsuelo.')
        pdf.text(x=40, y=234, txt='7. Alturas de edificación y restricciones en la colindancia posterior del predio.')
        pdf.text(x=40, y=237.5, txt='8. Instalaciones permitidas por encima del número de niveles.')
        pdf.text(x=40, y=241, txt='9. Subdivisión de predios.')
        pdf.text(x=40, y=244.5, txt='11. Cálculo del número de viviendas permitidas.')
        pdf.text(x=40, y=248, txt='17. Vía pública y estacionamientos subterráneos.')
        pdf.text(x=40, y=251.5, txt='18. Ampliación de construcciones existentes.')
        pdf.text(x=40, y=255, txt='19. Estudio de impacto urbano.')
        pdf.text(x=40, y=258.5,
                 txt='26. Norma para incentivar la producción de vivienda sustentable, de interés social y popular.')
        pdf.set_text_color(187, 6, 6)
        pdf.text(x=156, y=258.5, txt='SUSPENSIÓN RATIFICADA DE')
        pdf.text(x=40, y=261.5, txt='ACUERDO A LA PUBLICACIÓN DE LA GACETA OFICIAL DE LA CIUDAD DE ACUÑA DE FECHA 21 '
                                    'DE AGOSTO DE 2020')
        pdf.set_text_color(0, 0, 0)
        pdf.text(x=40, y=265,
                 txt='27. De requerimientos para la captación de aguas pluviales y descarga de aguas residuales.')
        # Información

        pdf.set_font('Arial', '', 8)
        pdf.text(x=60, y=60, txt='020_132_05')

        pdf.set_font('Arial', '', 7.5)
        pdf.text(x=23, y=128, txt='"VERSIÓN DE DIVULGACIÓN E INFORMACIÓN, NO')
        pdf.text(x=23, y=131, txt='PRODUCE EFECTOS JURÍDICOS". La consulta y')
        pdf.text(x=23, y=134, txt='difusión de esta información no constituye')
        pdf.text(x=23, y=137, txt='autorización, permiso o licencia sobre el uso de suelo.')
        pdf.text(x=23, y=140, txt='Para contar con un documento de carácter oficial es.')
        pdf.text(x=23, y=143, txt='necesario solicitar a la autoridad competente, la')
        pdf.text(x=23, y=146, txt='expedición del Certificado correspondiente.')
        # pdf.cell(w=50, h=100, txt='"VERSIÓN DE DIVULGACIÓN E INFORMACIÓN, NOPRODUCE EFECTOS JURÍDICOS". La consulta
        # y difusión de esta información no constituye autorización, permiso o licencia sobre el uso de suelo. Para
        # contar con un documento de carácter oficial es necesario solicitar a la autoridad competente, la expedición
        # del Certificado correspondiente', border=0, ln=10, align='C', fill=0)

        # segundo cuadro

        pdf.text(x=112, y=110, txt='Predio Seleccionado')
        pdf.text(x=110, y=134, txt='Este croquis puede no contener las ultimas modificaciones al ')
        pdf.text(x=110, y=137, txt='predio, producto de fusiones y/o subdivisiones llevadas a ')
        pdf.text(x=110, y=140, txt='cabo por el propietario.')



    def datosPredio(self):
        pc = PdfController()
        pdf.set_font('Arial', '', 7.5)
        pdf.text(x=30, y=181, txt=pc.get_usoSuelo())
        pdf.text(x=58, y=181, txt=pc.get_niveles())
        pdf.text(x=65, y=181, txt=pc.get_altura())
        pdf.text(x=90, y=181, txt=pc.get_area())
        pdf.text(x=105, y=181, txt=pc.get_perimetro())
        pdf.text(x=125, y=181, txt=pc.get_densidad())
        pdf.text(x=170, y=181, txt=pc.get_numVivienda())

        pdf.set_font('Arial', '', 8)
        pdf.text(x=50, y=76, txt=pc.get_propietario())
        pdf.text(x=50, y=80, txt=pc.get_colonia())
        pdf.text(x=50, y=84, txt=pc.get_codigoPostal())
        pdf.text(x=50, y=88, txt=pc.get_area())

    def asignacionContenido2(self):
        pdf.add_page()

        self.encabezado()

        # primer cuadro
        pdf.set_font('Arial', 'B', 8)
        pdf.text(x=16, y=18, txt='Particulares')
        # pdf.set_xy(x=13, y=20)
        pdf.set_font('Arial', '', 8)
        pdf.rect(x=13, y=20, w=190, h=10)
        pdf.cell(w=20, h=5, border=0, txt='', ln=1)
        pdf.set_xy(x=15, y=20)
        pdf.set_text_color(201, 186, 64)
        pdf.cell(w=25, h=10, border=0, txt='Info de la Norma')
        pdf.set_text_color(0, 0, 0)
        pdf.multi_cell(w=165, h=10, border=0, txt='Otras disposiciones particulares.')

        # segundo cuadro
        pdf.set_font('Arial', 'B', 8)
        pdf.text(x=16, y=36, txt='Antecedentes')
        pdf.rect(x=13, y=38, w=190, h=10)
        pdf.set_xy(x=16, y=38)
        pdf.set_font('Arial', '', 8)
        pdf.cell(w=190, h=10, border=0, txt='Antecedentes')

        # cuadros de abajo
        # pdf.rect(x=13, y=100, w =190, h= 15)

        # pdf.set_xy(x=13, y=100)
        pdf.set_font('Arial', 'B', 8)
        # pdf.cell(w=190, h=5, border=1, align='C', ln=1)
        pdf.set_xy(x=16, y=50)
        pdf.multi_cell(w=180, h=5, border=0, align='C',
                       txt='*A la superficie máxima de construcción se deberá restar el área resultante de las restricciones y demás limitaciones para la construcción de conformidad a los ordenamientos aplicables')

        pdf.rect(x=13, y=60, w=190, h=15)
        pdf.set_font('Arial', '', 8)
        pdf.set_xy(x=16, y=60)
        pdf.multi_cell(w=185, h=7, border=0, align='J',
                       txt='Cuando los Programas de Desarrollo Urbano determinen dos o más normas de ordenación y/o dos o más normas por vialidad para un mismo inmueble, el propietario o poseedor deberá elegir una sola de ellas, renunciando así a la aplicación de las restantes. ')

        pdf.rect(x=13, y=80, w=190, h=23)
        pdf.set_font('Arial', '', 8)
        pdf.set_xy(x=16, y=80)
        pdf.multi_cell(w=185, h=7, border=0, align='J',
                       txt='El contenido del presente documento es una transcripción de la información de los Programas de Desarrollo Urbano inscritos sobre el registro de Planes y Programas de esta Secretaría , por lo que en caso de existir errores ortográficos o de redacción, será facultada exclusiva de la Secretaría de Desarrollo Urbano y Vivienda proceder a su rectificación.')

        pdf.rect(x=13, y=109, w=190, h=15)
        pdf.set_font('Arial', '', 8)
        pdf.set_xy(x=16, y=109)
        pdf.multi_cell(w=185, h=7, border=0, align='J',
                       txt='Cuando los Programas de Desarrollo Urbano determinen dos o más normas de ordenación y/o dos o más normas por vialidad para un mismo inmueble, el propietario o poseedor deberá elegir una sola de ellas, renunciando así a la aplicación de las restantes. ')
        ahora = datetime.datetime.now()
        pc = PdfController()
        pdf.output('Normatividad de uso de suelo-' + pc.get_propietario() + ahora.strftime("%d%m%Y-%H%M") + '.pdf')
        remove('map.png')
