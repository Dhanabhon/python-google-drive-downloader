from __future__ import print_function

import io
import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']

def download_file(real_file_id, filename, client_secret_file_path):
    """Downloads a file
    Args:
        real_file_id: ID of the file to download
    Returns : IO object with location.
    """
    creds = None

    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_info('token.json', SCOPES)
    
    # If there are no (valid) credentials available, let the user log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(client_secret_file_path, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        # create drive api client
        service = build('drive', 'v3', credentials=creds)
        file_id = real_file_id

        # pylint: disable=maybe-no-member
        request = service.files().get_media(fileId=file_id)
        file = io.FileIO(filename, 'wb')

        downloader = MediaIoBaseDownload(file, request)
        done = False
        while done is False:
            status, done = downloader.next_chunk()
            if status:
                print(F'Download {(status.progress() * 100)}%')
        
        print(F'Download Complete!')

    except HttpError as error:
        print(F'An error occurred: {error}')
        file = None

if __name__ == '__main__':
    real_file_id = 'EDIT_HERE'
    filename = 'EDIT_HERE'
    client_secret_file = 'EDIT_HERE'
    download_file(real_file_id=real_file_id, filename=filename, client_secret_file_path=client_secret_file)
