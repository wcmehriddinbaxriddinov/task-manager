import csv

def show_tasks():
    with open("tasks.csv", "r") as file:
        viewer = csv.DictReader(file)
        xotira = list(viewer)
        
    for vazifa in xotira:
        print(f"{vazifa['id']}. {vazifa['name']} - {vazifa['status']}")
        
show_tasks()       