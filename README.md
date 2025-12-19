# 📝 OOP-Based Todo App (CLI, JSON Storage)

A simple **Command Line Interface (CLI) Todo application** built using **Python and Object-Oriented Programming (OOP)**.  
All tasks are stored locally in a **JSON file**, ensuring data persistence even after the program is closed and restarted.

---

## 📌 Project Overview

This project demonstrates how to:
- Design a Python application using **OOP principles**
- Persist data using **JSON serialization and deserialization**
- Build a functional **CRUD-based CLI application**

The app allows users to add, view, update, and delete todo tasks while automatically saving changes to a local file.

---

## ⚙️ Technical Requirements Fulfilled

### 1️⃣ Object-Oriented Design
The application is structured using classes:
- `Task` – Represents an individual todo item
- `TodoApp` – Manages all tasks and application logic

### 2️⃣ Data Persistence (JSON Serialization)
- Tasks are saved to a local file called `todos.json`
- Data is automatically reloaded when the program starts
- No database is used

---

## ✅ Functional Requirements

✔ Add a new todo  
✔ View all todos with ID, title, description, and status  
✔ Update todo title or description  
✔ Mark tasks as completed or incomplete  
✔ Delete todos by ID  
✔ Persistent storage using `todos.json`  

---
## 📄 JSON Serialization & Object Conversion

This application uses JSON serialization and deserialization to persist todo data without a database.

### 🔁 Converting Objects to JSON (Serialization)

Each todo task is represented by a `Task` object.  
Before saving to the `todos.json` file, every `Task` object is converted into a dictionary using the `to_dict()` method:

```python
def to_dict(self):
    return {
        'id': self.id,
        'title': self.title,
        'description': self.description,
        'completed': self.completed
    }


## 📂 Project Structure

