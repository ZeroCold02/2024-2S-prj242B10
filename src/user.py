import csv
import os
import re


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
    def __init__(self, file_path='data/userlist.txt'):
        self.file_path = file_path
        self.users = self.load_users()

    def load_users(self):
        users = []
        if os.path.exists(self.file_path):
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    name, user_id, password, loan_count, loan_date, is_admin = row
                    users.append(User(name, user_id, password, loan_count, loan_date, is_admin))
        else:
            print(f"{self.file_path} 파일이 존재하지 않아 새로 생성합니다.")
            os.makedirs(os.path.dirname(self.file_path), exist_ok=True)
            with open(self.file_path, 'w', encoding='utf-8') as file:
                pass
        return users

    def save_users(self):
        with open(self.file_path, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            for user in self.users:
                writer.writerow([user.name, user.user_id, user.password, user.loan_count, user.loan_date, user.is_admin])

    def validate_user(self, user_name, user_id, password): #나중에 parser 클래스?로 옮기면? 될듯
        name_pattern = r"^[A-Za-z]{1,20}$"
        id_pattern = r"^[A-Za-z0-9]{3,7}$"
        pw_pattern = r"^[A-Za-z0-9]{5,10}$"
        if not re.match(id_pattern, user_id):
            print(f"1 아이디,비밀번호 또는 이름이 입력 형식에 맞지 않습니다. 다시 입력해 주세요. ")
            return False
        for user in self.users:
            if user_id == user.user_id:
                print(f"2 아이디,비밀번호 또는 이름이 입력 형식에 맞지 않습니다. 다시 입력해 주세요. ")
                return False
        if not re.match(pw_pattern, password):
            print(f"3 아이디,비밀번호 또는 이름이 입력 형식에 맞지 않습니다. 다시 입력해 주세요. ")
            return False
        if not re.match(name_pattern, user_name):
            print(f"4 아이디,비밀번호 또는 이름이 입력 형식에 맞지 않습니다. 다시 입력해 주세요. ")
            return False

        return True

    def register_user(self, user_name, user_id, password):
        if self.validate_user(user_name, user_id, password):
            new_user = User(user_name, user_id, password)
            self.users.append(new_user)
            self.save_users()
            print(f"'{user_name}'님 회원가입에 성공하셨습니다. 메인 화면으로 돌아갑니다.")
            return True
        else:
            return False
