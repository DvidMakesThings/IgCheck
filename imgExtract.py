import zipfile
import os
import shutil

class MediaExtractor:
    def __init__(self, zip_file_path, img_folder_path='img/'):
        self.zip_file_path = zip_file_path
        self.media_folder = 'media/'
        self.subfolders = ['stories', 'posts', 'other']
        self.img_folder_path = img_folder_path
        self.valid_extensions = {'.jpg', '.jpeg', '.png', '.mp4', '.mov', '.gif'}

        # Create img folder if it doesn't exist
        if not os.path.exists(self.img_folder_path):
            os.makedirs(self.img_folder_path)

    def extract_and_rename_media(self):
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            for subfolder in self.subfolders:
                subfolder_path = os.path.join(self.media_folder, subfolder)
                media_files = []

                for file_info in zip_ref.infolist():
                    if file_info.filename.startswith(subfolder_path) and any(file_info.filename.endswith(ext) for ext in self.valid_extensions):
                        timestamp = None
                        try:
                            timestamp = int(file_info.filename.split('/')[-1].split('_')[0])
                        except (ValueError, IndexError):
                            timestamp = file_info.date_time[3]

                        media_files.append((file_info, timestamp))

                media_files.sort(key=lambda x: x[1])
                target_folder = os.path.join(self.img_folder_path, subfolder)
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                for idx, (file_info, timestamp) in enumerate(media_files):
                    extension = os.path.splitext(file_info.filename)[1]
                    new_filename = f"{subfolder}_{idx+1}{extension}"
                    extracted_file_path = os.path.join(target_folder, new_filename)
                    if not os.path.exists(extracted_file_path):
                        with zip_ref.open(file_info.filename) as source, open(extracted_file_path, 'wb') as target:
                            shutil.copyfileobj(source, target)
                        print(f"Extracted {file_info.filename} to {extracted_file_path}")

        print(f"All media files have been extracted and renamed chronologically to {self.img_folder_path}")

# Example usage:
# extractor = MediaExtractor('data/instagram-beefyburger91-2024-11-24-ohlvyaSX.zip')
# extractor.extract_and_rename_media()
