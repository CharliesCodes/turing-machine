# Python implementation of the Turing-machine

This module uses excel spreadsheets for instructions

## How to use
**If you want to use your own instructions, do the following steps:**

1. Add a new Excel sheet
2. Copy and paste header into first line
3. Add the sheetname into the beginning of the Python Code
4. Add a binary start sequence into the tape variable

``` py
instructions = <NAME OF YOUR SHEET>
df = pd.read_excel('instructions.xlsx', header=0,
                   sheet_name=instructions).astype("string")

tape = list("#<BINARY NUMBERS YOU WANT TO START WITH>#")
```
