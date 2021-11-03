from PyInquirer import prompt
import csv


def init_users(answers):
    users = []
    with open("users.csv", "r", newline='') as f:
        reader =  csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            users.append(row[0])
    return users

def init_involved(answers):
    users = []
    with open("users.csv", "r", newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            if (answers["spender"] != row[0]):
                users.append(row[0])
    dict = [{"name": val} for val in users]
    print(dict)
    return dict

expense_questions = [
    {
        "type":"input",
        "name":"amount",
        "message":"New Expense - Amount: ",
        'validate': lambda answer: 'You must input a number.' \
            if not answer.isnumeric() != 0 else True
    },
    {
        "type":"input",
        "name":"label",
        "message":"New Expense - Label: ",
    },
    {
        "type":"list",
        "name":"spender",
        "message":"New Expense - Spender: ",
        "choices": init_users
    },
    {
        "type":"checkbox",
        "name":"involved",
        "message":"New Expense - involved peoples: ",
        "choices": init_involved
    },


]



def new_expense(*args):
    infos = prompt(expense_questions)
    # Writing the informations on external file might be a good idea ¯\_(ツ)_/¯
    with open('expense_report.csv', 'a', newline='') as f:
        writer = csv.writer(f, delimiter=',',  quoting=csv.QUOTE_NONE, escapechar='')
        writer.writerow([infos["amount"],infos["label"], infos["spender"], ','.join(infos["involved"])])

    print("Expense Added !")
    return True


