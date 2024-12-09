import zipfile
import os
import json
import shutil

class InstaAPI:
    def __init__(self, zip_file_path, extract_to_path='data/'):
        self.zip_file_path = zip_file_path
        self.target_directory = 'connections/'
        self.not_following_me_back_file = 'not_following_me.txt'
        self.i_dont_follow_them_back_file = 'not_following_byme.txt'
        self.json_files_list_file = 'json_files_list.txt'
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

        with open(self.json_files_list_file, 'w') as file_list_output:
            file_list_output.write("List of JSON files in the 'connections' folder:\n\n")
            for idx, file_name in enumerate(json_files, start=1):
                file_list_output.write(f"{idx}. {file_name}\n")

        print(f"List of JSON files saved to {self.json_files_list_file}")

    def process_json_files(self):
        for json_file in ['followers_1.json', 'following.json']:
            json_file_path = os.path.join(self.extract_to_path, json_file)
            if os.path.exists(json_file_path):
                print(f"Processing {json_file}...")
                with open(json_file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    print(f"Data loaded from {json_file}: {len(data)} entries")
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

        print("Followers count:", len(self.followers))
        print("Following count:", len(self.following))

    def find_and_save_results(self):
        not_following_me_back = self.following - self.followers
        i_dont_follow_them_back = self.followers - self.following

        with open(self.not_following_me_back_file, 'w') as output_file:
            output_file.write("Users who don't follow me back:\n\n")
            for idx, user in enumerate(sorted(not_following_me_back), start=1):
                output_file.write(f"{idx}. {user}\n")

        print(f"Results saved to {self.not_following_me_back_file}")

        with open(self.i_dont_follow_them_back_file, 'w') as output_file:
            output_file.write("Users who I don't follow back:\n\n")
            for idx, user in enumerate(sorted(i_dont_follow_them_back), start=1):
                output_file.write(f"{idx}. {user}\n")

        print(f"Results saved to {self.i_dont_follow_them_back_file}")

    def getUnfollowers(self):
        self.extract_json_files()
        self.process_json_files()
        self.find_and_save_results()