'''
Assignment #3

1. Add / modify code ONLY between the marked areas (i.e. "Place code below"). Do not modify or add code elsewhere.
2. Run the associated test harness for a basic check on completeness. A successful run of the test cases does not guarantee accuracy or fulfillment of the requirements. Please do not submit your work if test cases fail.
3. To run unit tests simply use the below command after filling in all of the code:
	python 03_assignment.py
  
4. Unless explicitly stated, please do not import any additional libraries but feel free to use built-in Python packages
5. Submissions must be a Python file and not a notebook file (i.e *.ipynb)
6. Do not use global variables
7. Make sure your work is committed to your master branch in Github
8. Use the test cases to infer requirements wherever feasible


'''
import csv, json, math, pandas as pd, requests, unittest, uuid

# ------ Create your classes here \/ \/ \/ ------

# Box class declaration below here
class Box(object):

	"""A Box Object """
	def __init__(self, length, width):
		self._width = width
		self._length = length
	
	def get_length(self):
		return self._length
		
	def get_width(self):
		return self._width
	
	
	def render(self):
		for x in range(length):
			for y in range(width):
				print("*")

	def invert(self):
		self._length, self._width = self._width, self._length
		return self

	def get_area(self):
		self._area = self._length*self._width
		return self._area


	def get_perimeter(self):
		self.perimeter = 2 * (length + width)
		return self._perimeter

	def double(self):
		other = self
		self._width = self._width + other._width
		self._length = self._length + other._length
		return self

	def __eq__(self, other):
		test = (self._length == other._length and self._width == other._width) 
		return test


	def print_dim(self):
		print("The length is: ", self._length)
		print("The width is: ", self._width)
		
	def get_dim(self):
		dim = (self._length, self._width)
		return dim
	
	def combine(self, other):
		self._width = self._width + other._width
		self._length = self._length + other._length
		return self
	

	def get_hypot(self):
		hypot = (self._length**2 + self._width **2 )**.5
		return hypot

#### Mango DB class here

class MangoDB(object):
	def __init__(self):
		self.__set_default()
	
	def __set_default(self):
		self.__db =  {'default': {'version': '1.0', '__db': 'mango__db', 'uuid':uuid.uuid4()}}
	
	def display_all_connections(self):
		for collection in self:
			print(collection)

	def add_collection(self, name):
		self.__db[name] = dict()
		return self

	def update_collection(self, name, values):
		return self.__db[name].update(values)

	def remove_collection(self, name, values):
		for value in values:
			del self[name][value]
		return self

	def get_collection_size(self, collection_name): #TODO
		this = len(self.__db[collection_name])
		return this
   
	def list_collections(self): 
		collections = []
		for collection in self:
			collections.append(self[collection])
		return collections

	def to_json(self, collection_name):
		return json.dumps(self.__db[collection_name])

	def wipe(self):
		self = self.__set_default()
		return self

	def get_collection_names(self):
		return list(self.__db.keys())

def exercise01():

	box1 = Box(5,10)
	box2 = Box(3,4)
	box3 = Box(5,10)

	box1.print_dim
	box2.print_dim
	box3.print_dim

	print(box1==box2)
	print(box1==box3)
	box1.combine(box3)
	print(box1.get_dim())
	box2.double()
	print(box2.get_dim())
	box1.combine(box2)
	print(box1.get_dim())
	for i in [0,1]:
		print(box2.get_dim()[i])

	return box1, box2, box3

def exercise02():
	test_scores = [99,89,88,75,66,92,75,94,88,87,88,68,52]
	new = dict(str(enumerate(test_scores)))
	data = MangoDB()
	data.add_collection('testscores')

	data.get_collection_size('testscores')
	print(data.list_collections)
	uuid.uuid4()
	data.wipe()
	uuid.uuid4()

# def exercise03():
# 	'''
# 	1. Avocado toast is expensive but enormously yummy. What's going on with avocado prices? Read about avocado prices on Kaggle (https://www.kaggle.com/neuromusic/avocado-prices/home)
# 	2. Load the included avocado.csv file and display every line to the screen
# 	3. Use the imported csv library
	
# 	'''

# 	# ------ Place code below here \/ \/ \/ ------

# 	with open("avocado.csv") as file:
# 		data = csv.reader(file)
# 		for row in data:
# 			print(row[1])
# 	# ------ Place code above here /\ /\ /\ ------

# class TestAssignment3(unittest.TestCase):
# 	def test_exercise01(self):
# 		print('Testing exercise 1')
# 		b1, b2, b3 = exercise01()
# 		self.assertEqual(b1.get_length(),16)
# 		self.assertEqual(b1.get_width(),28)
# 		self.assertTrue(b1==Box(16,28))
# 		self.assertEqual(b2.get_length(),6)
# 		self.assertEqual(b2.get_width(),8)
# 		self.assertEqual(b3.get_length(),5)
# 		self.assertEqual(b2.get_hypot(),10)
# 		self.assertEqual(b1.double().get_length(),32)
# 		self.assertEqual(b1.double().get_width(),112)
# 		self.assertTrue(6 in b2.get_dim())
# 		self.assertTrue(8 in b2.get_dim())
# 		self.assertTrue(b2.combine(Box(1,1))==Box(7,9))

	def test_exercise02(self):
		print('Testing exercise 2')
		__db = MangoDB()
		self.assertEqual(__db.get_collection_size('default'),3)
		self.assertEqual(len(__db.get_collection_names()),1)
		self.assertTrue('default' in __db.get_collection_names() )
		__db.add_collection('temperatures')
		self.assertTrue('temperatures' in __db.get_collection_names() )
		self.assertEqual(len(__db.get_collection_names()),2)
		__db.update_collection('temperatures',{1:50})
		__db.update_collection('temperatures',{2:100})
		self.assertEqual(__db.get_collection_size('temperatures'),2)
		self.assertTrue(type(__db.to_json('temperatures')) is str)
		self.assertEqual(__db.to_json('temperatures'),'{"1": 50, "2": 100}')
		__db.wipe()
		self.assertEqual(__db.get_collection_size('default'),3)
		self.assertEqual(len(__db.get_collection_names()),1)
		
	def test_exercise03(self):
		print('Exercise 3 not tested')
		exercise03()
	 

if __name__ == '__main__':
	unittest.main()
