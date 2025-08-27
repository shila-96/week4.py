def file_read_write():
    filename = "notes.txt"

    try: 
        with open(filename, "r") as file:
            content = file.read()

        modified_content = content.upper()

        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.write(modified_content)

        print(f"File successfully written to '{new_filename}'")

    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")


if __name__ == "__main__":
    file_read_write()
