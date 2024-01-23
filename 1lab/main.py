import unittest

def is_subarray(nums1, nums2):
    # Перевіряємо, чи nums1 є підмасивом nums2
    i, j = 0, 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            i += 1
        j += 1

    return i == len(nums1)

class TestIsSubarrayFunction(unittest.TestCase):
    def test_example1(self):
        nums1 = [1, 2, 3]
        nums2 = [1, 2, 3, 4]
        self.assertTrue(is_subarray(nums1, nums2))

    def test_example2(self):
        nums1 = [4, 2]
        nums2 = [1, 2, 3, 4]
        self.assertFalse(is_subarray(nums1, nums2))

    def test_example3(self):
        nums1 = [1, 3, 5]
        nums2 = [1, 2, 3, 4, 5]
        self.assertTrue(is_subarray(nums1, nums2))

if __name__ == '__main__':
    unittest.main()

