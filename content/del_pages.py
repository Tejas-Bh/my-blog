import os

for i in range(1, 101):
    filename = f"page{i}.md"
    
    if os.path.exists(filename):
        os.remove(filename)
        print(f"Deleted {filename}")
    else:
        print(f"{filename} not found")

print("Done.")