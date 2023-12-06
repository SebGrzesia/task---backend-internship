from datetime import datetime
import re

class PhoneNumberVerifier:

    @staticmethod
    def has_phone(user):
        return hasattr(user, 'telephone_number') and user.telephone_number is not None

    @staticmethod
    def verify_users_phone(users):
        users_by_phone = {}

        for user in users:
            if PhoneNumberVerifier.has_phone(user):
                phone_number = PhoneNumberVerifier.clean_phone_number(user.telephone_number)

                if phone_number in users_by_phone:
                    existing_user = users_by_phone[phone_number]

                    if user.created_at > existing_user.created_at:
                        users_by_phone[phone_number] = user
                else:
                    users_by_phone[phone_number] = user

        return list(users_by_phone.values())

    @staticmethod
    def clean_phone_number(telephone_number):
        cleaned_number = re.sub(r'\D', '', telephone_number)
        cleaned_number = cleaned_number.lstrip('0')
        cleaned_number = cleaned_number[-9:]
        return cleaned_number if cleaned_number else None
