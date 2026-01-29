
# Take user input
data = input("Enter some data to write into the file: ")

# Write data to file
with open("output.txt", "w") as file:
    file.write(data + "\n")

# Append additional data
with open("output.txt", "a") as file:
    file.write("This is appended data.\n")

# Read and display final content
print("\nFinal content of the file:")
with open("output.txt", "r") as file:
    for line in file:
        print(line.strip())
