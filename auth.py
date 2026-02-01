import jwt
from config import SECRET_KEY

def validate_token(token: str) -> bool:
    try:
        jwt.decode(token, SECRET_KEY, algorithms=["HS256"], options={"verify_exp": False})
        return True  
    except jwt.InvalidTokenError:
        return False 
