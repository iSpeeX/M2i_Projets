import os
os.environ['TCL_LIBRARY'] = r'C:\Users\Mathieu\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Mathieu\AppData\Local\Programs\Python\Python36\tcl\tk8.6'
import sys
from cx_Freeze import setup,Executable

includefiles = ['tcl86t.dll', 'tk86t.dll', 'RenIT.ini', 'logo.gif', 'view/main.py', 'view/create.py', 'view/list.py', 'classes/regle.py', 'classes/listeregle.py', 'classes/renommage.py']
includes = []
excludes = []
packages = ['os','tkinter']

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name = 'RenIT',
    version = '1.0',
    description = '',
    author = 'Mathieu Foucher',
    options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}}, 
    executables = [Executable('run.py', base=base)]
)

def find_data_file(filename):
	if getattr(sys, 'frozen', False):
		# The application is frozen
		datadir = os.path.dirname(sys.executable)
	else:
		# The application is not frozen
		# Change this bit to match where you store your data files:
		datadir = os.path.dirname(__file__)

	return os.path.join(datadir, filename)