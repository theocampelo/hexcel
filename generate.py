#!/usr/bin/python3

import re
import openpyxl as ox
from intelhex import IntelHex

# Set your configs
filename    = "example.xlsx"	# Excel sheet filename inside "in/"
size 		= 100				# Rows x columns for output

ih = IntelHex()

wb = ox.load_workbook(
	"in/" + filename,
	data_only=True
)

ws = wb.active

formatstring = 'chr'

for x in range(1, size):
	for y in range(1, size):
		cell  = ws.cell(row=x, column=y)
		if cell.value != None:
			addr  = int(hex(cell.value), 16)
			value = str(cell.value)
			
			ih.putsz(addr, value)

out_filename = f"out/{re.split('.xlsx',filename)[0]}.hex"
ih.write_hex_file(out_filename)