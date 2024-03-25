from api_requests import request_orders


class TestOrder:

    def test_submit_order(self):
        response = request_orders.submit_order(1, "Jhon")
        assert response.json()['created'] == True
        assert 'orderId' in response.json().keys()
        request_orders.delete_order(
            response.json()['orderId'])  # curat lista de comezni ca mai jos sa nu impacteze rezultatele

    def test_submit_incorrect_order(self):
        response = request_orders.submit_order(30, 'Jhon')
        assert response.json()['error'] == 'Invalid or missing bookId.', f"actual: {response.json()} , expected: " \
                                                                         f"'error : Invalid or missing bookId. "

        # aici verificam o valoare care trebuie sa dea error

    # TestOrder().test_submit_order()
    # TestOrder().test_submit_incorrect_order()


    def test_get_all_orders(self):
        order_1 = request_orders.submit_order(1, "Doe")
        order_2 = request_orders.submit_order(3, "Vlad")
        response = request_orders.get_all_orders()
        assert len(response.json()) == 2
        assert order_1.json()['orderId'] in response.json()[0].values() or order_1.json()['orderId'] in response.json()[1].values()
        assert order_2.json()['orderId'] in response.json()[0].values() or order_2.json()['orderId'] in response.json()[1].values()
        # cleanup
        request_orders.delete_order(order_1.json()['orderId'])
        request_orders.delete_order(order_2.json()['orderId'])

    def test_get_order(self):
        book_id = 5
        customer_name = 'Vali'
        order_id = request_orders.submit_order(book_id, customer_name).json()['orderId']
        response = request_orders.get_order(order_id)
        assert response.json()['id'] == order_id
        assert response.json()['bookId'] == book_id
        assert response.json()['customerName'] == customer_name
        request_orders.delete_order(order_id)

    def test_update_order(self):
        customer_name = 'Elena'
        order_id = request_orders.submit_order(5, customer_name).json()['orderId']  # am creat o comanda cu name elena
        new_customer_name = 'Ana'
        response = request_orders.update_order(order_id, new_customer_name)  # update cu noul nume
        assert response.status_code == 204  # am verificat ca status code pt update sa fie 204
        new_order_response = request_orders.get_order(order_id)  # am verificat daca s-a updatat numele
        assert new_order_response.json()['customerName'] == new_customer_name  # verificam daca se potrivesc numele
        request_orders.delete_order(order_id)

    def test_delete_order(self):
        order_id = request_orders.submit_order(5, 'John').json()['orderId']
        response = request_orders.delete_order(order_id)
        assert response.status_code == 204
        get_order_response = request_orders.get_order(order_id)
        assert get_order_response.status_code == 404
        assert get_order_response.json()['error'] == f'No order with id {order_id}.'


