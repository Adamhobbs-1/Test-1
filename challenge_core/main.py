import argparse
import platform

print(f"Python: {platform.python_version()}")
print(f"OS: {platform.system()} {platform.release()}")

def main():
    print("Challenge Core package loaded!")
    print("You can now import and use the package.")

def run():
    parser = argparse.ArgumentParser(description="Challenge Core CLI")
    parser.add_argument("--name", type=str, help="Your name")
    args = parser.parse_args()

    name = args.name or "bubadubs"
    print(f"Hello, {name}!")