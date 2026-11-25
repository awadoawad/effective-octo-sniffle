
import unittest
from openvrd.hydrology import rational_method


class TestRationalMethod(unittest.TestCase):

    def test_standard_catchment(self):
        self.assertAlmostEqual(
            rational_method(10000, 0.6, 50),
            83.333333,
            places=5
        )

    def test_impervious_surface(self):
        self.assertAlmostEqual(
            rational_method(3600, 1.0, 100),
            100.0
        )

    def test_zero_runoff(self):
        self.assertEqual(
            rational_method(10000, 0, 50), 0
        )

    def test_zero_rainfall(self):
        self.assertEqual(
            rational_method(10000, 0.6, 0), 0
        )

    def test_invalid_area(self):
        with self.assertRaises(ValueError):
            rational_method(-100, 0.6, 50)

    def test_invalid_coefficient(self):
        with self.assertRaises(ValueError):
            rational_method(10000, 1.5, 50)

    def test_negative_rainfall(self):
        with self.assertRaises(ValueError):
            rational_method(10000, 0.6, -50)

    def test_non_finite_input(self):
        with self.assertRaises(ValueError):
            rational_method(float("inf"), 0.6, 50)


if __name__ == "__main__":
    unittest.main()
