
import sys
from app import add

def test_add():
    assert add(2, 3) == 5

if __name__ == '__main__':
    test_add()
    print("✅ All tests passed!")
