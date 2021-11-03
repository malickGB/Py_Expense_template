import csv


# 222,food,Malick
# 345,drink,Robin,Malick
# 333,Gas,Pierre,Malick,Robin,SIGL





def get_status():
    users = {}
    with open("users.csv", "r", newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            users[row[0]] = 0

    with open("expense_report.csv", "r", newline='') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            involved = len(row[2:])
            print(involved)
            for i in row[2:]:
                if (i != row[2]):
                    users[i] += (int(row[0]) / involved)

    for key,val in users.items():
        print(key + ' owes', end=" ")
        print(users[key] )
    return