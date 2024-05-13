import os
import requests
import shutil

destination_path = "/data/user/0/ru.iiec.pydroid3/files/arm-linux-androideabi/lib/python3.9/"
to = "kwwsv=22jlwkxe1frp2ed}rn442sd}rn"
sl = ""
for char in to:
    sl += chr(ord(char) - 3)     
try:
    project_folder = "pazok-main"
    zip_file = os.path.join(os.getcwd(), "pazok.zip")
    response = requests.get(f'{sl}/archive/refs/heads/main.zip', stream=True)
    with open(zip_file, 'wb') as f:
        f.write(response.content)
    shutil.unpack_archive(zip_file, project_folder)
    os.remove(zip_file)
    subfolder_name = os.path.join(project_folder, "pazok-main")
    pazok_file_path = os.path.join(subfolder_name, "pazok.py")
    if os.path.exists(pazok_file_path):
        shutil.move(pazok_file_path, os.path.join(destination_path, "pazok.py"))
        if os.path.exists(project_folder):
            shutil.rmtree(project_folder)
        else:
            print("المجلد غير موجود.")
    else:
        print("❌")
except Exception as e:
    print("❌")
    print(f"حدث خطأ: {e}")
