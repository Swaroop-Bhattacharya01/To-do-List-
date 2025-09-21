from sqlalchemy.orm import Session
from . import models, schemas
from .auth import get_password_hash, verify_password

# User CRUD
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# Todo CRUD
def get_todos(db: Session, owner_id: int):
    return db.query(models.Todo).filter(models.Todo.owner_id == owner_id).all()

def get_todo(db: Session, todo_id: int, owner_id: int):
    return db.query(models.Todo).filter(models.Todo.id == todo_id, models.Todo.owner_id==owner_id).first()

def create_todo(db: Session, todo: schemas.TodoCreate, owner_id: int):
    db_todo = models.Todo(**todo.model_dump(), owner_id=owner_id)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

def update_todo(db: Session, todo_id: int, todo_update: schemas.TodoUpdate, owner_id: int):
    db_todo = get_todo(db, todo_id, owner_id)
    if db_todo:
        for key, val in todo_update.model_dump(exclude_unset=True).items():
            setattr(db_todo, key, val)
        db.commit()
        db.refresh(db_todo)
    return db_todo

def delete_todo(db: Session, todo_id: int, owner_id: int):
    db_todo = get_todo(db, todo_id, owner_id)
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
