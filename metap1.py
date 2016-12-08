#funcion sinteticA

d = {}
print d.keys()
exec '''\
def spam(z):
	return z*z + 1
''' in d
exec '''\
def minus(z):
	return z*z - 1
''' in d
print d.keys()
spamv = d['spam']
print spamv(3)
