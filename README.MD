# 📝 FastAPI Social Posts API

A RESTful API built with **FastAPI** that provides user authentication and post management. Users must create an account before they can log in and access the application's features.

Once authenticated, users can create, view, update, delete, and like posts. Users can also browse posts created by other users.

---

## ✨ Features

### Authentication
- User registration (Sign Up)
- User login using JWT authentication
- Password hashing for secure password storage
- Protected routes that require authentication

### Posts
- Create a new post
- Retrieve all posts
- Retrieve a single post
- Update your own posts
- Delete your own posts
- View posts created by other users

### Likes
- Like a post
- Remove a like from a post
- Count the number of likes on each post

---

## 🛠️ Tech Stack

- Python 3
- FastAPI
- SQLAlchemy
- PostgreSQL
- Alembic
- Pydantic
- JWT Authentication
- Passlib (Password Hashing)
- Uvicorn

---

## 📂 Project Structure

```text
.
├── alembic/
├── app/
│   ├── routers/
│   ├── models.py
│   ├── schemas.py
│   ├── oauth2.py
│   ├── database.py
│   ├── utils.py
│   ├── config.py
│   └── main.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/your-repository.git

cd your-repository
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### Linux / macOS

```bash
python3 -m venv venv

source venv/bin/activate
```

---

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure environment variables

Create a `.env` file in the project root.

Example:

```env
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_NAME=your_database
DATABASE_USERNAME=postgres
DATABASE_PASSWORD=your_password

SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

---

### 5. Run database migrations

```bash
alembic upgrade head
```

---

### 6. Start the application

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

Interactive API documentation:

```
http://127.0.0.1:8000/docs
```

Alternative documentation:

```
http://127.0.0.1:8000/redoc
```

---

# Authentication Flow

## 1. Register

Create a new account.

```
POST /users
```

---

## 2. Login

Authenticate using your email/username and password.

```
POST /login
```

A JWT access token will be returned.

---

## 3. Access Protected Endpoints

Include the token in the Authorization header.

```
Authorization: Bearer <your_access_token>
```

---

# Posts Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| GET | `/posts` | Get all posts |
| GET | `/posts/{id}` | Get a single post |
| POST | `/posts` | Create a new post |
| PUT | `/posts/{id}` | Update your post |
| DELETE | `/posts/{id}` | Delete your post |

---

# Likes Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/vote` | Like or unlike a post |

---

## 🔒 Permissions

- Only authenticated users can access protected routes.
- Users can only edit their own posts.
- Users can only delete their own posts.
- Users can view posts created by other users.
- Logged-in users can like or unlike posts.

---

## 📖 API Documentation

FastAPI automatically generates interactive API documentation.

Swagger UI:

```
/docs
```

ReDoc:

```
/redoc
```

---

## 🔐 Security

- JWT Authentication
- Password hashing using Passlib
- Protected API routes
- Ownership validation before updating or deleting posts

---

## Future Implementations

- Comments on posts
- User profiles
- Follow/unfollow users
- Pagination
- Search and filtering
- Image uploads
- Email verification
- Password reset
- Refresh tokens