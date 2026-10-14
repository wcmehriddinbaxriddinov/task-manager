import csv

def complete_task():
    with open("tasks.csv", "r") as file:
        viewer = csv.DictReader(file)
        xotira = list(viewer)
        
    print("Vazifalar ro'yxati:")
    for vazifa in xotira:
        print(f"- {vazifa['id']}. {vazifa['name']} - {vazifa['status']}")
        
    vazifa_id = input("Bajarilgan vazifa id sini kiriting: ")
    
    topildi = False
    
    for vazifa in xotira:
        if vazifa['id'] == vazifa_id:
            vazifa['status'] = "bajarilgan"
            topildi = True
    
    if topildi:
        with open("tasks.csv", "w") as file:
            file.write("id,name,status\n")
            for vazifa in xotira:
                file.write(f"{vazifa['id']},{vazifa['name']},{vazifa['status']}\n")
        print(f"{vazifa_id} - vazifa bajarilgan deb belgilandi")
    else:
        print("Bunday id topilmadi")
        
complete_task()