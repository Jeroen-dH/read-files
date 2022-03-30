import time
with open (r"C:\Users\Jeroen\Desktop\Projecten\read-files\README.md") as file:
    for line in file:
        time.sleep(1)
        print(line)