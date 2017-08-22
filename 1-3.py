import unittest

def compare_str(str1,str2):
	if sorted(list(str1.lower())) == sorted(list(str2.lower())):
		return 1
	else:
		return 0

class TestCompareStr(unittest.TestCase):
	def test_compare_str(self):
		t_11 = "test"
		t_12 = "tets"
		t_21 = "Test"
		t_22 = "tets"
		t_31 = "Test"
		t_32 = "tet"

		self.assertEqual(compare_str(t_11,t_12),1)
		self.assertEqual(compare_str(t_21,t_22),1)
		self.assertEqual(compare_str(t_31,t_32),1)

	def test_compare_str1(self):
		t_11 = "test"
		t_12 = "tets"
		t_21 = "Test"
		t_22 = "tets"
		t_31 = "Test"
		t_32 = "tet"

		self.assertEqual(compare_str(t_11,t_12),1)
		self.assertEqual(compare_str(t_21,t_22),1)
		self.assertEqual(compare_str(t_31,t_32),1)

if __name__ == "__main__":
	unittest.main()
