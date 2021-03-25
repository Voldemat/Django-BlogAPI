import unittest
from typing import Optional
class ModelTestCase(unittest.TestCase):
	def create_model_and_save_data(self, modelClass, data:dict) -> None:
		self.model = modelClass.objects.create(**data)
		self.data = data

	def check_content_of_model(self, msg:str = None) -> None:
		for key in self.data:
			self.assertEqual(
				getattr(self.model,key).__str__(),
				self.data[key].__str__(),
				msg = msg if msg else f"{key.capitalize()}: {getattr(self.model, key)} != {self.data[key]}!"
			)

	def check_str_method(self,str_field:str, msg:str = None) -> None:
		if not str_field: return None
		self.assertEqual(
			self.model.__str__(),
			getattr(self.model, str_field),
			msg = msg if msg else f'Model __str__ return {self.model.__str__()} expected {getattr(self.model, str_field)}!'
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
