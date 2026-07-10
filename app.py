import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


def get_db_connection():
    connection = sqlite3.connect("database.db")
    connection.row_factory = sqlite3.Row
    return connection


def init_db():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS todos(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


# def add_todo(title):
#     connection = get_db_connection()

#     connection.execute(
#         "INSERT INTO todos(title) VALUES(?)",
#         (title,)
#     )

#     connection.commit()
#     connection.close()


# def get_all_todos():
#     connection = get_db_connection()

#     todos = connection.execute(
#         "SELECT * FROM todos ORDER BY id DESC"
#     ).fetchall()

#     connection.close()

#     return todos


# def delete_todo(todo_id):
#     connection = get_db_connection()

#     connection.execute(
#         "DELETE FROM todos WHERE id=?",
#         (todo_id,)
#     )

#     connection.commit()
#     connection.close()


# def update_todo(todo_id, title):
#     connection = get_db_connection()

#     connection.execute(
#         """
#         UPDATE todos
#         SET title=?
#         WHERE id=?
#         """,
#         (title, todo_id)
#     )

#     connection.commit()
#     connection.close()


# def toggle_complete(todo_id):
#     connection = get_db_connection()

#     connection.execute(
#         """
#         UPDATE todos
#         SET completed = NOT completed
#         WHERE id=?
#         """,
#         (todo_id,)
#     )

#     connection.commit()
#     connection.close()


# @app.route("/", methods=["GET", "POST"])
# def home():

#     if request.method == "POST":
#         title = request.form["title"].strip()

#         if title:
#             add_todo(title)

#         return redirect(url_for("home"))

#     todos = get_all_todos()

#     return render_template(
#         "index.html",
#         todos=todos
#     )


# @app.route("/delete/<int:todo_id>")
# def delete(todo_id):
#     delete_todo(todo_id)
#     return redirect(url_for("home"))


# @app.route("/toggle/<int:todo_id>")
# def toggle(todo_id):
#     toggle_complete(todo_id)
#     return redirect(url_for("home"))


# @app.route("/edit/<int:todo_id>", methods=["POST"])
# def edit(todo_id):
#     title = request.form["title"].strip()

#     if title:
#         update_todo(todo_id, title)

#     return redirect(url_for("home"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)