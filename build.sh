echo Building Binary

# Config
BINARY_DIR="$HOME/Documents/GitHub/RC-Controller/.venv/bin"
BUILD_DIR="/build"
DIST_DIR="/dist"
OUTPUT_ZIP="output.zip"
BYPASS=true #Bypass Checks

# Build
$BINARY_DIR/python -m pip install -U pyinstaller
$BINARY_DIR/pyinstaller src/main.py

# Checks
if [ "$BYPASS" = false]; then
    if [ &? -ne 0 ]; then
        echo Failed to Build
        exit 1
    fi

    if [ ! -d "$BUILD_DIR"]; then
        echo "$BUILD_DIR does not exist"
        exit 1
    fi

    if [ ! -d "$DIST_DIR" ]; then
        echo "$DIST_DIR does not exist"
        exit 1
    fi
fi

# Zip the output
zip -r "$OUTPUT_ZIP" . -i "$BUILD_DIR" "$DIST_DIR"

# Check
if [ "$BYPASS" = false]; then
    if [ $? -eq 0 ]; then
        echo "Build $OUTPUT_ZIP"
    else
        echo "Failed to create $OUTPUT_ZIP"
        exit 1
    fi
fi