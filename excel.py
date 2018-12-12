import xlsxwriter
from constants import XLS_FILE


class Excel:
    def __init__(self):
        self.workbook = xlsxwriter.Workbook(XLS_FILE)
        self.worksheet = self.workbook.add_worksheet()
        self.actual_row = 0
        self.col_names = [
            "referencia",
            "nombre",
            "imagen",
            "descripcion",
        ]

        self.__write_headers()

    def __write_headers(self):
        row = 0
        col = 0

        for header in self.col_names:
            self.worksheet.write(row, col, header)
            col += 1

        self.actual_row = 1

    def __write_row(self, element: dict):
        print(element)
        col = 0
        for value in list(element.values()):
            self.worksheet.write(self.actual_row, col, value)
            col += 1

        self.actual_row += 1

    def write_data(self, item_list: list):
        print("\nEscribiendo datos en excel...")
        for element in item_list:
            self.__write_row(element)
