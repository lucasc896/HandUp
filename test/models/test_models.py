import pytest

from handup.models import factories


def test_user(session):
    u1 = factories.UserFactory(name="Chris")
    import pdb; pdb.set_trace()