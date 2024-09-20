from src.book import BookManager


def admin_menu():
    """관리자 메뉴"""
    print("==== 관리자 도서 관리 시스템 ====")
    print("1. 책 등록")
    print("2. 책 삭제")
    print("3. 책 검색 (제목)")
    print("4. 종료")
    print("=========================")


def main():
    book_manager = BookManager()
    while True:
        admin_menu()
        choice = input("메뉴 선택: ")

        if choice == "1":
            title = input("책 제목: ")
            book_manager.register_book(title)

        elif choice == "2":
            book_id = input("삭제할 책 ID: ")
            book_manager.delete_book(book_id)

        elif choice == "3":
            print("\n현재 등록된 모든 책 목록:")
            book_manager.display_books()
            title = input("\n검색할 책 제목을 입력하세요: ")
            book_manager.search_book(title)

        elif choice == "4":
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()
