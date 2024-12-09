from sqlalchemy.orm import Session
from db.hash import Hash
from db.models import DbUser
from schemas import UserBase

# create element
def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        username = request.username,
        email = request.email,
        password = Hash.bcrypt(request.password)  # Hashクラスのbcryptメソッドを使用
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# Read all elements
def get_all_users(db: Session):
    return db.query(DbUser).all()
# Read one element
def get_user(db: Session, user_id: int):
    return db.query(DbUser).filter(DbUser.id == user_id).first()