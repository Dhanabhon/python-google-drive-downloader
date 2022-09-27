# python-google-drive-downloader
Download a large file from Google Drive in Python.

## Usage
## Step 1: Install the Google client library
```shell
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
## Step 2: Edit a little code.
```python
    real_file_id = 'EDIT_HERE'
    filename = 'EDIT_HERE'
    client_secret_file = 'EDIT_HERE'
````
- `real_file_id` is an ID of the file to download. Example: `https://drive.google.com/file/d/1KPQP1C7N3Ka15djrFjo1c2KC68Xwz6v/view` the real file ID is `1KPQP1C7N3Ka15djrFjo1c2KC68Xwz6v`
- `filename` is the path of the file want to save to the local drive. Example: `\User\Apple\Desktop\data.zip`
- `client_secret_file` needs to create and download from OAuth 2.0 Client IDs from (Google Cloud)[https://console.cloud.google.com/]

## Step 3: Run main.py file
```shell
    python main.py
```

## NOTE
The file token.json stores the user's access and refresh tokens, and is created automatically when the authorization flow completes for the first time.