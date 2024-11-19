import openpyxl
wb = openpyxl.Workbook()
from openpyxl.styles import PatternFill
b = "1E3A5F"
r = "D32F2F"
br = "6E4B3A"
t = "F1C27D"
y = "FFEB3B"

pixel_art = [
[b, b, b, b, b, b, b, b, b, b, b, b, b, b]
[b, b, b, b, r, r, r, r, r, b, b, b, b, b]
[b, b, b, r, r, r, r, r, r, r, r, r, b, b]
[b, b, b, br, br, br, t, t, br, t, b, b, b, b]
[b, b, br, t, br, t, t, t, br, t, t, t, b, b]
[b, b, br, t, br, br, t, t, t, br, t, t, t, b]
[b, b, br, br, t, t, t, t, br, br, br, br, b, b]
[b, b, b, t, t, t, t, t, t, t, t, b, b, b]
[b, b, b, br, br, r, br, br, r, b, b, b, b, b]
[b, b, br, br, br, r, r, r, r, br, br, br, b, b]
[b, br, br, br, r, y, r, r, y, r, ]
[]
[]
[]
[]
[]
[]
[]

]


wb.save("PixelArt.xlsx")