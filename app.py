import argparse
from datetime import datetime

from helpers import initialize_tasks_file, load_tasks, save_tasks


# Add a new task
def add_task(description):
    tasks, task_id_counter = load_tasks()
    task_id = max((task["id"] for task in tasks), default=0) + 1
    now = datetime.now()
    formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "created_at": formatted_time,
        "updated_at": formatted_time,
    }
    tasks.append(new_task)
    task_id_counter += 1
    save_tasks(tasks, task_id_counter)
    print(f"Task added: {new_task}")


# Update an existing task
def update_task(task_id, new_description):
    tasks, task_id_counter = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            now = datetime.now()
            task["updated_at"] = now.strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks, task_id_counter)
            print(f"Task updated: {task}")
            return
    print("Task not found.")


# Delete a task
def delete_task(task_id):
    tasks, task_id_counter = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks, task_id_counter)
    print(f"Task {task_id} deleted.")


# Mark a task as in-progress or done
def mark_task(task_id, status):
    allowed_statuses = ["todo", "in-progress", "done"]
    if status not in allowed_statuses:
        print(f"Error: Invalid status. Allowed statuses are: {', '.join(allowed_statuses)}")
        return

    tasks, task_id_counter = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = status
            now = datetime.now()
            task["updated_at"] = now.strftime("%Y-%m-%d %H:%M:%S")
            save_tasks(tasks, task_id_counter)
            print(f"Task marked as {status}: {task}")
            return
    print("Task not found.")


# List of all tasks, optionally filtered by status
def list_tasks(status=None):
    allowed_statuses = ["todo", "in-progress", "done"]
    if status and status not in allowed_statuses:
        print(f"Error: Invalid status. Allowed statuses are: {', '.join(allowed_statuses)}")
        return

    tasks, _ = load_tasks()
    filtered_tasks = tasks if status is None else [task for task in tasks if task["status"] == status]

    if not filtered_tasks:
        print("No tasks found.")
        return

    print(f"{'ID':<5} {'Description':<30} {'Status':<15} {'Created At':<20} {'Updated At':<20}")
    print("-" * 90)
    for task in filtered_tasks:
        print(f"{task['id']:<5} {task['description']:<30} {task['status']:<15} {task['created_at']:<20} "
              f"{task['updated_at']:<20}")


# Main function to handle command-line arguments
def main():
    initialize_tasks_file()
    parser = argparse.ArgumentParser(description="Personal Task Manager CLI")
    parser.add_argument("command", choices=["add", "update", "delete", "mark", "list"], help="Command to execute")
    parser.add_argument("args", nargs="*", help="Arguments for the command")
    args = parser.parse_args()

    if args.command == "add":
        if len(args.args) < 1:
            print("Error: Task description is required.")
        else:
            add_task(args.args[0])
    elif args.command == "update":
        if len(args.args) < 2:
            print("Error: Task ID and new description are required.")
        else:
            update_task(int(args.args[0]), args.args[1])
    elif args.command == "delete":
        if len(args.args) < 1:
            print("Error: Task ID is required.")
        else:
            delete_task(int(args.args[0]))
    elif args.command == "mark":
        if len(args.args) < 2:
            print("Error: Task ID and status are required.")
        else:
            mark_task(int(args.args[0]), args.args[1])
    elif args.command == "list":
        status = args.args[0] if args.args else None
        list_tasks(status)


if __name__ == "__main__":
    main()
