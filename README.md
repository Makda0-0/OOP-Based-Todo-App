# OOP-Based-Todo-App


A command-line Todo application built with Object-Oriented Programming principles and local JSON persistence.

## 📁 Project Files

### `todo_app.py`
Main application file containing all the core logic and classes.

### **Classes Overview**

#### **Task Class**
Represents individual todo items with the following structure:

**Attributes:**
- `id` (int): Unique identifier for each task
- `title` (str): Main task description
- `description` (str): Optional detailed description
- `completed` (bool): Completion status (default: False)

**Methods:**
- `__init__(self, id, title, description="", completed=False)` - Constructor
- `to_dict(self)` - Converts Task object to serializable dictionary
- `from_dict(cls, data)` - Class method to create Task from dictionary

#### **TodoApp Class**
Manages the collection of tasks and handles file operations.

**Attributes:**
- `tasks` (list): Collection of Task objects
- `next_id` (int): Auto-incrementing ID counter
- `filename` (str): JSON storage file name ('todos.json')

**Key Methods:**

**File Operations:**
- `load_tasks()` - Reads JSON file and creates Task objects on startup
- `save_tasks()` - Serializes all tasks to JSON file

**CRUD Operations:**
- `add_task(title, description="")` - Creates and saves new task
- `view_tasks()` - Displays all tasks with details
- `update_task(id, new_title=None, new_desc=None, toggle=False)` - Modifies existing task
- `delete_task(id)` - Removes task by ID

### **Main Function (`main()`)**
Program entry point that provides the user interface:

**Menu System:**
1. **Add Task** - Prompts for title and optional description
2. **View Tasks** - Lists all tasks with formatting
3. **Update Task** - Sub-menu for modifying task attributes
4. **Delete Task** - Removes task by entering ID
5. **Quit** - Exits application

## 🔄 Data Flow

### **Serialization (Save)**
