import os
import shutil
from copystatic import copy_files_recursiv
from generate_page import generate_page_recursive

dir_path_static = "./static"
dir_path_public = "./public"
from_path = "content/"
template_path = "template.html"
dest_path = "public/"

def main():
    print("deleting public directory")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)
    print("Copying static files to public directory...")
    copy_files_recursiv(dir_path_static, dir_path_public)
    generate_page_recursive(from_path, template_path, dest_path)


main()