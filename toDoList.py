import json

class Task:
    def __init__(self, id, title, description="", completed=False):
        self.id = id
        self.title = title
        self.description = description
        self.completed = completed

    def to_dict(self):
        return {'id': self.id, 'title': self.title, 'description': self.description, 'completed': self.completed}

    @classmethod
    def from_dict(cls, data):
        return cls(data['id'], data['title'], data.get('description', ""), data['completed'])

class TodoApp:
    def __init__(self):
        self.tasks = []
        self.next_id = 1
        self.filename = 'todos.json'
        self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(d) for d in data]
                self.next_id = max((t.id for t in self.tasks), default=0) + 1
        except:
            pass  # Start empty if no file

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json.dump([t.to_dict() for t in self.tasks], f, indent=4)

    def add_task(self, title, description=""):
        task = Task(self.next_id, title, description)
        self.tasks.append(task)
        self.next_id += 1
        self.save_tasks()
        print(f"Added: {task.title}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
            return
        for t in self.tasks:
            status = "completed" if t.completed else "incomplete"
            desc = f" | {t.description}" if t.description else ""
            print(f"{t.id}: {t.title}{desc} - {status}")

    def update_task(self, id, new_title=None, new_desc=None, toggle=False):
        for t in self.tasks:
            if t.id == id:
                if new_title: t.title = new_title
                if new_desc is not None: t.description = new_desc
                if toggle: t.completed = not t.completed
                self.save_tasks()
                print(f"Updated task {id}.")
                return
        print("Task not found.")

    def delete_task(self, id):
        self.tasks = [t for t in self.tasks if t.id != id]
        self.save_tasks()
        print(f"Deleted task {id}.")

def main():
    app = TodoApp()
    print("Todo App")
    while True:
        print("\n1.Add 2.View 3.Update 4.Delete 5.Quit")
        try:
            c = int(input("Choice: "))
        except:
            continue
        if c == 1:
            title = input("Title: ").strip()
            desc = input("Desc (opt): ").strip()
            if title: app.add_task(title, desc)
        elif c == 2:
            app.view_tasks()
        elif c == 3:
            try:
                id = int(input("ID: "))
                print("1.Title 2.Desc 3.Toggle Complete")
                sc = input("Sub: ").strip()
                if sc == '1': app.update_task(id, new_title=input("New title: ").strip())
                elif sc == '2': app.update_task(id, new_desc=input("New desc: ").strip())
                elif sc == '3': app.update_task(id, toggle=True)
            except: pass
        elif c == 4:
            try: app.delete_task(int(input("ID: ")))
            except: pass
        elif c == 5:
            break

if __name__ == "__main__":
    main()