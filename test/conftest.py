import pytest

from handup.models.manage import create_all, drop_all, get_test_session


@pytest.fixture(scope='function')
def session(request):
    session = get_test_session()

    drop_all()
    create_all()

    def teardown():
        session.rollback()
        session.close_all()
        drop_all()
        session.close()

    request.addfinalizer(teardown)
    return get_test_session()