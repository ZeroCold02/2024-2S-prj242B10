from src.user import UserManager

def main_menu():
    """메인 메뉴"""
    print("==== 도서 대출 관리 프로그램 ====")
    print("0. 종료")
    print("1. 로그인")
    print("2. 회원가입")
    print("==============================")

def main():
    user_manager = UserManager()
    while True:
        main_menu()
        choice = input("메뉴 선택: ")

        if choice == "0":
            print("프로그램을 종료합니다.")
            break

        elif choice == "1":
            print("로그인")
            #로그인

        elif choice == "2":
            while True:
                print("사용할 계정 정보를 입력해주세요")
                user_id = input("아이디: ")
                password = input("비밀번호: ")
                user_name = input("이름: ")
                answer = input("회원가입 하시겠습니까?(y): ")
                if answer == "y":
                    if user_manager.register_user(user_name, user_id, password):
                        break
                else:
                    print("초기화면으로 돌아갑니다.")
                    break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()
