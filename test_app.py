from app import add_numbers, greet

def test_add_numbers():
    """Test the add_numbers function"""
    assert add_numbers(2, 2) == 4
    assert add_numbers(10, 5) == 15
    assert add_numbers(-1, 1) == 0

def test_greet():
    """Test the greet function"""
    assert greet("Alice") == "Hello, Alice!"
    assert greet("Bob") == "Hello, Bob!"

def test_sample():
    """Basic sample test"""
    assert 1 + 1 == 2
