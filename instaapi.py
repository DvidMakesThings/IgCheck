import zipfile
import os
import json
import shutil

class InstaAPI:
    def __init__(self, zip_file_path, extract_to_path='data/'):
        self.zip_file_path = zip_file_path
        self.target_directory = 'connections/'
        self.extract_to_path = extract_to_path
        self.followers = set()
        self.following = set()

    def extract_json_files(self):
        json_files = []
        with zipfile.ZipFile(self.zip_file_path, 'r') as zip_ref:
            for file_info in zip_ref.infolist():
                if file_info.filename.startswith(self.target_directory) and file_info.filename.endswith('.json'):
                    json_files.append(file_info.filename)
                    extracted_file_path = os.path.join(self.extract_to_path, os.path.basename(file_info.filename))
                    if not os.path.exists(extracted_file_path):
                        with zip_ref.open(file_info.filename) as source, open(extracted_file_path, 'wb') as target:
                            shutil.copyfileobj(source, target)
        return json_files

    def process_json_files(self):
        for json_file in ['followers_1.json', 'following.json']:
            json_file_path = os.path.join(self.extract_to_path, json_file)
            if os.path.exists(json_file_path):
                with open(json_file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    if json_file == 'followers_1.json':
                        try:
                            for item in data:
                                if isinstance(item, dict) and 'string_list_data' in item:
                                    for entry in item['string_list_data']:
                                        if 'value' in entry:
                                            self.followers.add(entry['value'])
                        except Exception as e:
                            print(f"Error processing {json_file}: {e}")
                    elif json_file == 'following.json':
                        try:
                            for item in data.get("relationships_following", []):
                                if isinstance(item, dict) and 'string_list_data' in item:
                                    for entry in item['string_list_data']:
                                        if 'value' in entry:
                                            self.following.add(entry['value'])
                        except Exception as e:
                            print(f"Error processing {json_file}: {e}")

    def get_unfollowers(self):
        not_following_me_back = self.following - self.followers
        i_dont_follow_them_back = self.followers - self.following
        return not_following_me_back, i_dont_follow_them_back

    def run(self):
        self.extract_json_files()
        self.process_json_files()
        return self.get_unfollowers()