from instaapi import InstaAPI
import config

def main():
    zip_file_path = config.ZIP_FILE_PATH
    insta_api = InstaAPI(zip_file_path)
    insta_api.run()

if __name__ == "__main__":
    main()