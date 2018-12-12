import bs4 as bs
import urllib.request


class Scraper:

    def __init__(self):
        self.current_html = None

    def __parse_page(self, url) -> bs.BeautifulSoup:
        page = urllib.request.urlopen(url)

        if None is page:
            raise Exception("web no encontrada:", page)

        web_code = page.read()
        return bs.BeautifulSoup(web_code, 'lxml')

    #    def get_web_data(self):

    def scrap_item_list(self, url: str) -> list:
        print("\nScrapeando página:", url)
        item_list_data = []
        item_list_page_code = self.__parse_page(url)
        items = item_list_page_code.select('.product-image')
        for item in items:
            item_url = item.get('href')
            item_page_code = self.__parse_page(item_url)
            print("Recabando datos del elemento:", item_url)
            item_data = self.__get_item_data(item_page_code)
            item_list_data.append(item_data)

        return item_list_data

    def __get_item_data(self, item_page_code: bs.BeautifulSoup) -> dict:
        item = {'referencia': self.__get_item_reference(item_page_code),
                'nombre': self.__get_item_name(item_page_code),
                'imagen': self.__get_item_image(item_page_code),
                'descripcion': self.__get_item_description(item_page_code)}

        return item

    def __get_item_reference(self, item_page_code: bs.BeautifulSoup) -> str:
        tag = item_page_code.select_one('div.product-name p')
        text = str(tag.get_text())
        reference = text.replace("Código:", "")

        return reference

    def __get_item_name(self, item_page_code: bs.BeautifulSoup) -> str:
        tag = item_page_code.select_one('.h1')
        name = str(tag.get_text())

        return name

    def __get_item_image(self, item_page_code: bs.BeautifulSoup) -> str:
        tag = item_page_code.select_one('#image-main')
        image = str(tag.get('src'))

        return image

    def __get_item_description(self, item_page_code: bs.BeautifulSoup) -> str:
        tag = item_page_code.select_one('div.short-description')
        text = str(tag.get_text())
        description = text.strip()
        return description
