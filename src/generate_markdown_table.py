def generate_markdown_table(data):
    # Get the keys from the dictionary for table headers
    headers = list(data.keys())

    # Generate the table header row
    header_row = "| " + " | ".join(headers) + " |"

    # Generate the table header separator row
    separator_row = "| " + " | ".join(["---"] * len(headers)) + " |"

    # Generate the table rows
    rows = []
    for values in zip(*data.values()):
        row = "| " + " | ".join(str(value) for value in values) + " |"
        rows.append(row)

    # Combine all the rows into a markdown table
    markdown_table = "\n".join([header_row, separator_row] + rows)

    return markdown_table
