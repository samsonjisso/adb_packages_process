#!/bin/bash

# Global variable with package names
PACKAGE_LIST=(
    "com.android.chrome"
    "com.android.vending"
    "com.sec.android.app.samsungapps"
    "com.google.android.googlequicksearchbox"
)

# Function to install existing packages
install_existing_packages() {
    for package in "${PACKAGE_LIST[@]}"; do
        echo "Installing existing: $package"
        if adb shell pm install-existing "$package"; then
            echo "Successfully installed existing: $package"
        else
            echo "Failed to install existing: $package (maybe not available or not installed), continuing..."
        fi
    done
}

# Execute the function
install_existing_packages

echo "Installation process completed."

#sed -i 's/\r//' uninstall_script.sh
