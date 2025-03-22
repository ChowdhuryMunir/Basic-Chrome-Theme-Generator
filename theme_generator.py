import json
import os
import shutil

def create_theme(name, frame_color, toolbar_color, tab_text_color, bg_tab_color, bg_image_path, frame_image_path):
    # Create project folder
    folder_name = name.replace(" ", "_").lower()
    os.makedirs(folder_name, exist_ok=True)
    os.makedirs(os.path.join(folder_name, "images"), exist_ok=True)
    
    # Copy images to the theme folder
    bg_image_dest = os.path.join(folder_name, "images", "background.jpg")
    frame_image_dest = os.path.join(folder_name, "images", "frame.png")
    
    if os.path.exists(bg_image_path):
        shutil.copy(bg_image_path, bg_image_dest)
    if os.path.exists(frame_image_path):
        shutil.copy(frame_image_path, frame_image_dest)
    
    # Define theme JSON structure
    theme_data = {
        "manifest_version": 2,
        "version": "1.0",
        "name": name,
        "theme": {
            "images": {
                "theme_frame": "images/frame.png",
                "theme_ntp_background": "images/background.jpg"
            },
            "colors": {
                "frame": frame_color,
                "toolbar": toolbar_color,
                "tab_text": tab_text_color,
                "background_tab": bg_tab_color
            },
            "properties": {
                "ntp_background_alignment": "center",
                "ntp_background_repeat": "no-repeat",
                "ntp_background_size": "cover"
            }
        }
    }
    
    # Write JSON file
    manifest_path = os.path.join(folder_name, "manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(theme_data, f, indent=4)
    
    print(f"Chrome theme generated in {folder_name} folder.")

# Example usage
if __name__ == "__main__":
    theme_name = input("Enter theme name: ")
    frame = [int(x) for x in input("Enter frame color (R,G,B): ").split(",")]
    toolbar = [int(x) for x in input("Enter toolbar color (R,G,B): ").split(",")]
    tab_text = [int(x) for x in input("Enter tab text color (R,G,B): ").split(",")]
    bg_tab = [int(x) for x in input("Enter background tab color (R,G,B): ").split(",")]
    bg_image = input("Enter path to background image: ")
    frame_image = input("Enter path to frame image: ")
    create_theme(theme_name, frame, toolbar, tab_text, bg_tab, bg_image, frame_image)
