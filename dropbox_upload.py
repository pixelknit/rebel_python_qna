#pip install dropbox
import dropbox
from dropbox.files import WriteMode

# Replace with your Dropbox access token
ACCESS_TOKEN = 'your_access_token_goes_here'

# Replace with the path to the local file you want to upload
local_file_path = r'C:\Users\felip\Documents\test_to_upload.txt'

# Replace with the path where you want to store the file on Dropbox
dropbox_file_path = '/test/file.txt'

# Initialize Dropbox client
dbx = dropbox.Dropbox(ACCESS_TOKEN)

# Upload file
with open(local_file_path, 'rb') as file:
    dbx.files_upload(file.read(), dropbox_file_path, mode=WriteMode('overwrite'))

print(f"File uploaded to Dropbox: {dropbox_file_path}")

