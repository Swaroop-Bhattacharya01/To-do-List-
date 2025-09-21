from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
import os
from app import models, schemas, crud, database, auth
from app.database import engine, SessionLocal

# Create tables
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="To-do List API", version="1.0.0")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = auth.decode_access_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )
    username = payload.get("sub")
    user = crud.get_user_by_username(db, username)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    return user

@app.get("/")
def read_root():
    return {"message": "Welcome to the To-do List API", "docs": "/docs"}

@app.post("/token", response_model=dict)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = crud.get_user_by_username(db, form_data.username)
    if not user or not auth.verify_password(form_data.password, user.hashed_password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    access_token = auth.create_access_token(
        data={"sub": user.username},
        expires_delta=timedelta(minutes=30)
    )
    return {"access_token": access_token, "token_type": "bearer"}

@app.post("/users/", response_model=schemas.UserInDB)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db, user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db, user)

@app.get("/todos/", response_model=list[schemas.TodoInDB])
def read_todos(current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.get_todos(db, current_user.id)

@app.post("/todos/", response_model=schemas.TodoInDB)
def create_todo(todo: schemas.TodoCreate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    return crud.create_todo(db, todo, current_user.id)

@app.put("/todos/{todo_id}", response_model=schemas.TodoInDB)
def update_todo(todo_id: int, todo_update: schemas.TodoUpdate, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db, todo_id, todo_update, current_user.id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

@app.delete("/todos/{todo_id}", response_model=schemas.TodoInDB)
def delete_todo(todo_id: int, current_user: models.User = Depends(get_current_user), db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db, todo_id, current_user.id)
    if not db_todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# This is required for Vercel
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
