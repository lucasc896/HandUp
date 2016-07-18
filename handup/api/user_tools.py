import logging

from datetime import datetime

import sqlalchemy as sa

from handup.models.models import User

LOGGER = logging.getLogger()


def parse_datestring(date_string):
    if date_string is None:
        return None
    return datetime.strptime(date_string, "%d/%m/%Y")


def get_all_users(session):
    users_query = session.query(User)
    return users_query.all()


def get_user(session, uuid=""):
    user_query = session.query(User).filter(
        User.uuid == uuid)
        
    assert user_query.count() == 1

    return user_query.all()[0]


def is_networks_only_uuid(session, uuid):
    return True


def add_new_user(session, user_data):
    assert user_data.get('name')
    assert user_data.get('uuid')
    assert is_networks_only_uuid(
        session, user_data.get('uuid')
    )

    # could unpack user_data here - bad to require a given structure of user_data?
    # add others with default vals, or will they NULL?
    user_obj = User(
        name = user_data.get('name'),
        uuid = user_data.get('uuid'),
        date_added = user_data.get('date_added', datetime.utcnow()),
        date_of_birth = parse_datestring(user_data.get('date_of_birth')),
        place_of_birth = user_data.get('place_of_birth'),
    )

    try:
        session.add(user_obj)
        session.commit()
    except Exception as exc:
        LOGGER.exception("Error adding user. {}".format(exc))
        
        return False

    return True
