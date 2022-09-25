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
    from main import BooksCollector

    class TestBooksCollector:

        # Проверка init books_rating

        def test_default_book_rating_true(self):
            collector0 = BooksCollector()
            assert collector0.books_rating == {}

        # Проверка init favorites

        def test_default_favorites_true(self):
            collector1 = BooksCollector()
            assert collector1.favorites == []


        # Нельзя добавить одну и ту же книгу дважды.

        def test_add_book_two_times_true(self):
            collector2 = BooksCollector()
            collector2.add_new_book('Преступление и наказание')
            collector2.add_new_book('Преступление и наказание')
            assert len(collector2.get_books_rating()) == 1

        # Нельзя выставить рейтинг книге, которой нет в списке

        def test_add_rating_for_book_not_in_list_true(self):
            collector3 = BooksCollector()
            collector3.add_new_book('Преступление и наказание')
            collector3.set_book_rating('Война и мир', 6)
            assert collector3.books_rating.get('Война и мир') == None

        # Позитивная проверка выставления рейтинга

        def test_set_book_rating_six_rating_increased(self):
            collector4 = BooksCollector()
            collector4.add_new_book('Война и мир')
            collector4.set_book_rating('Война и мир', 6)
            assert collector4.books_rating['Война и мир'] == 6

        # Нельзя выставить рейтинг меньше 1.

        def test_cant_set_books_rating_zero_true(self):
            collector5 = BooksCollector()
            collector5.add_new_book('Война и мир')
            collector5.set_book_rating('Война и мир', 0)
            assert collector5.books_rating['Война и мир'] != 0

        # Нельзя выставить рейтинг больше 10.

        def test_cant_set_books_rating_ten_true(self):
            collector6 = BooksCollector()
            collector6.add_new_book('Война и мир')
            collector6.set_book_rating('Война и мир', 11)
            assert collector6.books_rating['Война и мир'] != 11

        # У не добавленной книги нет рейтинга.

        def test_no_added_book_no_rating_true(self):
            collector7 = BooksCollector()
            collector7.add_new_book('Война и мир')
            assert collector7.books_rating.get('Преступление и наказание') == None

        # добавляем книгу в Избранное

        def test_add_book_in_favorites_true(self):
            collector8 = BooksCollector()
            collector8.add_new_book('Преступление и наказание')
            collector8.add_book_in_favorites('Преступление и наказание')
            assert collector8.favorites == ['Преступление и наказание']

        # удаляем книгу из Избранного

        def test_delete_book_from_favorites_true(self):
            collector9 = BooksCollector()
            collector9.add_new_book('Преступление и наказание')
            collector9.add_book_in_favorites('Преступление и наказание')
            collector9.delete_book_from_favorites('Преступление и наказание')
            assert collector9.favorites == []

        # выводим список книг с определенным рейтингом

        def test_get_books_with_specific_rating_get_books_with_rating_6_true(self):
            collector10 = BooksCollector()
            collector10.add_new_book('Преступление и наказание')
            collector10.add_new_book('Война и мир')
            collector10.add_new_book('Гордость и предубеждение')
            collector10.set_book_rating('Война и мир', 8)
            collector10.set_book_rating('Преступление и наказание', 6)
            collector10.set_book_rating('Гордость и предубеждение', 2)
            books_with_specific_rating = collector10.get_books_with_specific_rating(6)
            assert books_with_specific_rating[0] == 'Преступление и наказание'

        # получаем список Избранных книг

        def test_list_of_favorites_books_true(self):
            collector11 = BooksCollector()
            collector11.add_new_book('Преступление и наказание')
            collector11.add_book_in_favorites('Преступление и наказание')
            collector11.favorites = collector11.get_list_of_favorites_books()
            assert collector11.favorites == ['Преступление и наказание']

