from unittest import TestCase
from digital_assets.chairs import Chair, CantStandException


class TestChair(TestCase):
    def setUp(self) -> None:
        self.chair_blue = Chair(material='wood', legs=3, color='blue')
        self.chair_red = Chair('wood', 4, 'red')

    def test_chair_can_stand(self):
        invalid_params = {'material': 'wood', 'legs': 2, 'color': 'green'}
        with self.assertRaises(CantStandException):
            Chair(**invalid_params)

    def test_add_capacity(self):
        self.assertEqual(self.chair_blue.capacity, 1)

        # self.chair_blue is blue, it most raise an exception if we try to add more people

        with self.assertRaises(OnlyOnePersonException):
            self.chair_blue.set_capacity(2)

        self.assertTrue(self.chair_red.set_capacity(3))

        self.assertEqual(self.chair_red.capacity, 3)
