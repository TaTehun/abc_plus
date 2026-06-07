import win32com.client
import os
import sys

BASE_DIR = os.path.dirname(sys.executable if getattr(sys, "frozen", False) else os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "abc_plus.xlsx")

excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = False

wb = excel.Workbooks.Open(FILE_PATH)
ws = wb.ActiveSheet

ws.Cells(1, 3).Value = "c value"

row = 2
while ws.Cells(row, 1).Value:
    ws.Cells(row, 3).Value = ws.Cells(row, 1).Value + ws.Cells(row, 2).Value
    row += 1

wb.Save()
excel.Quit()
print("완료")
