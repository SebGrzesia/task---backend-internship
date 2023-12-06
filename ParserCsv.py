import csv
from user import User

class ParserCSV:

    @staticmethod
    def read_from_file_csv(filename):
        list_of_users = []
        
        with open(filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile, delimiter=';')
            for row in reader:
                firstname = row['firstname']
                telephone_number = row['telephone_number']
                email = row['email']
                password = row['password']
                role = row['role']
                created_at = row['created_at']

                children_data = row.get('children','')
                children = [tuple(child.split(',')) for child in children_data.split(';') if child]

                user = User(firstname, telephone_number, email, password, role, created_at, children)
                list_of_users.append(user)
        
        return list_of_users