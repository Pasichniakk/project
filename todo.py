class ToDoApp:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Завдання '{task}' додано.")

    def view_tasks(self):
        if not self.tasks:
            print("Завдань немає.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                status = "виконано" if task["completed"] else "не виконано"
                print(f"{idx}. {task['task']} - {status}")

    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Завдання '{self.tasks[task_number - 1]['task']}' позначено як виконане.")
        else:
            print("Невірний номер завдання.")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            print(f"Завдання '{deleted_task['task']}' видалено.")
        else:
            print("Невірний номер завдання.")

    def run(self):
        while True:
            print("\nМеню:")
            print("1. Додати завдання")
            print("2. Переглянути завдання")
            print("3. Позначити завдання як виконане")
            print("4. Видалити завдання")
            print("5. Вийти")

            choice = input("Оберіть дію (1-5): ")

            if choice == "1":
                task = input("Введіть завдання: ")
                self.add_task(task)
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                task_number = int(input("Введіть номер завдання для позначення як виконане: "))
                self.complete_task(task_number)
            elif choice == "4":
                task_number = int(input("Введіть номер завдання для видалення: "))
                self.delete_task(task_number)
            elif choice == "5":
                print("Вихід з програми.")
                break
            else:
                print("Невірний вибір. Спробуйте ще раз.")


if __name__ == "__main__":
    app = ToDoApp()
    app.run()
