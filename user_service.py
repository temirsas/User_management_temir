from user import User

class UserService:
    users = {}

    @classmethod
    def add_user(cls, user):
        cls.users[user.user_id] = user

    @classmethod
    def find_user(cls, user_id):
        return cls.users.get(user_id)

    @classmethod
    def delete_user(cls, user_id):
        if user_id in cls.users:
            del cls.users[user_id]

    @classmethod
    def update_user(cls, user_id, user_update):
        if user_id in cls.users:
            user = cls.users[user_id]
            user.name = user_update.name
            user.surname = user_update.surname
            user.birthday = user_update.birthday
            user.email = user_update.email
            user.password = user_update.password

    @classmethod
    def get_number(cls):
        return len(cls.users)