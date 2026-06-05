
from app import add

def test_add():
    assert add(2, 3) == 5

result = add(2, 3)
print("output =", result)

print("Test Passed")