import requests
import json

# Define the Power BI API endpoint and the report ID
power_bi_api_url = "https://api.powerbi.com/v1.0/myorg/reports/{report_id}/refresh"
report_id = "your_report_id_here"  # Replace with your actual report ID

# Define the authentication token (you need to obtain this token)
access_token = "your_access_token_here"  # Replace with your actual access token

def refresh_powerbi_report():
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    # Make the API call to refresh the report
    response = requests.post(power_bi_api_url.format(report_id=report_id), headers=headers)

    if response.status_code == 202:
        print("Refresh initiated successfully.")
    else:
        print(f"Failed to initiate refresh: {response.status_code} - {response.text}")

if __name__ == "__main__":
    refresh_powerbi_report()