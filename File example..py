file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

file = open("example.txt", "w")
file.write("Hello, World!")
file.close()

file = open("example.txt", "r")
# Perform operations
file.close()

with open("example.txt", "r") as file:
    content = file.read()
    print(content)
