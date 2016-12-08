#clase sintetica

def spam(self, x):
	return 'hello spam(%s).' % x

def eggs(self):
	return 'hello eggs().'

d = dict( spam = spam, eggs = eggs)


SyntheticClass = type( 'SyntheticClass', (), d)

obj = SyntheticClass()

print obj.spam(7), obj.eggs()
