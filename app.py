from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = (
    f"mysql+pymysql://"
    f"{os.getenv('MYSQL_USER')}:"
    f"{os.getenv('MYSQL_PASSWORD')}@"
    f"mysql:3306/"
    f"{os.getenv('MYSQL_DATABASE')}"
)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class Task(db.Model):
    __tablename__ = "tasks"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    completed = db.Column(db.Boolean, default=False)


def task_to_dict(task):
    return {
        "id": task.id,
        "title": task.title,
        "completed": task.completed
    }


@app.route("/api/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.order_by(Task.id.desc()).all()
    return jsonify([task_to_dict(task) for task in tasks])


@app.route("/api/tasks", methods=["POST"])
def add_task():
    data = request.get_json()

    title = data.get("title", "").strip()

    if not title:
        return jsonify({"error": "Task title is required"}), 400

    task = Task(title=title)

    db.session.add(task)
    db.session.commit()

    return jsonify(task_to_dict(task)), 201


@app.route("/api/tasks/<int:id>", methods=["PUT"])
def update_task(id):
    task = Task.query.get_or_404(id)

    data = request.get_json()

    if "completed" in data:
        task.completed = bool(data["completed"])

    db.session.commit()

    return jsonify(task_to_dict(task))


@app.route("/api/tasks/<int:id>", methods=["DELETE"])
def delete_task(id):
    task = Task.query.get_or_404(id)

    db.session.delete(task)
    db.session.commit()

    return jsonify({"message": "Task deleted"})


@app.route("/api/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )
