# Task Tracker CLI

A simple command line interface to track and manage your tasks. Built with Python using only the standard library.

## Features

- Add, update, and delete tasks
- Mark tasks as in-progress or done
- List all tasks or filter by status
- Tasks are persisted in a local JSON file

## Requirements

- Python 3.x

## Setup

Clone the repository and navigate into the project directory:

```bash
git clone https://github.com/your-username/task-tracker
cd task-tracker
```

No dependencies to install. The project uses only Python's built-in libraries.

## Usage

### Add a task

```bash
python task_cli.py add "Buy groceries"
# Output: Task added successfully (ID: 1)
```

### Update a task

```bash
python task_cli.py update 1 "Buy groceries and cook dinner"
```

### Delete a task

```bash
python task_cli.py delete 1
```

### Mark a task as in-progress

```bash
python task_cli.py mark-in-progress 1
```

### Mark a task as done

```bash
python task_cli.py mark-done 1
```

### List all tasks

```bash
python task_cli.py list
```

### List tasks by status

```bash
python task_cli.py list done
python task_cli.py list todo
python task_cli.py list in-progress
```

## Task Properties

Each task stored in `tasks.json` has the following properties:

| Property | Description |
|---|---|
| `id` | Unique identifier for the task |
| `description` | Short description of the task |
| `status` | Current status: `todo`, `in-progress`, or `done` |
| `createdAt` | Date and time the task was created |
| `updatedAt` | Date and time the task was last updated |

## Project Structure

```
task-tracker/
│
├── task_cli.py       # Entry point and all application logic
└── tasks.json        # Auto-generated on first run
```

## Notes

- `tasks.json` is created automatically in the current directory on the first run
- Task IDs are auto-incremented and never reused