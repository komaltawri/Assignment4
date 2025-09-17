user_input = input("Enter some text: ")
file1 = open("output.txt", "w")
write_text = file1.write(user_input + "\n")
file1.close()
print("Data Written Succesfully!")

append_input = input("Enter some additional text: ")
file1 = open("output.txt", "a")
file1.write(append_input)
file1.close()

print("Data Appended Successfully!")

file1 = open("output.txt", "r")
read_file = file1.read()
print(read_file)
file1.close()