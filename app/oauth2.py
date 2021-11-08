from jose import JWTError, jwt
from datetime import datetime, timedelta

# SECRET KEY
# ALGORITHM
# EXPIRATION TIME

SECRET_KEY = "ASDSJjdjJAHSBHDBBXSDBCHJBB4U5T75U49E8UI357YRHCCBGURT6TGH5T46"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
