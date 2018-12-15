from constants import WEB_URLS
from excel import Excel
from scraper import Scraper


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

            page = 1
            start_page = 0
            end_page = int(ur["pages"])

            if ur["start_page"] is not None:
                start_page = int(ur["start_page"]) - 1

            if ur["end_page"] is not None:
                end_page = int(ur["end_page"])

            if None is ur["end_page"] or (ur["end_page"] and int(ur["end_page"]) > 0):

                print('\nCARGANDO CATEGORÍA:', ur["category"])
                print("PÁGINA FINAL: ", end_page)

                page += start_page
                while page <= end_page:
                    link = create_link(ur["url"], page)
                    item_list_data = scraper.scrap_item_list(link)
                    xls.write_data(item_list_data)
                    page += 1

    except Exception as e:
        print("Error en el proceso", e)
    finally:
        xls.workbook.close()
