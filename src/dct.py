from typing import List
import math


def to_frequencies(grid: List[List[float]]) -> List[List[float]]:
    freqs = [[0.0] * 8 for _ in range(8)]

    for u in range(8):
        for v in range(8):
            sum_val: float = 0.0

            for x in range(8):
                for y in range(8):
                    sum_val += (grid[x][y] - 128) * cosines_function(x, y, u, v)

            freqs[u][v] = 0.25 * scale_constant(u, v) * sum_val

    return freqs


def from_frequencies(freqs: List[List[float]]) -> List[List[float]]:
    pixels = [[0.0] * 8 for _ in range(8)]

    for x in range(8):
        for y in range(8):
            sum_val: float = 0.0

            for u in range(8):
                for v in range(8):
                    sum_val += scale_constant(u, v) * freqs[u][v] * cosines_function(x, y, u, v)

            pixel_val = (0.25 * sum_val) + 128
            pixels[x][y] = max(0.0, min(255.0, pixel_val))

    return pixels

def cosines_function(x: float, y: float, u: float, v: float) -> float:
   cos_x = math.cos(((2 * x + 1) * u * math.pi) / 16)
   cos_y = math.cos(((2 * y + 1) * v * math.pi) / 16)
   return cos_x * cos_y

def scale_constant(u: float, v: float) -> float:
    cu = 1.0 / math.sqrt(2) if u == 0 else 1.0
    cv = 1.0 / math.sqrt(2) if v == 0 else 1.0
    return cu * cv
