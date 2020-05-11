import os

def printworld():
	print("hello world!")
	print(os.getcwd())
	print(os.path.join("this", "that"))
	print(os.path.join("/root/", "thisDirectory"))

printworld()
