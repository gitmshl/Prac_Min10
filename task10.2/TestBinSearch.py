import unittest
import random
from binsearch import BinSearch

class TestBinSearch(unittest.TestCase):
    
    def setUp(self):
        self.bs = BinSearch()
        self.arr = []

    def test_empty_arr(self):
        key = random.randrange(-10, 10)
        self.assertEqual(self.bs.search([], key), -1, "Найден элемент в пустом массиве!")

    def test_non_empty_arr_true(self, size=10):
        arr = [random.randrange(-100, 100) for _ in range(size)]
        self.arr = sorted(arr)
        key_pos = random.randrange(0, len(arr))
        self.assertEqual(self.bs.search(self.arr, self.arr[key_pos]), key_pos)

    def test_non_empty_arr_false(self, size=10):
        arr = [random.randrange(-100, 100) for _ in range(size)]
        self.arr = sorted(arr)
        self.assertEqual(self.bs.search(self.arr, arr[0] - 10), -1)
        self.assertEqual(self.bs.search(self.arr, arr[-1] + 10), -1)
        
    def test_non_empty_random(self, size=10):
        arr = [random.randrange(-100, 100) for _ in range(size)]
        self.arr = sorted(arr)
        key = random.randrange(self.arr[0], self.arr[-1] + 1)
        
        position = self.bs.search(self.arr, key)
        if key not in self.arr:
            self.assertEqual(position, -1, "Нету такого элемента в массиве")
        else:
            self.assertEqual(self.arr[position], key)
        
    def test(self, size_=10):
        self.test_empty_arr()
        for size in range(1, size_ + 1):
            self.test_non_empty_arr_true(size)
            self.test_non_empty_arr_false(size)
            self.test_non_empty_random(size)

if __name__ == "__main__":
  unittest.main()