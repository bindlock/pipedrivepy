import unittest.mock

import pytest

from pipedrive import PipedriveError
from pipedrive.sio import Client


def test__request():
    client = Client(domain='test', token='test')

    with unittest.mock.patch('requests.request') as mock:
        client.deals(1).update(title='test')

        mock.assert_called_with(
            'PUT',
            'https://test.pipedrive.com/api/v1/deals/1',
            json={'title': 'test'},
            params={'api_token': 'test'},
            headers={'Content-Type': 'application/json'},
        )


def test__error():
    client = Client(domain='test', token='test')

    with pytest.raises(PipedriveError) as error:
        client.deals(1).update(title='test')

    assert error.value.code == 401
