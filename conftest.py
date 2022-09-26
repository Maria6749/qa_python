import pytest
from tests2 import TestBooksCollector
@pytest.fixture
def book():
    book = TestBooksCollector(name='Преступление и наказание')

    return book

