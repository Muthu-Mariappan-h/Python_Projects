sample_file = 'sample.txt'
try:
    with open(sample_file, 'r') as file1:
       content = file1.readlines()
       for i in range(len(content)):
           print(content[i])
except FileNotFoundError:
    print("The file", sample_file, "was not found")
