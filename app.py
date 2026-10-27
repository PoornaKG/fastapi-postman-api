
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# API Key
API_KEY = "12345ABCDEF"


# Middleware to check API key
@app.middleware("http")
async def check_api_key(request: Request, call_next):
    # Public endpoints that do not require an API key
    public_paths = [
        "/",
        "/welcome",
        "/users",
        "/docs",
        "/openapi.json",
        "/redoc"
    ]

    if request.url.path in public_paths:
        return await call_next(request)

    # Read API key from request headers
    key = request.headers.get("X-API-KEY")

    # Debug: print the API key received
    print("Received API key:", repr(key))

    # Validate API key
    if key is None or key.strip() != API_KEY:
        return JSONResponse(
            status_code=401,
            content={
                "error": "Unauthorized. Please provide a valid X-API-KEY header."
            }
        )

    return await call_next(request)


# Pydantic model
class User(BaseModel):
    name: str
    role: str
    LinkedIn: str


# Temporary storage: initial user
users = {
    1: {
        "name": "Poorna Devi K G",
        "role": "Software Developer",
        "LinkedIn": "https://www.linkedin.com/in/poorna-devi-k-g/"
    }
}


# Home endpoint
@app.get("/")
def home():
    return {"message": "Welcome to my FastAPI app!"}


# Welcome endpoint
@app.get("/welcome")
def welcome():
    return {"message": "Welcome to my FastAPI app!"}


# GET API: retrieve all users
@app.get("/users")
def get_all_users():
    return {
        "users": [
            {"user_id": user_id, **user_data}
            for user_id, user_data in users.items()
        ]
    }


# GET API: retrieve the original profile
@app.get("/user")
def get_user_profile():
    return {
        "user_id": 1,
        **users[1]
    }


# GET API: retrieve a user by ID
@app.get("/user/{user_id}")
def get_user_by_id(user_id: int):
    if user_id in users:
        return {
            "user_id": user_id,
            **users[user_id]
        }

    return JSONResponse(
        status_code=404,
        content={
            "message": "User not found",
            "user_id": user_id
        }
    )


# POST API: add a new user
@app.post("/user", status_code=201)
def create_user(user: User):
    new_id = max(users.keys(), default=0) + 1
    users[new_id] = user.model_dump()

    return {
        "message": "User added successfully",
        "user_id": new_id,
        "user": users[new_id]
    }
