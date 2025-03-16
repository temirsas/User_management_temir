from datetime import datetime

class User:
    def __init__(self, user_id, name, surname, birthday):
        self.user_id = user_id
        self.name = name
        self.surname = surname
        self.birthday = birthday
        self.email = None
        self.password = None

    def get_details(self):
        return f"User  ID: {self.user_id}, Name: {self.name} {self.surname}, Email: {self.email}, Birthday: {self.birthday.strftime('%Y-%m-%d')}"

    def get_age(self):
        today = datetime.now()
        age = today.year - self.birthday.year - ((today.month, today.day) < (self.birthday.month, self.birthday.day))
        return age