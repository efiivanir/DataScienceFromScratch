from typing import List


Vector = List[float]
height_weight_age = [70, # inches,
                    170, # pounds,
                    40 ] # years
grades = [95, # exam1
            80, # exam2
            75, # exam3
            62 ] # exam4

def add(v: Vector, w: Vector) -> Vector:
    """Adds corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i + w_i for v_i, w_i in zip(v, w)]



def subtract(v: Vector, w: Vector) -> Vector:
    """Subtracts corresponding elements"""
    assert len(v) == len(w), "vectors must be the same length"
    return [v_i - w_i for v_i, w_i in zip(v, w)]

assert subtract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]
assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]
