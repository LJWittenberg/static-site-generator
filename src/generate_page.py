import os

from markdown_blocks import( 
    markdown_to_html_node,
    extract_title,
)


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    #
    try:
        with open(from_path, "r", encoding="utf-8") as from_path_content:
            from_content = from_path_content.read()
        with open(template_path, "r", encoding="utf-8") as template_path_content:
            template_content = template_path_content.read()
    except Exception as e:
        print(e)
        return  # Exit the function if an error occurs
    Head_node = markdown_to_html_node(from_content)
    page_title = extract_title(from_content)
    final_content = template_content.replace("{{ Title }}", page_title).replace("{{ Content }}", Head_node.to_html())
    #
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, "w", encoding="utf-8") as dest_file:
        dest_file.write(final_content)