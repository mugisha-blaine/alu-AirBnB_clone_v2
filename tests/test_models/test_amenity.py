#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import TestBaseModel
from models.amenity import Amenity


class test_Amenity(TestBaseModel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = Amenity

    def test_name2(self):
        """ """
        new = self.value()
        new.name = "amenity"
        self.assertEqual(type(new.name), str)
