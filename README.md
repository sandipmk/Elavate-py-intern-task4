# Elevate Lab Python Internship — Task 4 -> REST API with flask.

## 📋 Task Overview
A simple REST API built with Flask for managing users in in-memory storage (list of dictionaries).

**Objective**:
  - Create REST API that manages user data
  - app with ** GET/POST/PUT/DELETE ** routes.

**Key Concepts**:
  - REST.
  - HTTP Methods.
  - Flask
    
---

## 📚 Approach

1. Setup Flask App

   - Imported Flask, request, and jsonify.

   - Initialized Flask instance.

2. In-Memory Data Storage

   - Used a Python list of dictionaries to store users instead of a database.

3. CRUD Endpoints

  - GET: Fetch all or specific users using Python list filtering.

  - POST: Generate new id dynamically, append to list.

  - PUT: Find user by ID, update fields if provided.

  - DELETE: Remove user by filtering list.

4. Error Handling

  - Returned "User not found" with HTTP 404 when ID is missing.

  - Used proper HTTP status codes (201, 204, etc.).


---

## ▶️ How to Run

# Install Flask
pip install flask

# Run the app
python app.py

# open endpiont file ** user_api.http **  and send request..
user_api.http

---

## Tools

  - python
  - Flask
  - Postman or Curl

---

