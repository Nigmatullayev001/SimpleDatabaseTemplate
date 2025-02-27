import sqlite3

class UserDatabase:
    def __init__(self):
        self.conn = sqlite3.connect("users.db")
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        """Creates the users table if it doesn't exist."""
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL
        )
        """)
        self.conn.commit()

    def add_user(self, name, phone):
        """Adds a new user to the database."""
        self.cursor.execute("INSERT INTO users (name, phone) VALUES (?, ?)", (name, phone))
        self.conn.commit()

    def get_users(self):
        """Gets all users."""
        self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def update_user(self, user_id, name, phone):
        """Updates a user's name and phone number by ID."""
        self.cursor.execute("UPDATE users SET name = ?, phone = ? WHERE id = ?", (name, phone, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        """Deletes a user by ID."""
        self.cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.conn.commit()

    def close(self):
        """Closes the database connection."""
        self.conn.close()


# Example usage
if __name__ == "__main__":
    db = UserDatabase()

    # Adding users
    db.add_user("Alice", "+998901234567")
    db.add_user("Bob", "+998901234568")

    # Updating user
    db.update_user(1, "Alice Updated", "+998909876543")

    # Fetching and displaying users
    users = db.get_users()
    for user in users:
        print(user)

    # Deleting a user
    db.delete_user(2)

    db.close()
