# Read from a File Program
filename = input("Enter filename to read: ")

try:
    file = open(filename, "r")
    data = file.read()
    file.close()

    print("\n--- File Content ---")
    print(data)

except FileNotFoundError:
    print("File not found.")
