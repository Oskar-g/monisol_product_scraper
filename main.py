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

            page = 1
            start_page = 0
            end_page = int(ur["pages"])

            if ur["start_page"] is not None:
                start_page = int(ur["start_page"])
            if ur["end_page"] is not None:
                if ur["end_page"] == ur["start_page"]:
                    end_page = int(ur["start_page"])
                else:
                    end_page -= int(ur["end_page"])

            if ur["end_page"] and int(ur["end_page"]) > 0:

                page += (start_page - 1)
                while page <= end_page:
                    link = create_link(ur["url"], page)
                    item_list_data = scraper.scrap_item_list(link)
                    xls.write_data(item_list_data)
                    page += 1

    except Exception as e:
        print("Error en el proceso", e)
    finally:
        xls.workbook.close()
