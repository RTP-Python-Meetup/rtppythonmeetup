import json
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = '1UdksBpMSSnHLzQK1fMikUyuOi4AsEN0vjamkTyElO-E'
HEADER_RANGE = 'Meetings!A1:G1'
DATA_RANGE_NAME = 'Meetings!A2:G'

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    header_result = sheet.values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=HEADER_RANGE
    ).execute()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=DATA_RANGE_NAME).execute()
    header = header_result.get('values', [[]])[0]
    print(header)
    values = result.get('values', [])

    if not values:
        print('No data found.')
    else:
        print(json.dumps([dict(zip(header, row)) for row in values], indent=4))

if __name__ == '__main__':
    main()

