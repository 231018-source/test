name = input("Enter name: ")
age = input("Enter age: ")
boot_camp_name = input("Enter boot camp name: ")
with open("file.txt", "w") as f:
    f.write(name + "\n")
    f.write(age + "\n")
    f.write(boot_camp_name + "\n")
    print("done saved notes")
    with open("file.txt","r") as f:
     reads = f.read()
     print(reads)
        



















