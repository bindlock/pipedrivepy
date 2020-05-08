import unittest.mock

from pipedrive.chain import Chain


def test__get():
    client = unittest.mock.MagicMock()

    Chain(client).users(1).get()
    Chain(client).activities.get(user_id=1)

    client.request.assert_any_call('users/1', 'GET', query={})
    client.request.assert_any_call('activities', 'GET', query={'user_id': 1})


def test__add():
    client = unittest.mock.MagicMock()

    Chain(client).deals.add(title='test')
    Chain(client).deals(1).duplicate().add()

    client.request.assert_any_call('deals', 'POST', payload={'title': 'test'})
    client.request.assert_any_call('deals/1/duplicate', 'POST', payload={})


def test__update():
    client = unittest.mock.MagicMock()

    Chain(client).deals(1).update(title='test')
    Chain(client).deals(1).merge.update(merge_with_id=2)

    client.request.assert_any_call('deals/1', 'PUT', payload={'title': 'test'})
    client.request.assert_any_call('deals/1/merge', 'PUT', payload={'merge_with_id': 2})


def test__delete():
    client = unittest.mock.MagicMock()

    Chain(client).files(1).delete()
    Chain(client).activities.delete(ids='1,2')

    client.request.assert_any_call('files/1', 'DELETE', payload={})
    client.request.assert_any_call('activities', 'DELETE', payload={'ids': '1,2'})
