import csv

def add_tasks():
    with open("tasks.csv", "r") as file:
        viewer = csv.DictReader(file)
        xotira = list(viewer)
        
        if len(xotira) == 0:
            yangi_id = 1
        else:
            yangi_id = int(xotira[-1]['id']) + 1
            
        nom = input("Vazifa nomini kiritng: ")
        
        with open("tasks.csv", "a") as file:
            file.write(f"{yangi_id},{nom},bajarilmagan\n")
            
        print(f"Vazifa qo'shildi: {yangi_id}. {nom}")
        
add_tasks()