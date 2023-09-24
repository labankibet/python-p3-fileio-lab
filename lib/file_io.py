def write_file(file_name, file_content):
    with open(file_name + ".txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    with open(file_name + ".txt", "a") as file:
        file.write(append_content)

def read_file(file_name):
    with open(file_name + ".txt", "r") as file:
        return file.read()
    
write_file(file_name="logfile", file_content="Log 1: 5 bananas added")
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

file_contents = read_file(file_name="logfile")
print(file_contents)