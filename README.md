# Personal Task Manager CLI

## Description
A command-line application for managing personal tasks efficiently. 
This tool allows you to add, update, and delete tasks directly from the terminal. 
It also provides functionality to track the status of tasks.

## Features
- Add new tasks with a unique identifier, description, and status.
- Update existing tasks, including their description and status.
- Delete tasks.
- Mark tasks as "in progress" or "done."
- List all tasks.
- List tasks by status:
  - Tasks that are done.
  - Tasks that are not done.
  - Tasks that are in progress.
- Interactive mode for easier task management.

## Task Properties
Each task has the following properties:
- `id`: A unique identifier for the task.
- `description`: A short description of the task.
- `status`: The status of the task (`todo`, `in-progress`, `done`).
- `createdAt`: The date and time when the task was created.
- `updatedAt`: The date and time when the task was last updated.
