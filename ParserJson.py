import json
from user import User

class ParserJSON:

    @staticmethod
    def read_from_file_json(filename):
        with open(filename, 'r') as file:
            data = json.load(file)

        list_of_users = []

        for user_element in data:
            firstname = user_element['firstname']
            telephone_number = user_element['telephone_number']
            email = user_element['email']
            password = user_element['password']
            role = user_element['role']
            created_at = user_element['created_at']

            children_data = user_element.get('children', [])
            children = [(child['name'], child['age']) for child in children_data]

            user = User(firstname, telephone_number, email, password, role, created_at, children)
            list_of_users.append(user)

        return list_of_users
