import uuid

class MangoDB(object):
	def __init__(self):
		self.__set_default()
	
	def __set_default(self):
		self.db =  {'default': {'version': '1.0', 'db': 'mangodb', 'uuid':uuid.uuid4()},'temperatures': {1:50, 2:100, 3:120}}
	
	def add_collection(self, name):
		self.db[name] = dict()
		return self

	def update_collection(self, name, values):
		return self.db[name].update(values)

	def remove_collection(self, name, values):
		for value in values:
			del self[name][value]
		return self

	def get_collection_size(self, collection_name): #TODO
		this = len(self.db[collection_name])
		return this
   
	def list_collections(self): 
		collections = []
		for collection in self:
			collections.append(self[collection])
		return collections

	def to_json(self, collection_name):
		return str(self[collection_name])

	def wipe(self):
		self = self.__set_default()
		return self

	def get_collection_names(self):
		return self.db.keys()





######################


test_scores = [99,89,88,75,66,92,75,94,88,87,88,68,52]
new = dict(enumerate(test_scores))
data = MangoDB()
data.add_collection('testscores')

data.get_collection_size('testscores')
print(data.list_collections)
uuid.uuid4()
data.wipe()
uuid.uuid4()