import subprocess

def is_package_installed(package_name):
    try:
        result = subprocess.run(["adb", "shell", "pm", "list", "packages", package_name], capture_output=True, text=True, check=True)
        return package_name in result.stdout

    except subprocess.CalledProcessError as e:
        print(f"Error executing adb command: {e}")
        return False

def uninstall_package(package_name):
    if is_package_installed(package_name):
        try:
            subprocess.run(["adb", "shell", "pm", "uninstall", "-k", "--user", "0", package_name], check=True)
            print(f"Package {package_name} has been uninstalled successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing adb command: {e}")
    else:
        print("Package not installed")

def install_package(package_name):
    if not is_package_installed(package_name):
        try:
            subprocess.run(["adb", "shell", "pm", "install-existing", package_name], check=True)
            print(f"Package {package_name} has been installed successfully.")
        except subprocess.CalledProcessError as e:
            print(f"Error executing adb command: {e}")
    else:
        print("Package already installed")

if __name__ == "__main__":
    is_package_installed()
    install_package()
    uninstall_package()