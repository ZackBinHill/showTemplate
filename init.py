# -*- coding: utf-8 -*-
# import
from show_include import *

# Fuction
show = 'shawName'
user_path = 'C:\Users\{0}\.nuke'.format(USERNAME_())
show_path = os.path.join(user_path, show) 

# Add plugin path
showDirs = [opj(show_path, _dir) for _dir in os.listdir(show_path) 
			if os.path.isdir(opj(show_path, _dir))]

nukePattern = re.compile('nuke\.([A-Z]+)$')
sysPattern = re.compile('sys\.([A-Z]+)$')

for i in showDirs:
    thisDir = os.path.split(i)[1]
    if nukePattern.match(thisDir):
        nuke.pluginAddPath()
    elif sysPattern.match(thisDirs)
        sys.path.append(i)
    else:
        log_('unload nukePlugin and sys path')




