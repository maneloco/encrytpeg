import unittest
from src.dct import to_frequencies, from_frequencies
import random

class TestDCT(unittest.TestCase):
    def test_transformation_equal(self):
        grid = [[0.0] * 8 for _ in range(8)]
        for x in range(8):
            for y in range(8):
                value = random.uniform(0.0, 255.0)
                grid[x][y] = value

        freqs_grid = to_frequencies(grid)
        grid_after_transformation = from_frequencies(freqs_grid)
        
        for x in range(8):
            for y in range(8):
                self.assertAlmostEqual(
                        grid[x][y],
                        grid_after_transformation[x][y],
                        places=6
                        )

if __name__ == "__main__":
    unittest.main()

