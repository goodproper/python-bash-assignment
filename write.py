# Write to a File Program
filename = input("Enter filename (example: myfile.txt): ")
content = input("Enter the content you want to write: ")

file = open(filename, "w")
file.write(content)
file.close()

print("Content written to", filename)
