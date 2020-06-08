from cx_Freeze import setup, Executable 
import cx_Freeze
import tkinter 
from akramRtree import RTree, Rect, RTreeGuttman
from akramRtree import RStarTree, Rect
from akramRtree.diagram import create_rtree_diagram0
import numpy
import webbrowser,os
import pandas
import sys

setup(name = "GeeksforGeeks" , 
	version = "0.1" , 
	description = "" , 
	executables = [Executable("main.py",base="Win32GUI")])
