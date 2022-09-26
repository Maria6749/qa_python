from main import BooksCollector
class Book:
    def test_list_of_favorites_books_true(self, book):
        collector11 = BooksCollector()
        collector11.add_new_book = book.name
        collector11.add_book_in_favorites = book.name
        collector11.favorites = collector11.get_list_of_favorites_books()
        assert collector11.get_list_of_favorites_books() == ['Преступление и наказание']