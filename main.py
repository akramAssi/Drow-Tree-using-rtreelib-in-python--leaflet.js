import random
from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from akramRtree import RTree, Rect, RTreeGuttman
from akramRtree import RStarTree, Rect
from akramRtree.diagram import create_rtree_diagram0
import numpy as np
import webbrowser,os
import pandas as pd
import sys
sys.path.append("/path/to/script/file/directory/")

new = 2


def openp():
    webbrowser.open('file://' + os.path.realpath("index.html"))

window = Tk()
window.title("program for generate random R-tree")
# window.geometry('400x400')
# window.configure(background = "grey")
v = tk.IntVar()
v.set(1)  # initializing the choice, i.e. Python

languages = [
    ("R-TreeGuttman"),
    ("R*-Tree"),
]
x = 0




mix = 2
mxx = 4
len = 15

list_rand_rects = np.array([[0, 0, 0, 0]])

ulist=pd.read_csv("mapv.csv")
ulist=ulist.set_index('name')
llco = ulist.copy()


def generate():
    global list_rand_rects
    global mxx
    global mix
    global len
    try:
        len = int(a1.get())
    except:
        len = 15

    width = 100
    height = 100
    x1 = random.randrange(width)
    y1 = random.randrange(height)
    x2 = x1 + random.randrange(width)
    y2 = y1 + random.randrange(height)
    list_rand_rects = np.array([[x1, y1, x2, y2]])
    for i in range(1, len):
        x1 = random.randrange(width)
        y1 = random.randrange(height)
        x2 = x1 + random.randrange(width)
        y2 = y1 + random.randrange(height)
        list_rand_rects = np.append(list_rand_rects, [[x1, y1, x2, y2]], axis=0)
    try:
        mxx = int(b1.get())
    except:
        mxx = 4
    vv = list(range(0, len))
    tk.Label(window, text="select node to delete").grid(row=5, column=0, sticky=E)
    var = StringVar(window)
    var.set("0")
    option = OptionMenu(window, var, *vv)
    option.grid(row=5, column=1)
    tk.Button(window, text="Delete", command=lambda: delete(option, var),
              width=20, height=2).grid(row=5, column=3, pady=4)


def delete(option, var):
    x = var.get()
    option["menu"].delete(x)
    var.set("no")
    global list_rand_rects
    list_rand_rects[(int(x))] = np.array([[-1, -1, -1, -1]])# =np.delete(list_rand_rects,(int(x)),0)
    Guttman(mxx, len)
    Star(mxx, len)

def edelete(option, var):
    x = var.get()
    option["menu"].delete(x)
    var.set("no")
    global llco
    llco= llco.drop([x])
    gexample()
    sexample()



def Guttman(mx=4, r=15):
    t = RTreeGuttman(max_entries=mx,min_entries=int(mx/2))
    for rect in range(0, r):
        if np.array_equal(list_rand_rects[int(rect)], np.array([-1, -1, -1, -1]))==TRUE:
            continue
        x = Rect(list_rand_rects[rect][0], list_rand_rects[rect][1], list_rand_rects[rect][2], list_rand_rects[rect][3])
        t.insert(str(rect), x)

    create_rtree_diagram0(t, filename="R-TreeGuttman")


def Star(mx=4, r=15):
    ts = RStarTree(max_entries=mx,min_entries=int(mx/2))
    for rect in range(0, r):
        if np.array_equal(list_rand_rects[int(rect)], np.array([-1, -1, -1, -1])) == TRUE:
            continue
        x = Rect(list_rand_rects[rect][0], list_rand_rects[rect][1], list_rand_rects[rect][2], list_rand_rects[rect][3])
        ts.insert(str(rect), x)
    create_rtree_diagram0(ts, filename="R*-tree")


def gexample():
    try:
        maxe=int(n.get())
    except:
        maxe=4
    t = RTreeGuttman(max_entries=maxe)
    for label, row in llco.iterrows():
        t.insert(label, Rect(row['x1'],row['y1'],row['x2'],row['y2']))


    create_rtree_diagram0(t, filename="R-TreeGuttman")


def sexample():
    try:
        maxs=int(n.get())
    except:
        maxs=4
    st = RStarTree(max_entries=maxs,min_entries=int(maxs/2))
    for label, row in llco.iterrows():
        st.insert(label, Rect(row['x1'],row['y1'],row['x2'],row['y2']))

    create_rtree_diagram0(st, filename="R*-tree")
def reload(ob):
    ob.destroy()
    global llco
    llco = ulist.copy()
    var = StringVar(window)
    var.set("it")
    vsz = list(llco.index)
    option = OptionMenu(window, var, *vsz)
    option.config(width=17)
    option.grid(row=10, column=1)

fontStyle = tkFont.Font(family="Lucida Grande", size=25)
tk.Label(window, text="program for generate random R-tree",font=fontStyle).grid(row=1, column=1,columnspan=3, pady=15, padx=6)
a = tk.Label(window, text="number object").grid(
    row=2, column=0, pady=15, padx=6)
b = tk.Label(window, text="max entries").grid(
    row=2, column=3, pady=15, padx=6)
a1 = tk.Entry(window)
a1.grid(row=2, column=1, padx=6, pady=15)
b1 = tk.Entry(window)
b1.grid(row=2, column=4, padx=6, pady=15,sticky=W)

tk.Button(window, wraplength=200, text="generate", command=lambda: generate(),
          width=13, height=2).grid(row=4, column=0, pady=15, padx=10)

tk.Button(window, wraplength=200, text="generate R-TreeGuttman", command=lambda: Guttman(mxx, len),
          width=20, height=2).grid(row=4, column=1, columnspan=1, pady=4)
tk.Button(window, wraplength=200, text="generate R*-tree", command=lambda: Star(mxx, len),
          width=20, height=2).grid(row=4, column=2, columnspan=2, pady=4, padx=10)

w = tk.Canvas(window, width=820, height=20)
w.grid(row=6, column=0,columnspan=5)
w.create_line(10, 10, 810 , 10 ,fill="black")
tk.Label(window,text="example diagram for building najah university: ").grid(row=7,sticky=W, column=0,columnspan=2,padx=4)
tk.Label(window, text="max entries").grid(
    row=8, column=0, pady=15, padx=6)
n = tk.Entry(window)
n.grid(row=8, column=1, padx=6, pady=15,sticky=W)
tk.Button(window,  text="R-TreeGuttman", command=lambda: gexample(), width=20, height=2).grid(row=9, column=0, columnspan=1, pady=4,padx=10)
tk.Button(window,  text="R*-tree",
          command=lambda: sexample(), width=20,height=2).grid(row=9, column=1, columnspan=2 )

tk.Label(window, text="select node to delete").grid(row=10, column=0, sticky=E)
var = StringVar(window)
var.set("it")
vsz=list(llco.index)
option = OptionMenu(window, var, *vsz)
option.config(width=17)
option.grid(row=10, column=1)
tk.Button(window, text="Delete", command=lambda: edelete(option, var), width=20, height=2).grid(row=10, column=3, pady=4)
tk.Button(window, text="Reload", command=lambda: reload(option), width=20, height=2).grid(row=10, column=4, pady=4)
tk.Button(window,  justify=LEFT, text="visualize for building najah university on map",
          command=lambda: openp(), width=40,height=2).grid(row=11,column=0, columnspan=3, pady=6)

fontStyle = tkFont.Font(family="Lucida Grande", size=17)
tk.Label(window, text="Advanced database",font=fontStyle,fg='#777').grid(row=13, column=0, pady=3, padx=13,sticky=W)
tk.Label(window, text="Hussam Abdel Halim",font=fontStyle,fg='#777').grid(row=14, column=0, pady=3, padx=6,sticky=W)
tk.Label(window, text="Akram Assi",font=fontStyle,fg='#777').grid(row=13, column=4, pady=3, padx=13,sticky=W)
tk.Label(window, text="Hamza Shakshir",font=fontStyle,fg='#777').grid(row=14, column=4, pady=3, padx=6,sticky=W)
fontX = tkFont.Font(family="Lucida Grande", size=12)
tk.Label(window, text=u"\u00a9"+"2020",font=fontX,fg='#777').grid(row=14, column=1,columnspan=3, pady=3, padx=6)
window.mainloop()
