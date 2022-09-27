from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()


    # Проверка init books_rating


    def test_default_favorites_true(self):
        collector = BooksCollector()
        assert collector.get_books_rating() == {}

    # Проверка init favorites

    def test_default_favorites_true(self):
        collector = BooksCollector()
        assert collector.get_list_of_favorites_books() == []

    # Проверка добавления книг.

    def test_add_new_book_add_two_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Преступление и наказани')
        assert len(collector.get_books_rating()) == 2

    # Нельзя добавить одну и ту же книгу дважды.

    def test_add_book_two_times_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_new_book('Война и мир')
        assert len(collector.get_books_rating()) == 1

    # Нельзя выставить рейтинг книге, которой нет в списке

    def test_add_rating_for_book_not_in_list_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Преступление и наказание', 6)
        assert collector.get_book_rating('Преступление и наказани') == None

    # Позитивная проверка выставления рейтинга

    def test_set_book_rating_six_rating_increased(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 6)
        assert collector.get_book_rating('Война и мир') == 6

    # Нельзя выставить рейтинг меньше 1.

    def test_cant_set_books_rating_zero_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 0)
        assert collector.get_book_rating('Война и мир') != 0

    # Нельзя выставить рейтинг больше 10.

    def test_cant_set_books_rating_ten_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 11)
        assert collector.get_book_rating('Война и мир') != 11

    # У не добавленной книги нет рейтинга.

    def test_no_added_book_no_rating_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        assert collector.get_book_rating('Преступление и наказание') == None

    # добавляем книгу в Избранное

    def test_add_book_in_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == ['Война и мир']

    # удаляем книгу из Избранного

    def test_delete_book_from_favorites_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.delete_book_from_favorites('Война и мир')
        assert collector.get_list_of_favorites_books() == []

    # выводим список книг с определенным рейтингом

    def test_get_books_with_specific_rating_get_books_with_rating_6_true(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и наказание')
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 8)
        collector.set_book_rating('Преступление и наказание', 6)
        books_with_specific_rating = collector.get_books_with_specific_rating(8)
        assert books_with_specific_rating[0] == 'Война и мир'

    # получаем список Избранных книг

    def test_list_of_favorites_books_true(self):
        collector = BooksCollector()
        collector.add_new_book('Война и мир')
        collector.add_book_in_favorites('Война и мир')
        collector.favorites = collector.get_list_of_favorites_books()
        assert collector.get_list_of_favorites_books() == ['Война и мир']



