import constants
from excel import Excel
from scraper import Scraper
from constants import WEB_URLS


def create_link(base_url: str, index: int) -> str:
    return base_url + "?p=" + str(index)


if __name__ == "__main__":
    print('\nIniciando el programa...')

    print("\nGenerando excel...")
    xls = Excel()

    print("\nCargando librerías...")
    scraper = Scraper()

    print("\n########################################################################")
    print("Iniciando scraping...")
    print("########################################################################")

    try:
        for ur in WEB_URLS:
            print('\nCargando categoría:', ur["category"])
            for page in range(int(ur["pages"]) + 1):
                link = create_link(ur["url"], page)
                item_list_data = scraper.scrap_item_list(link)
                xls.write_data(item_list_data)

    except Exception as e:
        print("Error en el proceso", e)
    finally:
        xls.workbook.close()
