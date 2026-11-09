# dict型の確認
import pandas as pd
import numpy as np
task_1 = {'ID': 1, 'task_title': 'ゴミ出しをする',
          'deadline': 2026-11-9, 'status': 'unfinished'}
task_2 = {'ID': 2, 'task_title': 'トマトを買う',
          'deadline': 2026-11-8, 'status': 'completed'}
task_3 = {'ID': 3, 'task_title': '風呂掃除',
          'deadline': 2026-11-15, 'status': 'finished'}
task_list = [task_1, task_2]
task_list.append(task_3)
print(task_list)
# appendにより新規タスク（dict型）をtask_listに加えることができた

# 付番された中で最大のIDを求める→+1すれば新規IDに
print(max([_task['ID'] for _task in task_list]))

# ただしリストが空の場合は使用できない
# task_list = []
# print(len(task_list))

# 表形式での表示チェック
df = pd.DataFrame(task_list)
print(df)

# 検索関数の検討
update_ID = 3
for _task in task_list:
    if _task['ID'] == update_ID:
        print(_task)
        break
else:
    print('no_ID')

# 削除仕様の確認


def search_ID(update_ID):
    for task in task_list:
        if task['ID'] == update_ID:
            return task
    else:
        print('no_ID')


print(task_list)
update_ID = 2
task = search_ID(update_ID)
task_list.remove(task)
print(task_list)
