import os

def get_files_info(working_directory, directory=None):
    absolute_working = os.path.abspath(working_directory)
    if directory == None:
        directory = absolute_working
    elif os.path.isabs(directory):
        absolute_path = os.path.abspath(directory)
    else:
        absolute_path = os.path.abspath(os.path.join(absolute_working, directory))

    # If directory argument is outside of working directory
    separator = os.path.sep
    if not (absolute_path.startswith(absolute_working + separator) or absolute_path == absolute_working):
        return f'Error: Cannot list "{absolute_path}" as it is outside the permitted working directory'

    # If directory argument is not a directory
    if not os.path.isdir(absolute_path):
        return f'Error: "{absolute_path}" is not a directory'
    
    try:
        all_items = os.listdir(absolute_path)
        item_list = []
        for item in all_items:
            item_size = os.path.getsize(os.path.join(absolute_path, item))
            item_dir = os.path.isdir(os.path.join(absolute_path, item))
            formatted_item = f'- {item}: file_size={item_size} bytes, is_dir={item_dir}'
            item_list.append(formatted_item)
        formatted_string = '\n'.join(item_list)
        return formatted_string
    except Exception as e:
        return f'Error: {e}'