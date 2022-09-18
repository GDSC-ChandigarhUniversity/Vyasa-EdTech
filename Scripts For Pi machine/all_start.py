import os
os.system("python3 req_down.py| tee -a files_to_download.txt")
os.system("python3 json_cov.py")
os.system("python3 names.py >> names_new.html")
os.system("python3 -m http.server")

