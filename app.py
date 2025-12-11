def add_numbers(a, b):
    """Simple function to add two numbers"""
    return a + b

def greet(name):
    """Simple greeting function"""
    return f"Hello, {name}!"

if __name__ == "__main__":
    print("App running successfully!")
    print(greet("Student"))
    print(f"2 + 2 = {add_numbers(2, 2)}")