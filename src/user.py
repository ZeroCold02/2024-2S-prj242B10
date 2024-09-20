class User:
    def __init__(self, name, user_id, password, loan_count=0, loan_date=None, is_admin=False):
        self.name = name
        self.user_id = user_id
        self.password = password
        self.loan_count = loan_count
        self.loan_date = loan_date
        self.is_admin = is_admin

    def __str__(self):
        return f"{self.name}, {self.user_id}, {self.password}, {self.loan_count}, {self.loan_date}, {self.is_admin}"

class UserManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.users = self.load_users()