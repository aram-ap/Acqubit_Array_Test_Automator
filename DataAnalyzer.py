import tkinter as tk
import re
import pandas as pd
from tkinter import filedialog as fd
import numpy as np
import matplotlib.pyplot as plt

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

def getData(path: str):
    file = np.loadtxt(path, delimiter=',')
    return file

def normalize(df):
    return df / np.linalg.norm(df)

def plot(data):
    plt.style.use('_mpl-gallery-nogrid')

    X, Y = np.meshgrid(np.linspace(0,31), np.linspace(0,31))
    fig, ax = plt.subplots()
    ax.imshow(data)
    plt.show()

def callback():
    name = fd.askopenfilename();

    if(len(name) < 1):
        return "No file passed"

    dict = testType(name)
    for key in dict.keys():
        print(key, ": ", dict[key])

    file = getData(name)
    file = normalize(file)
    print(file)
    plot(file)



def main():
    root = tk.Tk()
    root.geometry("400x300")
    root.resizable(False,False)
    button = tk.Button(text='Click to Open File', command=callback, height=5).pack(fill=tk.X)
    root.mainloop()

if __name__ == "__main__":
    main()


