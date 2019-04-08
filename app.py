import pandas as pd
import xlrd

extract = "/home/janaelson/Downloads/clear_02-2019.xls"

tags = [
    {
        'searched_text': 'Ativos em Custódia',
        'header': None,
        'start': None,
        'end': None,
        'end_text': 'VALORIZAÇÃO EM REAIS'
    },
    'VALORIZAÇÃO EM REAIS'
    'MOVIMENTAÇÕES NO PERÍODO',
    'PROVENTOS EM DINHEIRO - PROVISIONADOS',
    'INFORMAÇÕES DE NEGOCIAÇÃO DE ATIVOS'
]

book = xlrd.open_workbook(extract)

# print number of sheets
print (book.nsheets)

# print sheet names
print (book.sheet_names())

# get the first worksheet
first_sheet = book.sheet_by_index(0)

# read a row
# print (first_sheet.row_values(0))
# values = [first_sheet.row_values(i) for i in range(1, first_sheet.nrows)]

# for val in values:
#     print (val)

num_rows = first_sheet.nrows
num_cols = first_sheet.ncols

rows = []

for row_idx in range(1, num_rows):
    row_cells = [first_sheet.cell_value(row_idx, col_idx) for col_idx in range(num_cols) if first_sheet.cell_type(row_idx, col_idx)]
    rows.append(row_cells)
    # print (row_cells.index('GOAU4'))
    # print ("{}: {}".format(row_idx, row_cells))
    # if len(row_cells) and row_cells[0] == 'INFORMAÇÕES DE NEGOCIAÇÃO DE ATIVOS':
    #     print (row_cells[0].index('INFORMAÇÕES DE NEGOCIAÇÃO DE ATIVOS'))

print (rows[9:12])

def split_rows_by_block(idx):
    array = []
    size = len(rows[idx])
    while size > 0:
        print (rows[idx])
        idx = idx + 1
        size = len(rows[idx])
        array.append(rows[idx])
    return array


# idx = 114
split_rows_by_block(114)

# read a cell
# cell = first_sheet.cell(0, 0)
# print (cell)
# print (cell.value)

# read a row slice
# print (first_sheet.row_slice(rowx=0,
#                             start_colx=0,
#                             end_colx=2))
