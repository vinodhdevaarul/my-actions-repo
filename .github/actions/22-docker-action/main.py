import sys

def greeting(name: str) -> str:
    """
    Function to return a greeting message.
    
    Args:
        name (str): The name to greet.
        
    Returns:
        str: A greeting message.
    """
    return f"Hello !!!!!!!!!!!! , {name}!"

if __name__ == "__main__":
    name = sys.argv[1]
    print(greeting(name))