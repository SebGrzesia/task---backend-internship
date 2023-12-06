import re

class EmailVerifier:

    @staticmethod
    def is_valid_email(email):
        email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{1,4}$')
        return bool(email_pattern.match(email))
    
    @staticmethod
    def verify_users_email(users):
        for user in users:
            user.email = EmailVerifier.verify_email(user.email)

        verified_users = [user for user in users if EmailVerifier.is_valid_email(user.email)]

        return verified_users
    
    @staticmethod
    def verify_email(email):
        return email if EmailVerifier.is_valid_email(email) else ''