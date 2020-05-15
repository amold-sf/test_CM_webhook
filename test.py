import os

def printworld():
	print("hello world!")
	print(os.getcwd())
	print(os.path.join("this", "that"))
	print("test")
	print(os.path.join('/root/','someFile'))

printworld()
