import unittest
class ModelTestCase:
	def create_model(self, modelClass, data:dict) -> None:
		self.model = modelClass.objects.create(**data)
		self.data = data

	def check_content_of_model(self, msg:str = None) -> None:
		for key in self.data:
			self.assertEqual(
				getattr(self.model,key),
				self.data[key],
				msg = msg if msg != None else f'{key.capitalize()}: {getattr(self.model,key)} != {self.data[key]}'
			)












# class BetterModelTestCase(unittest.TestCase):
# 	def setUp(self) -> None:
# 		print(self.__dir__())
# 		metadata:dict = self.get_data(self)
# 		self.model_class, self.data, self.str_field = metadata.values()
# 		self.model = self.model_class.objects.create(**self.data)

# 	def test_content(self):
# 		for key in self.data:
# 			self.assertEqual(
# 				getattr(self.model,key),
# 				self.data[key],
# 				msg = f'{key.capitalize()}: {getattr(self.model,key)} != {self.data[key]}'
# 			)

# 	def test_str_method_of_model(self):
# 		if self.str_field != None:
# 			self.assertEqual(self.model, getattr(self.model, self.str_field))
