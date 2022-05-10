import gc, weakref


class Test(unittest.TestCase):

    def test_case_1(self):
        le = LinkedList()
        le.addFront(1)
        le.addBack(2)
        le.addBack(3)
        le.addFront(0)

        le.removeNode(2)
        self.assertEqual(le.toArray(), [0, 1, 3])

    def test_case_2(self):
        le = LinkedList()
        le.addFront(3)
        le.addFront(2)
        le.addFront(0)

        le.removeNode(2)
        self.assertEqual(le.toArray(), [0, 3])

    def test_case_3(self):
        le = LinkedList()
        le.addBack(2)
        le.addFront(0)
        le.addBack(3)
        le.addBack(4)

        le.removeNode(0)
        self.assertEqual(le.toArray(), [2, 3, 4])

   
