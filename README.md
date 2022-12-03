# HEXCEL v0.1

Generate IntelHex HEX files from Excel sheets (XLSX)

## Python3 Module Requirements

* IntelHex
* Openpyxl

## Usage

First, define the filename in generate.py:
```
filename = "example.xlsx"
```

Optionally, set the output name for the .hex file:
```
ih.write_hex_file("out/example.hex")
```

Then, run the program by typing:
```
python3 generate.py
```

Your .hex file should be in the ```out/``` directory.
