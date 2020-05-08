# pylint:disable=useless-super-delegation,invalid-overridden-method

from unittest.mock import patch, MagicMock

import pytest

from pipedrive import PipedriveError
from pipedrive.aio import Client


class AsyncMock(MagicMock):
    def raise_for_status(self):
        pass

    async def __call__(self, *args, **kwargs):
        return super(AsyncMock, self).__call__(*args, **kwargs)


@pytest.mark.asyncio
async def test__request():
    client = Client(domain='test', token='test')

    with patch('aiohttp.ClientSession.request', new_callable=AsyncMock) as mock:
        await client.deals(1).update(title='test')

        mock.assert_called_with(
            method='PUT',
            url='https://test.pipedrive.com/api/v1/deals/1',
            json={'title': 'test'},
            params={'api_token': 'test'},
            headers={'Content-Type': 'application/json'},
        )


@pytest.mark.asyncio
async def test__error():
    client = Client(domain='test', token='test')

    with pytest.raises(PipedriveError) as error:
        await client.deals(1).update(title='test')

    assert error.value.code == 401
