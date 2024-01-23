import unittest

def find_triplet(arr, target_sum):
    # Сортуємо масив для полегшення пошуку
    arr.sort()

    n = len(arr)

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]
            if current_sum == target_sum:
                return True
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return False

class TestFindTripletFunction(unittest.TestCase):
    def test_example1(self):
        arr = [1, 2, 3]
        target_sum = 6
        self.assertTrue(find_triplet(arr, target_sum))

    def test_example2(self):
        arr = [1, 2, 3, 4]
        target_sum = 8
        self.assertFalse(find_triplet(arr, target_sum))

    def test_example3(self):
        arr = [3, 2, 1, 4]
        target_sum = 6
        self.assertTrue(find_triplet(arr, target_sum))

if __name__ == '__main__':
    unittest.main()

