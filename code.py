import json
import os
import datetime
import time

# --- Configuration ---
TASKS_FILE = "tasks.json"

# --- Emojis for the UI ---
EMOJI_STATUS_PENDING = "⏳"
EMOJI_STATUS_COMPLETE = "✅"
EMOJI_ADD = "📝"
EMOJI_VIEW = "📜"
EMOJI_DELETE = "🗑️"
EMOJI_MARK = "✔️"
EMOJI_QUIT = "👋"
EMOJI_SUCCESS = "🎉"
EMOJI_ERROR = "❌"
EMOJI_THINKING = "🤔"
EMOJI_STAR = "✨"

# --- Helper Functions ---

def clear_screen():
    """Clears the terminal screen for a clean UI."""
    # 'nt' is for Windows, 'posix' is for Linux/macOS/Android(Termux)
    os.system('cls' if os.name == 'nt' else 'clear')

def load_tasks():
    """Loads tasks from the JSON file."""
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Saves the current list of tasks to the JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=4)

# --- Core Application Functions ---

def display_tasks(tasks):
    """Displays all the tasks in a formatted, user-friendly way."""
    clear_screen()
    print(f"{EMOJI_STAR} TidyTasks - Your Awesome Task Manager {EMOJI_STAR}\n")
    print(f"{EMOJI_VIEW} Your To-Do List:")
    print("-" * 40)

    if not tasks:
        print(f"\n{EMOJI_SUCCESS} Hooray! Your list is empty. Time for a break! {EMOJI_SUCCESS}\n")
    else:
        sorted_tasks = sorted(tasks, key=lambda x: x['status'] == 'completed')
        for i, task in enumerate(sorted_tasks, 1):
            status_emoji = EMOJI_STATUS_COMPLETE if task['status'] == 'completed' else EMOJI_STATUS_PENDING
            print(f"{i}. {status_emoji} {task['description']} (Added: {task['created_at']})")
    
    print("-" * 40)

def add_task(tasks):
    """Prompts the user to add a new task."""
    clear_screen()
    print(f"{EMOJI_ADD} Add a New Task\n")
    description = input("What do you need to get done? \n> ")

    if not description.strip():
        print(f"\n{EMOJI_ERROR} Task description cannot be empty.")
        time.sleep(2)
        return

    new_task = {
        "description": description,
        "status": "pending",
        "created_at": datetime.date.today().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"\n{EMOJI_SUCCESS} Task '{description}' added successfully!")
    time.sleep(2)

def mark_task_complete(tasks):
    """Marks a specific task as complete."""
    display_tasks(tasks)
    if not any(t['status'] == 'pending' for t in tasks):
        print(f"\n{EMOJI_SUCCESS} No pending tasks to mark as complete. Great job!")
        time.sleep(2)
        return

    try:
        task_num_str = input(f"\n{EMOJI_THINKING} Enter the number of the task to mark as complete: ")
        task_num = int(task_num_str)
        sorted_tasks = sorted(tasks, key=lambda x: x['status'] == 'completed')
        
        if 0 < task_num <= len(sorted_tasks):
            task_to_update = sorted_tasks[task_num - 1]
            for original_task in tasks:
                if original_task is task_to_update:
                    original_task['status'] = 'completed'
                    break
            save_tasks(tasks)
            print(f"\n{EMOJI_SUCCESS} Great work! Task marked as complete!")
        else:
            print(f"\n{EMOJI_ERROR} Oops! That's not a valid task number.")
    except ValueError:
        print(f"\n{EMOJI_ERROR} Invalid input. Please enter a number.")
    time.sleep(2)


def delete_task(tasks):
    """Deletes a task from the list."""
    display_tasks(tasks)
    if not tasks:
        print("\nNothing to delete!")
        time.sleep(2)
        return

    try:
        task_num_str = input(f"\n{EMOJI_THINKING} Enter the number of the task to delete: ")
        task_num = int(task_num_str)
        sorted_tasks = sorted(tasks, key=lambda x: x['status'] == 'completed')
        
        if 0 < task_num <= len(sorted_tasks):
            task_to_delete = sorted_tasks[task_num - 1]
            tasks.remove(task_to_delete)
            save_tasks(tasks)
            print(f"\n{EMOJI_DELETE} Task has been successfully deleted.")
        else:
            print(f"\n{EMOJI_ERROR} Oops! That's not a valid task number.")
    except ValueError:
        print(f"\n{EMOJI_ERROR} Invalid input. Please enter a number.")
    time.sleep(2)


def main():
    """The main function to run the application."""
    tasks = load_tasks()
    while True:
        display_tasks(tasks)
        print("\nWhat would you like to do?")
        print(f"  1. {EMOJI_ADD} Add Task")
        print(f"  2. {EMOJI_MARK} Mark Task as Complete")
        print(f"  3. {EMOJI_DELETE} Delete Task")
        print(f"  4. {EMOJI_QUIT} Quit")
        choice = input("\nEnter your choice (1-4): ")

        if choice == '1': add_task(tasks)
        elif choice == '2': mark_task_complete(tasks)
        elif choice == '3': delete_task(tasks)
        elif choice == '4':
            print(f"\n{EMOJI_QUIT} Goodbye! Keep up the great work! {EMOJI_STAR}\n")
            break
        else:
            print(f"\n{EMOJI_ERROR} Invalid choice. Please select a number from 1 to 4.")
            time.sleep(2)

if __name__ == "__main__":
    main()