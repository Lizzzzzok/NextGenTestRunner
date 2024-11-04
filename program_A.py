import sys
import random

def main():
    while True:
        command = sys.stdin.readline().strip()
        
        if command == "Hi":
            print("Hi")
            sys.stdout.flush()
        
        elif command == "GetRandom":
            print(random.randint(0, 100))
            sys.stdout.flush()
        
        elif command == "Shutdown":
            break
        
        # Ignoring any unknown commands
        else:
            continue

if __name__ == "__main__":
    main()
