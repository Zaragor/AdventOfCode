import unittest
from unittest.mock import patch
import intcode_computer

class incode_computer_tests(unittest.TestCase):
    def test_opcode_1(self):
        stack = list([1, 3, 3, 3])
        intcode_computer.calculate(stack)
        self.assertEqual(stack[3], 6, 'Adding failed')
    
    def test_opcode_1_correct_position(self):
        stack = list([1, 5, 6, 7, 99, 4, 3, 0])
        intcode_computer.calculate(stack)
        self.assertEqual(stack[7], 7, 'Correct place')
    
    def test_opcode_2(self):
        stack = list([2, 5, 6, 4, 0, 33, 3])
        intcode_computer.calculate(stack)
        self.assertEqual(stack[4], 99, 'Multiplying')
    
    def test_opcode_3(self):
        stack = list([3, 0, 99])
        intcode_computer.input = lambda _: 1
        intcode_computer.calculate(stack)
        self.assertEqual(1, stack[0])
    
    @patch('intcode_computer.print', create= True)
    def test_opcode_4(self, print_):
        stack = list([4, 2, 99])
        intcode_computer.calculate(stack)
        print_.assert_called_with(99)

    @patch('intcode_computer.print', create= True)
    def test_opcode_8_equals(self, print_):
        stack = [3,9,8,9,10,9,4,9,99,-1,8]
        intcode_computer.input = lambda _: 8
        intcode_computer.calculate(stack)
        print_.assert_called_with(1)

    @patch('intcode_computer.print', create= True)
    def test_opcode_8_not_equals(self, print_):
        stack = [3,9,8,9,10,9,4,9,99,-1,8]
        intcode_computer.input = lambda _: 7
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_7_less_than(self, print_):
        stack = [3,9,7,9,10,9,4,9,99,-1,8]
        intcode_computer.input = lambda _ : 7
        intcode_computer.calculate(stack)
        print_.assert_called_with(1)
    
    @patch('intcode_computer.print', create= True)
    def test_opcode_7_equal(self, print_):
        stack = [3,9,7,9,10,9,4,9,99,-1,8]
        intcode_computer.input = lambda _ : 8
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_7_greater_than(self, print_):
        stack = [3,9,7,9,10,9,4,9,99,-1,8]
        intcode_computer.input = lambda _ : 9
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_8_immediate_not_equal(self, print_):
        stack = [3,3,1108,-1,8,3,4,3,99]
        intcode_computer.input = lambda _ : 7
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_8_immediate_equal(self, print_):
        stack = [3,3,1108,-1,8,3,4,3,99]
        intcode_computer.input = lambda _ : 8
        intcode_computer.calculate(stack)
        print_.assert_called_with(1)

    @patch('intcode_computer.print', create= True)
    def test_opcode_7_immediate_less(self, print_):
        stack = [3,3,1107,-1,8,3,4,3,99]
        intcode_computer.input = lambda _ : 7
        intcode_computer.calculate(stack)
        print_.assert_called_with(1)

    @patch('intcode_computer.print', create= True)
    def test_opcode_7_immediate_equal(self, print_):
        stack = [3,3,1107,-1,8,3,4,3,99]
        intcode_computer.input = lambda _ : 8
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_7_immediate_greater(self, print_):
        stack = [3,3,1107,-1,8,3,4,3,99]
        intcode_computer.input = lambda _ : 9
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_jumps_equals(self, print_):
        stack = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        intcode_computer.input = lambda _ : 0
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_jumps_not_equal(self, print_):
        stack = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        intcode_computer.input = lambda _ : 6
        intcode_computer.calculate(stack)
        print_.assert_called_with(1)

    @patch('intcode_computer.print', create= True)
    def test_opcode_jumps_immediate_equal(self, print_):
        stack = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        intcode_computer.input = lambda _ : 0
        intcode_computer.calculate(stack)
        print_.assert_called_with(0)

    @patch('intcode_computer.print', create= True)
    def test_opcode_jumps_immediate_not_equal(self, print_):
        stack = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        intcode_computer.input = lambda _ : 6
        intcode_computer.calculate(stack)
        print_.assert_called_with(1)

if __name__ == "__main__":
    unittest.main()