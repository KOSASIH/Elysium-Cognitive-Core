def generate_bullet_list(data):
    markdown = ""
    for item in data:
        markdown += f"- {item}\n"
    return markdown
