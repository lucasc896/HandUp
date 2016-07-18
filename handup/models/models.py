import datetime
import sqlalchemy as sa

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    __sequence_name__ = 'user_id_sequence'

    sequence = sa.Sequence(name=__sequence_name__)

    id = sa.Column(sa.Integer,
                   sequence,
                   primary_key=True)

    name = sa.Column(
        sa.String(128),
        nullable=False,
        doc="Name of the user")

    uuid = sa.Column(
        sa.String(128),
        nullable=False,
        doc="Unique user identifier in network")

    date_added = sa.Column(
        sa.DateTime(),
        nullable=False,
        doc="Date user was entered into the system",
        index=True) # why?

    date_of_birth = sa.Column(
        sa.DateTime(),
        nullable=True,
        doc="Date of birth of the user")

    place_of_birth = sa.Column(
        sa.String(128),
        nullable=True,
        doc="Place of birth of user")


class UserHistory(Base):
    __tablename__ = 'user_history'
    __sequence_name__ = 'user_history_id_sequence'

    sequence = sa.Sequence(name=__sequence_name__)
    id = sa.Column(sa.Integer,
                   sequence,
                   primary_key=True)

    user_id = sa.Column(
        sa.Integer,
        sa.ForeignKey(User.id),
        index=True)

    user = sa.orm.relation('User')

    last_seen_date = sa.Column(
        sa.DateTime(),
        nullable=True,
        doc="Date user was last seen (can be logged by a donater)")

    last_seen_location = sa.Column(
        sa.String(256),
        nullable=True,
        doc="Location user was last seen (can be logged by a donater)")

    # last_institution_visited = sa.Column(
    #     sa.Integer,
    #     nullable=True,
    #     sa.ForeignKey(Instituion.id),
    #     doc="ID of last known Instituion visited")

    last_institution_visit_date = sa.Column(
        sa.DateTime,
        nullable=True,
        index=True,
        doc="Date of last known visit to a network instritition")

