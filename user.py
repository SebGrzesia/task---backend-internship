import re


class User:
    def __init__(self, firstname, telephone_number, email, password, role, created_at, children):
        self.firstname = firstname
        self.telephone_number = telephone_number
        self.email = email
        self.password = password
        self.role = role
        self.created_at = created_at
        self.children = children

    def __str__(self):
        return f"User(firstname={self.firstname}, telephone_number={self.telephone_number}, email={self.email}, password={self.password}, role={self.role}, created_at={self.created_at}, children={self.children})"
    
    def clean_telephone_number(self):
        if self.telephone_number:
            cleaned_number = re.sub(r'\D', '', self.telephone_number)
            cleaned_number = cleaned_number.lstrip('0')
            cleaned_number = cleaned_number[-9:]
            self.telephone_number = cleaned_number if cleaned_number else None