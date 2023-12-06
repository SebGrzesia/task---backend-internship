from ParserCsv import ParserCSV
from ParserXML import ParserXML
from ParserJson import ParserJSON
from emailVerify import EmailVerifier
from phoneNumberVerify import PhoneNumberVerifier
from userManager import UserManager
import argparse

xml_file_1 = 'data/users_2.xml'
xml_file_2 = 'data/a/b/users_1.xml'
json_file_1 = 'data/a/users.json'
csv_file_1 = 'data/a/b/users_1.csv'
csv_file_2 = 'data/a/c/users_2.csv'

users_1 = ParserXML.read_from_file_xml(xml_file_1)
users_2 = ParserXML.read_from_file_xml(xml_file_2)
users_3 = ParserJSON.read_from_file_json(json_file_1)
users_4 = ParserCSV.read_from_file_csv(csv_file_1)
users_5 = ParserCSV.read_from_file_csv(csv_file_2)

all_users = users_1 + users_2 + users_3 + users_4 + users_5

for user in all_users:
    user.clean_telephone_number()

email_verifier = EmailVerifier()
verified_users = email_verifier.verify_users_email(all_users)

users_with_phone = PhoneNumberVerifier.verify_users_phone(verified_users)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="User Management Script")
    parser.add_argument("--login", required=True, help="User login (email or telephone number)")
    parser.add_argument("--password", required=True, help="User password")
    parser.add_argument("command", choices=["print-all-accounts", "print-oldest-account", "group-by-age","print_children"], help="Command to execute")

    args = parser.parse_args()

    user_manager = UserManager(users_with_phone)

    if args.command == "print-all-accounts":
        user_manager.print_all_accounts()
    elif args.command == "print-oldest-account":
        user_manager.print_oldest_account()
    elif args.command == "group-by-age":
        user_manager.group_children_by_age()
    elif args.command == "print_children":
        user_manager.group_children_by_age()
    else:
        print("Invalid command")