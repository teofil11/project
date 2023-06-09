from functions.typefile import isCsv,isTxt

def format_file(file_name,content):
    """
    Format the content of a file for further processing.

    Args:
        file_name (str): The name of the file.
        content (list): The content of the file.
    Returns:
        list: The formatted lines of the file.
    """
    lines = []
    if isCsv(file_name) is True:
        for line in content:
            cleaned_row = [item.replace("T", " ").replace("Z", "") for item in line]
            lines.append(cleaned_row)
        return lines
    if isTxt(file_name) is True:
        for line in content:
            cleaned_row = line.rstrip(";\n ").replace('T', " ").replace('Z', '')
            lines.append(cleaned_row)
        return lines