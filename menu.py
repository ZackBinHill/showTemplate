# -*- coding: utf-8 -*-
# import
from show_global import *

# function
# ------------------------- NUKE GUI ----------------------------------------# 
if not nuke_GUI:
    log_('\n\n')
    for i in nuke.pluginPath():
        log_('init:pluginPath  ' + i)
    log_('\n\n')
    for i in sys.path:
        log_('init:syspath  ' + i)
    log_('\n\n')



# ------------------------- NUKE TOOLBAR ------------------------------------# 
show_menu = nuke.addMenu('Nodes')
show_menu.addCommand('Refresh',
					 'execfile(os.path.join(show_path, 'menu.py'))')




