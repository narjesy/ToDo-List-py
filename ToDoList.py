import os
ToDo_File="tasks.txt"
def load_tasks():
   tasks=[]
   if os.path.exists(ToDo_File):
      with open(ToDo_File,"r", encoding="utf-8")as f:
         for line in f:
            line=line.strip()
            if line:
               parts=line.split("|")
               if len(parts)==2:
                  tasks.append({"title":parts[0],"done":parts[1]=="True"})
   return tasks
def save_tasks(tasks):
   with open(ToDo_File,"w",encoding="utf-8")as f:
         for task in tasks:
            f.write(f"{task['title']}|{task['done']}\n") 
def add_task(tasks):
   title=input("Enter task title : ").strip()
   if title:
       tasks.append({"title":title,"done":False})
       save_tasks(tasks)
       print(f"Task '{title}' added!")
   else:
       print("Task cannot be empty!")
def view_tasks(tasks):
   if not tasks:
      print("\n No tasks yet!")
      return
   print("\n"+"-"*40)
   for i,task in enumerate(tasks,1):
      status="✅"if task["done"] else "❌"
      print(f"{i}.{status} {task['title']}")
   print("-"*40)
def mark_done(tasks):
   if not tasks:
      print("No task to mark!")
      return
   view_tasks(tasks)
   try:
      index=int(input("Enter task number to mark as done : "))-1
      if 0<=index<len(tasks):
         if tasks[index]["done"]:
            print(f"task '{tasks[index]['title']}' is already done!")
         else:
            tasks[index]["done"] = True
            save_tasks(tasks)
            print(f" Task '{tasks[index]['title']}' marked as done!")
   except ValueError:
      print("Pleas enter a number!")
def delete_task(tasks):
   if not tasks:
      print("\n No tasks to delete!")
      return
   view_tasks(tasks)
   try:
      index=int(input("Enter task number to delete : "))-1
      if 0<=index<len(tasks):
         removed=tasks.pop(index)
         save_tasks(tasks)
         print(f" task '{removed['title']}' deleted!")
      else:
         print("invalid task number!")
   except ValueError:
      print("Pleas enter a number!")
def show_stats(tasks):
   if not tasks:
      print("\n No tasks yet!")
      return
   total=len(tasks)
   done=sum(1 for task in tasks if task["done"])
   not_done=total-done

   print("\n"+"="*30)
   print(f"Total tasks : {total}")
   print(f"Done : {done}")
   print(f"Pending : {not_done}")
   if total>0:
      print(f"progress : {done/total*100:.1f}%")
      print("="*30)
print("DEBUG:add_task function is",add_task)
tasks=load_tasks()
while True:

    print("\n"+"="*40)
    print("To-Do List Manager")
    print("="*40)
    print("1.add task")
    print("2.view all task")
    print("3.mark task as done")
    print("4.delete task")
    print("5.show stats")
    print("6.exit")
    print("="*40)
    choice=input("choose : ")

    if choice=="1":
        add_task(tasks)
    elif choice=="2":
       view_tasks(tasks)
    elif choice=="3":
       mark_done(tasks)
    elif choice=="4":
       delete_task(tasks)
    elif choice=="5":
       show_stats(tasks)
    elif choice=="6":
       print("Bye")
       break
    else:
        print("Invalid option!")
    input("\nPress Enter to continue...")