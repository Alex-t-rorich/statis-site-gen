def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:].strip()
    raise ValueError("No h1 header found in markdown file")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating {from_path} -> {dest_path}")
    
    with open(from_path, "r") as f:
        markdown_content = f.read()
    
    with open(template_path, "r") as f:
        template_content = f.read()
    
    from markdown_blocks import markdown_to_html_node
    html_node = markdown_to_html_node(markdown_content)
    html_content = html_node.to_html()
    title = extract_title(markdown_content)
    
    final_html = template_content.replace("{{ Title }}", title).replace("{{ Content }}", html_content)
    
    import os
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    with open(dest_path, "w") as f:
        f.write(final_html)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    import os
    from pathlib import Path
    
    for root, dirs, files in os.walk(dir_path_content):
        for file in files:
            if not file.endswith('.md'):
                continue
                
            rel_path = os.path.relpath(root, dir_path_content)
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir_path, rel_path, 'index.html')
            
            print(f"Processing: {src_file} -> {dest_file}")
            generate_page(src_file, template_path, dest_file)