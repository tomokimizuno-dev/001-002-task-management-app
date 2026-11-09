from datetime import datetime
import numpy as np
import pandas as pd

task_list = []


def latest_ID(list):
    return max([_task['ID'] for _task in list])


def reg_new_task(task_list):
    if len(task_list) == 0:
        ID = 1
    else:
        ID = latest_ID(task_list) + 1

    while True:
        task_title = input('input your task: ')
        if task_title != "":
            break
        else:
            print("invalid input. Please enter at least one character.")

    while True:
        deadline = input('input deadline (yyyy-mm-dd): ')
        try:
            dt_deadline = datetime.strptime(deadline, '%Y-%m-%d')
            break
        except ValueError:
            print("invalid input. Please enter datetime in the correct format.")

    status = 'unfinished'

    task = {'ID': ID, 'task_title': task_title,
            'deadline': dt_deadline, 'status': status}

    return task


def view_table(task_list):
    return pd.DataFrame(task_list)


def search_ID(task_list):
    print(view_table(task_list))
    while True:
        hit_ID = int(input('enter task ID: '))
        for task in task_list:
            if task['ID'] == hit_ID:
                return task
        else:
            print('ID was not found.')


def update_status(updated_task):
    status = int(input('Task status? 1: unfinished 2: in progress 3: done '))
    match status:
        case 1:
            updated_task['status'] = 'unfinished'
        case 2:
            updated_task['status'] = 'in progress'
        case 3:
            updated_task['status'] = 'done'
        case 9:
            print("invalid input. Please correct number.")


def delete_task(deleted_task):
    while True:
        is_conf = int(input('Delete this task? 1: Yes 2: No '))
        match is_conf:
            case 1:
                task_list.remove(deleted_task)
                break
            case 2:
                print('interrupted.')
                break
            case 9:
                print("invalid input. Please correct number.")


def menu():
    while True:
        select = int(input(
            "Please select an action. 1: Add a new task. 2: View a task list. 3: Update status. 4: Delete task. 9: exit  "))
        match select:
            case 1:
                new_task = reg_new_task(task_list)
                task_list.append(new_task)
                print("Task added.")
            case 2:
                print(view_table(task_list))
            case 3:
                updated_task = search_ID(task_list)
                update_status(updated_task)
            case 4:
                deleted_task = search_ID(task_list)
                delete_task(deleted_task)
            case 9:
                break
            case _:
                print("invalid input. Please correct number.")


def __main__():
    menu()


__main__()
