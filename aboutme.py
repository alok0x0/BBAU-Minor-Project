from tkinter import messagebox as tmsg

class Mydetails:
	def __init__(self):
		self.info = "Developer name is Alok Pratap Singh and Nitesh Kumar I am currently pursuing M.Sc degree in Information Technology, Babasaheb Bhimrao Ambedkar Universty, Lucknow."
	def show(self, label):
		tmsg.showinfo(label,self.info)
