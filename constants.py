import os
import datetime

now = datetime.datetime.now()

USER_NAME = os.getlogin()
FILE_PATH = "C:/users/" + USER_NAME + "/Desktop"
SCRAPED_WEB_NAME = "monisol.es"
XLS_FILE_NAME = now.strftime("%Y-%m-%d") + "_Scap_" + SCRAPED_WEB_NAME + ".xlsx"
XLS_FILE = FILE_PATH + "/" + XLS_FILE_NAME

WEB_URLS = [
    {"url": "https://tienda.monisol.es/bombas-agricolas.html", "pages": 304, "category": "Bombas Agricolas"},
    {"url": "https://tienda.monisol.es/bombas-industriales.html", "pages": 172, "category": "Bombas Industriales"},
    {"url": "https://tienda.monisol.es/pulverizacion.html", "pages": 58, "category": "Pulverizacion"},
    {"url": "https://tienda.monisol.es/espolvoreadores.html", "pages": 1, "category": "Espolvoreadores"},
    {"url": "https://tienda.monisol.es/repuestos-bertolini.html", "pages": 376, "category": "Repuestos Bertolini"}
]
''' 
'''

''' URLS FOR TESTING
WEB_URLS = [
    {"url": "https://tienda.monisol.es/bombas-agricolas.html", "pages": 1, "category": "Bombas Agricolas"},
    {"url": "https://tienda.monisol.es/bombas-industriales.html", "pages": 1, "category": "Bombas Industriales"},
    {"url": "https://tienda.monisol.es/pulverizacion.html", "pages": 1, "category": "Pulverizacion"},
    {"url": "https://tienda.monisol.es/espolvoreadores.html", "pages": 1, "category": "Espolvoreadores"},
    {"url": "https://tienda.monisol.es/repuestos-bertolini.html", "pages": 1, "category": "Repuestos Bertolini"}
]
'''
