#!/usr/bin/python3

import struct
import openpyxl as ox
from intelhex import IntelHex

# Nome do arquivo excel
filename = "hexcel.xlsx"

ih = IntelHex()

wb = ox.load_workbook(filename, data_only=True)
ws = wb.active

formatstring = 'chr'

for x in range(1,100):
	for y in range(1,100):
		cell  = ws.cell(row=x, column=y)
		if cell.value != None:
			addr  = int(hex(cell.value), 16)
			value = str(cell.value)
			
			ih.putsz(addr, value)

# Nome do arquivo de saída .hex			
ih.write_hex_file("out/out.hex")