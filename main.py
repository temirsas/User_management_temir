from datetime import datetime
from user import User
from user_service import UserService
from user_util import UserUtil

# Example usage
if __name__ == "__main__":
    # Create a user
    user_id = UserUtil.generate_user_id()
    name = "Temir"
    surname = "Saidulaev"
    birthday = datetime(2004, 9, 4)

    user = User(user_id, name, surname, birthday)
    user.email = UserUtil.generate_email(name, surname, "gmail.com")
    user.password = UserUtil.generate_password()

    # Add user to UserService
    UserService.add_user(user)

    # Retrieve user details
    retrieved_user = UserService.find_user(user_id)
    print(retrieved_user.get_details())
    print(f"Age: {retrieved_user.get_age()}")

    # Get number of users
    print(f"Number of users: {UserService.get_number()}")

    # Update user
    updated_user = User(user_id, "Temir", "Saidulaev", datetime(2004, 9, 4))
    updated_user.email = UserUtil.generate_email("Temir", "Saidulaev", "gmail.com")
    updated_user.password = UserUtil.generate
