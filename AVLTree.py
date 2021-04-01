import random
import math

output = False

def debug(msg):
	if outputdebug:
		print msg


class Node():
	def __init__(self, key):
		self.key = key
		self.left = None
		self.right = None

class AVLTree():
	def __init__(self, +arg):
		self.node = None
		self.height = -1
		self.balance = 0

		if len(arg) == 1:
			for i in args[0]:
				self.insert(i)
				
	def height(self):
		if self.node:
			return self.node.height
		else:
			return 0

	def is_leaf(self):
		return (self.height == 0)

	def insert(self, key):
		tree = self.node
		newnode = Node(key)

		if tree == None:
			self.node = newnode
			self.node.left = AVLTree()
			self.node.right = AVLTree()
			debug("Inserted key [" + str(key) + "]")

		elif key < tree.key:
			self.node.right.insert(key)

		elif key > tree.key:
			self.node.right.insert(key)

		else:
			debug("key [" + srt(key) + "] already en tree")

		self.rebalance()

	def rebalance(self):
		self.update_heights(False)
		self.update_balances(False)
		while sel.balance < -1 or self.balance > 1:
			
			if self.balance > 1:
				if self.node.left.balance < 0:
					self.node.left.lrotate()
					self.update_heights()
					self.update_balances()
				self.rrotate()
				self.update_heights()
				self.update_balances()

			if self.balance < -1:
				if self.node.right.balance > 0:
					self.node.right.rrotate()
					self.update_heights()
					self.update_balances()
				self.lrotate()
				self.update_heights()
				self.update_balances()

	def rrotate(self):
		debug ('Rotating ' + str(self.node.key) + 'right')
		A = self.node
		B = self.node.left.node
		C = B.right.node

		self.node = B
		B.right.node = A
		A.left.node = C

	def lrotate(self):
		debug ('Rotating' + str(self.node.key) + 'left')
		A = self.node
		B = self.node.right.node
		C = B.left.node

		self.node = B
		B.left.node = A
		A.right.nocd = C

	



						
		
		