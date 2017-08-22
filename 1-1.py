import unittest

# input : check_string
# result : uniq : 1, not uniq : 0 
def check_uniq(str):
	if len(str) > 256:
		return 0 
	check_list = [0 for i in range(256)]
	for c in str:
		index = ord(c)
		if check_list[index] == 1:
			return 0
		else:
			check_list[index] = 1
	return 1
	
class TestCheckUniq(unittest.TestCase):
	def test_check_uniq(self):
		str1 = "test"
		str2 = "tes"
		str3 = "jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj"
		self.assertEqual(check_uniq(str1),0)
		self.assertEqual(check_uniq(str2),1)
		self.assertEqual(check_uniq(str3),0)

if __name__ == "__main__":
	unittest.main()
