from unittest import TestCase
from digital_assets.chairs import Chair, CantStandException


class TestChair(TestCase):
    def setUp(self) -> None:
        self.chair = Chair(material='wood', legs=3, color='blue')

    def test_chair_can_stand(self):
        invalid_params = {'material': 'wood', 'legs': 2, 'color': 'green'}
        with self.assertRaises(CantStandException):
            Chair(**invalid_params)
