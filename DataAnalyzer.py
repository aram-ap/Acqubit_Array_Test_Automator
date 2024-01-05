import tkinter as tk
import re
import pandas as pd
from tkinter import filedialog as fd


def split(delimiters, string, maxsplit=0):
    import re
    regex_pattern='|'.join(map(re.escape, delimiters))
    return re.split(regex_pattern, string, maxsplit)

def testType(path: str):
    delimiters = "_","-","."
    paths = path.split('/')
    filename = paths[-1]

    name_breakdown = split(delimiters, filename)
    wafer_id = name_breakdown[1]
    arr_id = name_breakdown[3][0:2]
    diameter = name_breakdown[3][2:]
    test_type = name_breakdown[-2]

    dict = {
        "filepath"  : path,
        "name"      : filename,
        "wafer_id"  : wafer_id,
        "array_id"  : arr_id,
        "diameter"  : diameter,
        "test_type" : test_type
    }

    return dict

def callback():
    name = fd.askopenfilename();
    print(testType(name))

def main():
    root = tk.Tk()
    root.geometry("400x300")
    root.resizable(False,False)
    button = tk.Button(text='Click to Open File', command=callback).pack(fill=tk.X)
    root.mainloop()

if __name__ == "__main__":
    main()


