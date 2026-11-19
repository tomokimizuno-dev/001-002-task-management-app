from datetime import datetime, date
import numpy as np
import pandas as pd
import json
import copy


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


def read_file():
    print('Checking the relevant file...')
    try:
        with open('task_list.json', 'xt', encoding='utf-8') as file:
            task_list = []
            return task_list
            print('No relevant file. Created a new file.')
    except FileExistsError:
        with open('task_list.json', 'r', encoding='utf-8') as file:
            task_list = json.load(file)
            print('Loading the relevant file...')
            task_list = str_to_datetime(task_list)
            print('Converting data type...')
            return task_list


def save_file(task_list):
    task_list_for_save = copy.deepcopy(task_list)
    task_list_for_JSON = datetime_to_str(task_list_for_save)
    with open('task_list.json', 'wt', encoding='utf-8') as file:
        json.dump(task_list_for_JSON, file)


def datetime_to_str(task_list):
    for task in task_list:
        task['deadline'] = task['deadline'].isoformat()
        return task_list


def str_to_datetime(task_list):
    for task in task_list:
        deadline = str(task['deadline'])
        deadline = datetime.fromisoformat(deadline)
        task['deadline'] = deadline.date()
        return task_list


def menu(task_list):
    while True:
        select = int(input(
            "Please select an action. 1: Add a new task. 2: View a task list. 3: Update status. 4: Delete task. 5: Save to JSON. 9: exit  "))
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
            case 5:
                save_file(task_list)
                print('saved.')
            case 9:
                break
            case _:
                print("invalid input. Please correct number.")


def __main__():
    task_list = read_file()
    menu(task_list)


__main__()
