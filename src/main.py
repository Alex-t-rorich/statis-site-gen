import os
import shutil

def copy_static(src: str, dst: str):
    # Remove existing destination if it exists
    if os.path.exists(dst):
        shutil.rmtree(dst)
    
    # Create destination directory
    os.mkdir(dst)
    
    # Copy files recursively
    for item in os.listdir(src):
        src_path = os.path.join(src, item)
        dst_path = os.path.join(dst, item)
        
        if os.path.isfile(src_path):
            shutil.copy(src_path, dst_path)
            print(f"Copied {src_path} to {dst_path}")
        else:
            copy_static(src_path, dst_path)

def main():
    copy_static("static", "public")

if __name__ == "__main__":
    main()