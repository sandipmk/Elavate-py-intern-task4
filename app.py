from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory user storage (list of dictionaries)
users = [
    {"id": 1, "name": "Sandip", "email": "sandip@example.com"},
    {"id": 2, "name": "Rahul", "email": "rahul@example.com"}
]

# GET all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

# GET single user by ID
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    return jsonify(user) if user else ("User not found", 404)

# POST - Add new user
@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    new_id = max([u["id"] for u in users]) + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201

# PUT - Update existing user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return ("User not found", 404)
    user["name"] = data.get("name", user["name"])
    user["email"] = data.get("email", user["email"])
    return jsonify(user)

# DELETE - Remove user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    users = [u for u in users if u["id"] != user_id]
    return ("", 204)

if __name__ == "__main__":
    app.run(debug=True)
