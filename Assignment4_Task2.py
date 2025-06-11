out_file = 'output.txt'
user_input = input("Enter text to write to the file:")
with open(out_file, 'w') as file1:
    file1.write(user_input)
    print("Data successfully written to " + out_file + ".\n")

add_text = input("Enter additional text to append:")
with open(out_file, 'a') as file1:
    file1.write("\n" + add_text)
    print("Data successfully appended.\n")

with open(out_file, 'r') as file1:
    file_content = file1.read()
    print("Final content of " + out_file + ":")
    print(file_content)
