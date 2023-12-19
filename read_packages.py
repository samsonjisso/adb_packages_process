from subprocess_tasks import install_package, uninstall_package

def read_file(file_path, option):
    try:
        with open(file_path, 'r') as file:
            for line in file:
                if option == 'in':
                    install_package(line.strip())
                else:
                    uninstall_package(line.strip())

    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    read_file()

