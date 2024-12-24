import pytest
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
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('valid_genre', ['Фантастика', 'Ужасы', 'Мультфильмы', 'Комедии'])
    def test_set_book_genre_if_book_genre_in_genre_list(self,valid_genre):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', valid_genre)
        assert collector.books_genre['Оно'] in collector.genre


    @pytest.mark.parametrize('invalid_genre', ['Аниме', 'Киберпанк', 'Байопик'])
    def test_set_book_genre_if_book_genre_not_in_genre_list(self,invalid_genre):
        collector = BooksCollector()
        collector.add_new_book('Акира')
        collector.set_book_genre('Акира', invalid_genre)
        assert collector.books_genre['Акира'] == ''

    @pytest.mark.parametrize('valid_genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_book_genre_if_book_in_book_genre_list(self, valid_genre):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', valid_genre)
        assert collector.get_book_genre('Оно') == valid_genre

    @pytest.mark.parametrize('invalid_genre', ['Аниме', 'Киберпанк', 'Байопик'])
    def test_get_book_genre_if_book_genre_not_in_genre_list(self, invalid_genre):
        collector = BooksCollector()
        collector.add_new_book('Акира')
        collector.set_book_genre('Акира', invalid_genre)
        assert collector.get_book_genre('Акира') == ''

    @pytest.mark.parametrize('valid_genre', ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии'])
    def test_get_books_with_specific_genre_if_books_genre_in_genre_list(self,valid_genre):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Акира')
        collector.set_book_genre('Оно', valid_genre)
        collector.set_book_genre('Акира', valid_genre)
        assert collector.get_books_with_specific_genre(valid_genre) == ['Оно', 'Акира']

    def test_get_books_genre_if_book_genre_in_genre_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Акира')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Акира', 'Мультфильмы')
        assert collector.books_genre == {'Оно' : 'Ужасы', 'Акира' : 'Мультфильмы'}

    def test_get_books_genre_if_book_genre_not_in_genre_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Акира')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Акира', 'Аниме')
        assert collector.books_genre == {'Оно': 'Ужасы', 'Акира': ''}

    def test_get_books_for_children_if_book_not_in_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Вавилон 5')
        collector.add_new_book('Акира')
        collector.set_book_genre('Вавилон 5', 'Фантастика')
        collector.set_book_genre('Акира', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Вавилон 5','Акира']

    def test_get_books_for_children_if_book_in_genre_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Акира')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Акира', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Акира']

    def test_add_book_in_favorites_if_book_in_books_genre_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Акира')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Акира')
        assert collector.favorites == ['Оно','Акира']

    def test_add_book_in_favorites_if_book_is_already_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Акира')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Акира')
        collector.add_book_in_favorites('Оно')
        assert collector.favorites == ['Оно', 'Акира']

    def test_delete_book_from_favorites_book_in_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_book_in_favorites('Оно')
        collector.delete_book_from_favorites('Оно')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.add_new_book('Акира')
        collector.add_book_in_favorites('Оно')
        collector.add_book_in_favorites('Акира')
        assert collector.get_list_of_favorites_books() == ['Оно','Акира']

    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()