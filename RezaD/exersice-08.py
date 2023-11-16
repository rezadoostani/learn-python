file_name = input("Enter file name with extenteion :")
with open(file_name, "r") as file:
    lines = file.readlines()
    counter = 0

    for i in lines:
        counter += 1

        if i == '\n' or i[0] == "#":
            counter -= 1

print(counter)