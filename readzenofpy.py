import time
file = open("C:\Users\Jeroen\Desktop\Projecten\read-files\README.md", "r")
for lines in file:
    time.sleep(1)
    print(file.readline())