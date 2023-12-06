import xml.etree.ElementTree as ET
from user import User

class ParserXML:

    @staticmethod
    def read_from_file_xml(filename):
        tree = ET.parse(filename)
        root = tree.getroot()

        list_of_users = []

        for user_element in root.findall('user'):
            firstname = user_element.find('firstname').text
            telephone_number = user_element.find('telephone_number').text
            email = user_element.find('email').text
            password = user_element.find('password').text
            role = user_element.find('role').text
            created_at = user_element.find('created_at').text

            children_element = user_element.find('children')
            children = []
            for child_element in children_element.findall('child'):
                child_name = child_element.find('name').text
                child_age = child_element.find('age').text
                children.append((child_name, child_age))

            user = User(firstname, telephone_number, email, password, role, created_at, children)
            list_of_users.append(user)

        return list_of_users