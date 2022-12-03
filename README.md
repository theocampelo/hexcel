# HEXCEL v0.1

Generate IntelHex HEX files from an Excel sheet of integers (XLSX)

## Python3 Module Requirements

* IntelHex
* Openpyxl

## Usage

First, put the xlsx file inside the ```in/``` directory.

Secondly, set your filename in ```generate.py``` to the name of the file you've just put inside the input dir, as such:
```
filename = "example.xlsx"
```

Then, define the sheet size (rows x columns), or the size of the output you want to be written in the .hex file output. Default value is 100.
```
size = 100
```

Finally, run the program by typing:
```
python3 generate.py
```

Your .hex file should be in the ```out/``` directory, with the same filename as the input file.

**Example .xlsl and .hex files can be found in the ```example``` directory for general purposes.**
