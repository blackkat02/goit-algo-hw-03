from pathlib import Path
import shutil


def copy_file_of_directory(path_in: str, path_out="dist"):
    """
    Recursively copies files from the input directory to the output directory,
    organizing files into directories based on file extensions.

    Args:
        path_in (str): The path to the source directory.
        path_out (str): The path to the destination directory (default: 'dist').
    """

    dir_path_in = Path(path_in)
    dir_path_out = Path(path_out)

    if not dir_path_in.exists():
        print(f"Error: Directory '{dir_path_in}' does not exist.")
        return

    if not dir_path_in.is_dir():
        print(f"Error: '{dir_path_in}' is not a directory.")
        return

    if not dir_path_out.is_dir():
        dir_path_out.mkdir(parents=True, exist_ok=True)
        print(f"Directory '{dir_path_out}' created successfully.")

    for item in dir_path_in.iterdir():
        if item.is_dir():
            copy_file_of_directory(item, path_out=dir_path_out)
        elif item.is_file():
            file_parts = item.name.split(".")
            if len(file_parts) > 1:
                extension = file_parts[1]
            else:
                extension = "no_extension"  # Для файлів без розширень

            dir_path_out_type = dir_path_out / extension

            if not dir_path_out_type.exists():
                dir_path_out_type.mkdir(parents=True, exist_ok=True)
            path_of_copy_file = shutil.copy(item, dir_path_out_type)
            print(f"File '{item.name}' copied to '{path_of_copy_file}'")


copy_file_of_directory(
    r"C:\Users\Admin\PycharmProjects\goit-algo-hw-03\dir_in",
    r"C:\Users\Admin\PycharmProjects\goit-algo-hw-03\new_dir1"
)

copy_file_of_directory(
    r"C:\Users\Admin\PycharmProjects\goit-algo-hw-03\dir_in",
)