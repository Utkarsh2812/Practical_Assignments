import csv

def write_into_csv(info_list):
    with open('Student_info.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(['Name', 'Age', 'Contact Number', 'E-Mail ID'])

        writer.writerow(info_list)

if __name__ == '__main__':
    condition = True
    student_num = 1

    while(condition):
        student_info = input("Enter student details for student #{} in the following format (Name Age Mobile Number E-Mail Id): ".format(student_num))

        # SPLIT
        student_info_list = student_info.split(' ')
        
        print("\nThe Entered information is- \nName: {}\nAge: {}\nMobile Number: {}\nE-Mail Id: {}"
        .format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3]))

        choice = input("Is the entered information correct? (y/n): ")

        if choice == "y":
            write_into_csv(student_info_list)
            condition_check = input("Do you want to enter more details of other students? (y/n)")
            if condition_check == "y":
                condition = True
                student_num = student_num + 1
            elif condition_check == "n":
                condition = False
        elif choice == 'n':
            print("\n Re-enter the details! ")