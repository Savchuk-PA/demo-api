from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base
from .mixins import UserRelationMixin


class Post(UserRelationMixin, Base):
    title: Mapped[str] = mapped_column(String(100))
    _user_back_populates = "posts"
    body: Mapped[str] = mapped_column(
        Text,
        default="",
        server_default="",
    )
