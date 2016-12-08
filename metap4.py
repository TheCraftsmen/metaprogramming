import new

class MyClass():
	pass

x = MyClass()

def new_spam(self):
	print 'grafted Spam!'

MyClass.spam = new.instancemethod(new_spam, None, MyClass)

x.spam()