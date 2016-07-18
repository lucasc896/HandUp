from datetime import datetime

import factory

from factory.alchemy import SQLAlchemyModelFactory
from handup.models import models, manage


SESSION = manage.get_test_session()


class UserFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.User
        sqlalchemy_session = SESSION

    id = factory.Sequence(int)
    name = factory.Sequence(str)
    unique_user_id = factory.Sequence(lambda s: "id_{}".format(s))
    date_added = factory.Sequence(lambda _: datetime.utcnow())
    date_of_birth = factory.Sequence(lambda _: datetime.utcnow())
    place_of_birth = factory.Sequence(lambda s: "EastBourne {}".format(s))


class UserHistoryFactory(SQLAlchemyModelFactory):
    class Meta:
        model = models.UserHistory
        sqlalchemy_session = SESSION

    id = factory.Sequence(int)
    user = factory.SubFactory(UserFactory)
    user_id = factory.Sequence(int)
    # TO-DO: offset the last_seen_date datetime object
    last_seen_date = factory.Sequence(lambda _: datetime.utcnow())
    last_seen_location = factory.Sequence(lambda s: "Old Street {}".format(s))
    last_institution_visited = factory.Sequence(int)
    # TO-DO: offset the last_seen_date datetime object
    last_institution_visit_date = factory.Sequence(lambda _: datetime.utcnow())
