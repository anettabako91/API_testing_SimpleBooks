from api_requests import request_books


class TestBooks:

    def test_get_all_books(self):
        response = request_books.get_all_books()
        assert response.status_code == 200, f'actual:{response.status_code} , expected: 200'
        assert len(response.json()) == 6  # stim ca trebuie sa contina 6 carti - asta doar in cazul in care stim cate
        # elemente trebuie sa fie
        for book in response.json():
            assert "id" in book.keys()  # verificam ca id sa fie in lista de key
            assert "name" in book.keys()
            assert "type" in book.keys()
            assert "available" in book.keys()

    def test_get_all_fiction_books(self):
        response = request_books.get_all_books('fiction')  # punem paramentru pt ca vrem doar cartile de fiction
        assert response.status_code == 200, f'actual:{response.status_code} , expected: 200'
        for book in response.json():
            assert book['type'] == "fiction", f'actual: {book["type"]}, expected: fiction'

    # ATENTIE - LA FIECARE VERIFICARE/INPUT NOU FACEM UN TEST NOU!! NU FACEM MODIFICARI INTR-UN TEST

    def test_get_all_non_fiction_books(self):
        response = request_books.get_all_books('non-fiction')  # punem paramentru pt ca vrem doar cartile de fiction
        assert response.status_code == 200, f'actual:{response.status_code} , expected: 200'
        for book in response.json():
            assert book['type'] == "non-fiction", f'actual: {book["type"]}, expected: non-fiction'

    def test_limit_books_query(self):
        response = request_books.get_all_books(limit=3)  # specificam parametrul la care dam valoare
        assert response.status_code == 200, f'actual:{response.status_code} , expected: 200'
        assert len(response.json()) <= 3, f'actual:number of objects: {response.json()} , expected: number of ' \
                                          f'objects <=3 '
        # poate fi 1/2/3, important <=

    def test_get_book(self):
        response = request_books.get_book(1)
        assert response.status_code == 200, f'actual:{response.status_code} , expected: 200'
        assert response.json()['id'] == 1  # verificam ca id-ul primului book intradevar e 1

# putem verifica si cu valori care nu exista, valori prea mari/mici -> limit -1 , type action, id 30


# TestBooks().test_get_all_fiction_books()
# TestBooks().test_get_all_non_fiction_books()
# TestBooks().test_limit_books_query() # daca la astea dam run si da exit code 0 inseamna ca e totul ok!!!
