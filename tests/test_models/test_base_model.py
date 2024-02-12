import unittest
from models.base_model import BaseModel
from datetime import datetime
import json


class TestBaseModel(unittest.TestCase):
    def test_attributes(self):
        my_model = BaseModel()
        self.assertTrue(hasattr(my_model, 'id'))
        self.assertTrue(hasattr(my_model, 'created_at'))
        self.assertTrue(hasattr(my_model, 'updated_at'))

    def test_str_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        expected_str = "[BaseModel] ({}) {}".format(my_model.id, my_model.__dict__)
        self.assertEqual(str(my_model), expected_str)

    def test_save_method(self):
        my_model = BaseModel()
        old_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(old_updated_at, my_model.updated_at)

    def test_to_dict_method(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        expected_dict = {
            'id': my_model.id,
            '__class__': 'BaseModel',
            'created_at': my_model.created_at.isoformat(),
            'updated_at': my_model.updated_at.isoformat(),
            'name': 'My First Model',
            'my_number': 89
        }

        self.assertDictEqual(my_model.to_dict(), expected_dict)

    def test_json_representation(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89

        my_model_json = my_model.to_dict()
        json_str = json.dumps(my_model_json)
        expected_json_str = '{"id": "' + my_model.id + '", "__class__": "BaseModel", "created_at": "' + my_model.created_at.isoformat() + '", "updated_at": "' + my_model.updated_at.isoformat() + '", "name": "My First Model", "my_number": 89}'

        self.assertEqual(json_str, expected_json_str)


if __name__ == '__main__':
    unittest.main()
