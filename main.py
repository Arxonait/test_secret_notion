from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from database import get_session
from models import NotionOrm
from schemas import NewNotedSchema

app = FastAPI()


@app.get("/")
def main():
    return {"detail": "main page"}


@app.post("/notion", status_code=201)
def post_notion(new_noted: NewNotedSchema, session: Session = Depends(get_session)):
    notion = NotionOrm(password=new_noted.password, message=new_noted.message)
    session.add(notion)
    session.commit()
    session.refresh(notion)
    return notion.get_schema(include=("message_id",))


@app.get("/notion", status_code=200)
def get_notion(password: str, message_id: str, session: Session = Depends(get_session)):
    stmt = select(NotionOrm).where(NotionOrm.message_id == message_id)
    try:
        notion: NotionOrm = session.scalars(stmt).one()
    except Exception as e:
        return {"detail": f"not found notion with id {message_id}"}

    if notion.password != password:
        return {"detail": "wrong password"}
    session.delete(notion)
    session.commit()
    return notion.get_schema()
