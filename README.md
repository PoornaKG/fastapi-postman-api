🚀 FastAPI User Management REST API

A hands-on Python project built with FastAPI to explore REST API development and testing using Postman. Features include retrieving all users, fetching user details by individual ID, creating new users with auto-generated IDs, JSON request/response handling, Pydantic validation, and API-key middleware for endpoint protection.

📌 Key Features:
- GET `/users` – Retrieve all users
- GET `/user/{user_id}` – Fetch a specific user by ID
- GET `/user` – Retrieve the default user profile
- POST `/user` – Create a new user with an automatically assigned ID
- GET `/welcome` – Welcome endpoint
- API-key validation using custom middleware
- Interactive API documentation with Swagger UI
- Endpoint testing using Postman

🛠️ Tech Stack: Python, FastAPI, Uvicorn, Pydantic, Postman, REST APIs.

🎯 Learning Goal: Build, test, and understand RESTful APIs, HTTP methods, JSON data exchange, request validation, and API access control.

Note: User data is stored temporarily in memory and resets when the server restarts.
