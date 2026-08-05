# Script for grabbing posts content/
import os
def get_posts():
    posts_list = []
    full_paths = [os.path.join("content/", file) for file in os.listdir("content/")]
    for file in sorted(full_paths, key=os.path.getmtime, reverse=True):
        if file.endswith(".md") and ((not file.endswith("index.md")) and (not file.endswith("blog.md"))):
            with open(file, "r") as f:
                file_content = f.read().splitlines()
                filename = file.split("content/")[1].split(".md")[0]
                print(filename)
                title = [line for line in file_content if "title: " in line][0].split("title: ")[1]
                date = [line for line in file_content if "date: " in line][0].split("date: ")[1]
                desc = [line for line in file_content if "description: " in line][0].split("description: ")[1]
                posts_list.append((filename, title, date, desc))
    return posts_list