from PyInquirer import prompt
import csv

user_questions = [
    {
        "type":"input",
        "name":"name",
        "message":"New user - name: ",
    },
]

def add_user(*args):
    # This function should create a new user, asking for its name
    infos = prompt(user_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('users.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow([infos["name"]])

    print("User Added !")
    return True