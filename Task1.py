try:
    file1 = open("sample.txt", "r")
    read_file = file1.read()
    print(read_file)
    file1.close()
except FileNotFoundError:
    print("File not found")
finally:
    print("Closing file")