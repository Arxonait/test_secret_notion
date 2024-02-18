from sqlalchemy.orm import DeclarativeBase, mapped_column, sessionmaker
from sqlalchemy import select, create_engine


db_url = "postgresql+psycopg2://postgres:1234@localhost/secret_notion"

engine = create_engine(db_url, echo=True)

session_factory = sessionmaker(bind=engine, autocommit=False)


def get_session():
    session = session_factory()
    try:
        yield session
    finally:
        session.close()
