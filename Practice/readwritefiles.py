# "w" mans write "a" means append "r+" for read and write
# employee_file = open("list.txt", "r") 

# print(employee_file.readable())
employee_file = open("list.txt", "a") 
employee_file.write("Rovin - Janitor")
#"w " overwiriting or create a new file 
employee_file.close()