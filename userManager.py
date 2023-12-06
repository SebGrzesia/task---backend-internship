from collections import Counter

class UserManager:
    def __init__(self, users):
        self.users = users

    def print_all_accounts(self):
        if self.is_admin_authenticated():
            valid_accounts = sum(1 for user in self.users if self.is_valid_account(user))
            print(valid_accounts)
        else:
            print("Invalid credentials or insufficient permissions.")

    def is_valid_account(self, user):
        return hasattr(user, 'telephone_number') and user.telephone_number is not None

    def is_admin_authenticated(self):
        return True
    
    def print_oldest_account(self):
        if self.is_admin_authenticated():
            oldest_account = self.get_oldest_account()
            if oldest_account:
                print(f"name: {oldest_account.firstname}")
                print(f"email_address: {oldest_account.email}")
                print(f"created_at: {oldest_account.created_at}")
            else:
                print("No account in our system.")
        else:
            print("Invalid credentials or insufficient permissions.")

    def get_oldest_account(self):
        return min((user for user in self.users if self.is_valid_account(user)),
            key=lambda user: user.created_at, default=None)

    def group_children_by_age(self):
        if self.is_admin_authenticated():
            children_by_age = Counter()

            for user in self.users:
                if self.is_valid_account(user):
                    for child in user.children:
                        if isinstance(child, str):
                            try:
                                age = int(child.split('(')[1].split(')')[0])
                                children_by_age[age] += 1
                            except (ValueError, IndexError):
                                pass

            for age, count in sorted(children_by_age.items()):
                print(f"wiek: {age} lat, liczba: {count}")
        else:
            print("Invalid credentials or insufficient permissions.")

    def print_children(self):
        if self.is_authenticated():
            authenticated_user = self.get_authenticated_user()
            children_info = [(child['name'], child['age']) for child in authenticated_user.children]
            sorted_children = sorted(children_info, key=lambda x: x[0])
            for child_name, child_age in sorted_children:
                print(f"{child_name}, {child_age}")
        else:
            print("Nieprawidłowe dane uwierzytelniające lub niewystarczające uprawnienia.")
