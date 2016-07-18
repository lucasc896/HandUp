import pytest

from handup.models import factories, models


def test_user(session):
    factories.UserFactory(name="Chris")

    session.commit()

    query = session.query(models.User)

    assert query.count() == 1

    for user in query.all():
        assert user.name in ["Chris", "Will"]