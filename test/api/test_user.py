from datetime import datetime

import freezegun
import pytest
import sqlalchemy as sa

from handup.api import user_tools
from handup.models import factories, models

TEST_USER_NAMES = ['Chris', 'Will', 'Dan']


@pytest.fixture(scope='function')
def fill_test_users(session):
    for name in TEST_USER_NAMES:
        factories.UserFactory(name=name)
    session.commit()


def test_get_all_users(session, fill_test_users):
    users = user_tools.get_all_users(session)
    
    assert len(users) == len(TEST_USER_NAMES)
    for user in users:
        assert user.name in TEST_USER_NAMES


def test_get_user(session):

    factories.UserFactory(name='Chris', uuid='uuid_0')
    factories.UserFactory(name='Will', uuid='uuid_1')

    assert user_tools.get_user(session, uuid='uuid_0').name == 'Chris'
    assert user_tools.get_user(session, uuid='uuid_1').name == 'Will'


@freezegun.freeze_time('2016-01-16 12:00:00')
def test_add_new_user(session):

    user_1_data = {
        'name': 'Dan',
        'uuid': 'uuid_0',
    }

    user_tools.add_new_user(session, user_1_data)

    user_query = session.query(models.User).filter(
        models.User.uuid == user_1_data.get('uuid'))

    assert user_query.count() == 1
    assert user_query.first().name == 'Dan'
    assert user_query.first().date_added == datetime.strptime("160120161200",
                                                                       "%d%m%Y%H%M")

    user_2_data = {
        'name': 'Will',   
    }

    with pytest.raises(AssertionError):
        user_tools.add_new_user(session, user_2_data)

    assert session.query(models.User).count() == 1

    user_3_data = {
        'name': 'Chris',
        'uuid': 'uuid_1',
        'date_of_birth': '16/01/1989',
        'place_of_birth': 'London'
    }
    user_tools.add_new_user(session, user_3_data)

    user_query = session.query(models.User).filter(
        models.User.uuid == user_3_data.get('uuid'))

    assert user_query.count() == 1
    user_3 = user_query.first()
    assert user_3.name == user_3_data.get('name')
    assert user_3.uuid == user_3_data.get('uuid')
    assert user_3.date_of_birth == user_tools.parse_datestring(
        user_3_data.get('date_of_birth'))
    assert user_3.place_of_birth == user_3_data.get('place_of_birth')