import vec
import unittest

class vecTest(unittest.TestCase):
	
	def setUp(self):
		self.list1=[2,7,3]
		self.list2=[2,3,7]
	
	def test_tri(self):
		list1=[2,7,3]
		list2=[2,3,7]
		list=vec.triBulle(list1)
		self.assertEqual(list,list2)
	
	def test_somme(self):
		list1=[2,7,3]
		list2=[2,3,7]
		list3=[4,10,10]
		list=vec.sommeElem(list1,list2)
		self.assertEqual(list,list3)

	def test_invers(self):
		list1=[2,7,3]
		list2=[3,7,2]
		list=vec.inversElem(list1)
		self.assertEqual(list,list2)
		
		
		
if __name__ == '__main__':
    unittest.main()