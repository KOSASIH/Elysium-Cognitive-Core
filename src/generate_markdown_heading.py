def generate_markdown_heading(level, content):
    if level < 1 or level > 6:
        raise ValueError("Heading level must be between 1 and 6")
    
    heading_symbol = '#' * level
    return f"{heading_symbol} {content}"

# Example usage
heading = generate_markdown_heading(1, "Main Heading")
print(heading)
