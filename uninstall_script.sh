#!/bin/bash

# Global variable with package names
PACKAGE_LIST=(
    "com.android.chrome"
    "com.google.android.youtube"
    "com.android.vending"
    "com.sec.android.app.samsungapps"
    "com.facebook.katana"
    "org.mozilla.firefox"
    "com.zhiliaoapp.musically"
    "com.google.android.googlequicksearchbox"
    "org.freedownloadmanager.fdm"
    "org.freedownloadmanager.fdm.MyActivity"
    "com.microsoft.copilot"
    "com.microsoft.sapphire.app.main.SapphireMainActivity"
    "et.jiji.app"
    "ng.jiji.app.ui.splash.SplashActivity"
    "com.netflix.mediaclient"
    "org.telegram.messenger"
    "com.duckduckgo.mobile.android"
)

# Function to uninstall packages
uninstall_packages() {
    for package in "${PACKAGE_LIST[@]}"; do
        echo "Uninstalling: $package"
        if adb shell pm uninstall -k --user 0 "$package"; then
            echo "Successfully uninstalled: $package"
        else
            echo "Failed to uninstall: $package (maybe not installed), continuing..."
        fi
    done
}

# Execute the function
uninstall_packages

echo "Uninstallation process completed."
