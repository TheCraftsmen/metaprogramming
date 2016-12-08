#modulo sintetico

import new, sys
my_module = new.module( 'synthetic', 'Fake module.')

"""
from types import ModuleType
mi_modulo = ModuleType('glassblower')
"""

def my_function():
	print 'hello from my_function()'

my_module.eggs = my_function
sys.modules['synthetic'] = my_module
#borra la memoria
del new, sys, my_module, my_function

import synthetic
synthetic.eggs()
