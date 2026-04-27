import os
import json
from datetime import datetime
#-----------------------
#---storage functions---
#-----------------------
def load_json():
    if not os.path.exists('tasks.json'):
        return []
    with open ('tasks.json','r') as file:
        data=json.load(file)
    return data
def save_task(tasks):
    with open('tasks.json','w') as file:
        json.dump(tasks,file)
#-----------------------
#---task functions------
#-----------------------
def add_tasks(description):
    data=load_json()
    if not data:
        id=1
    else:
        field=max(data, key=lambda tasks:tasks["id"])
        id=field["id"] + 1
    current=datetime.now()
    update=datetime.now()
    tasks={"id":id,"description":description,"status":"todo","createdAt": current.isoformat(), "updatedAt": update.isoformat()}
    data.append(tasks)
    save_task(data)
    print("succesfully saved task")

def delete_tasks(id):
    data=load_json()
    if not any(task["id"] == id for task in data):
        print("task does not exist, input correct id!")
        return
    new_data=[task for task in data if task["id"]!=id]
    save_task(new_data)
    print("succesfully removed task")
