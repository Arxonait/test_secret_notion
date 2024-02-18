import uuid
from uuid import UUID

from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped


class Base(DeclarativeBase):
    @classmethod
    def get_type_obj(self):
        return "type"

    def to_dict(self, include: tuple[str] | None = None):
        main_dict = self.__dict__.copy()
        if include is not None:
            main_dict_in = dict()
            for key in include:
                if key in main_dict:
                    main_dict_in[key] = main_dict.get(key)
            main_dict = main_dict_in
        return main_dict

    def get_schema(self,  include: tuple[str] | None = None):
        return {
            "type_obj": self.get_type_obj(),
            "data": self.to_dict(include=include)
        }


class NotionOrm(Base):
    __tablename__ = "notions"

    id: Mapped[int] = mapped_column(primary_key=True)
    password: Mapped[str]
    message: Mapped[str]
    message_id: Mapped[UUID] = mapped_column(default=uuid.uuid4(), index=True)

    def get_type_obj(self):
        return "notions"
