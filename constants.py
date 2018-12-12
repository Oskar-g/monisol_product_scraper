import os
import datetime

SCRAPED_WEB_NAME = "monisol.es"
WEB_URLS = [
    {
        "url": "https://tienda.monisol.es/bombas-agricolas.html",
        "pages": 304,
        "category": "Bombas Agricolas",
        "start_page": None,
        "end_page": None
    },
    {
        "url": "https://tienda.monisol.es/bombas-industriales.html",
        "pages": 172,
        "category": "Bombas Industriales",
        "start_page": None,
        "end_page": None
    },
    {
        "url": "https://tienda.monisol.es/pulverizacion.html",
        "pages": 58,
        "category": "Pulverizacion",
        "start_page": None,
        "end_page": None
    },
    {
        "url": "https://tienda.monisol.es/espolvoreadores.html",
        "pages": 1,
        "category": "Espolvoreadores",
        "start_page": None,
        "end_page": None
    },
    {
        "url": "https://tienda.monisol.es/repuestos-bertolini.html",
        "pages": 376,
        "category": "Repuestos Bertolini",
        "start_page": None,
        "end_page": None
    }
]

#........................NO EDITAR ESTO........................

now = datetime.datetime.now()
USER_NAME = os.getlogin()
FILE_PATH = "C:/users/" + USER_NAME + "/Desktop"
XLS_FILE_NAME = now.strftime("%Y-%m-%d") + "_Scap_" + SCRAPED_WEB_NAME + ".xlsx"
XLS_FILE = FILE_PATH + "/" + XLS_FILE_NAME

#........................NO EDITAR ESTO........................
