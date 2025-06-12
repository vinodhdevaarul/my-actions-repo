import os

def main():
    name = os.environ.get("INPUT_NAME", "World")
    print(f"Hello {name}!")

if __name__ == "__main__":
    main()