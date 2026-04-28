#!/usr/bin/env python3
import argparse
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

def update_tasks(id,description):
    data=load_json()
    if not any(task["id"] == id for task in data):
        print("task does not exist, input correct id!")
        return
    for task in data:
        if task["id"]==id:
            task["description"]=description
            task["updatedAt"]=(datetime.now()).isoformat()
    save_task(data)
    print("succesfully updated task")

def mark_tasks(id,status):
    data=load_json()
    if not any(task["id"] == id for task in data):
        print("task does not exist, input correct id!")
        return
    for task in data:
        if task["id"]==id:
            task["status"]=status
            task["updatedAt"]=(datetime.now()).isoformat()
    save_task(data)
    print("succesfully updated task status")

def list_tasks(status=None):
    data=load_json()
    if status==None:
        for task in data:
            print(f"{task['id']} {task['description']}")
    else:
        for task in data:
            if task["status"]==status:
                print(f"{task['id']} {task['description']}")

   
#-----------------------
#---main parser---------
#-----------------------
if __name__=="__main__":
    parser = argparse.ArgumentParser()
    subparser=parser.add_subparsers(dest="command")
    add_parser=subparser.add_parser("add")
    add_parser.add_argument("description")
    delete_parser=subparser.add_parser("delete")
    delete_parser.add_argument("id",type=int)
    update_parser=subparser.add_parser("update")
    update_parser.add_argument("id",type=int)
    update_parser.add_argument("description")
    mark_parser=subparser.add_parser("mark")
    mark_parser.add_argument("id",type=int)
    mark_parser.add_argument("status")
    list_parser=subparser.add_parser("list")
    list_parser.add_argument("status",nargs="?",default=None)
    args=parser.parse_args()
    if args.command=="add":
        add_tasks(args.description)
    elif args.command=="delete":
        delete_tasks(args.id)
    elif args.command=="update":
        update_tasks(args.id,args.description)
    elif args.command=="mark":
        mark_tasks(args.id,args.status)
    elif args.command=="list":
        list_tasks(args.status)
    
    
    
