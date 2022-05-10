import ctypes
ctypes.cdll.LoadLibrary('../../Cpp/multiplyTwoNumbers/multiplyTwoNumbers.dll')

# Import the DLL
import multiplyTwoNumbers

def test_multiply():
    assert multiplyTwoNumbers.multiply(2, 2) == 4
