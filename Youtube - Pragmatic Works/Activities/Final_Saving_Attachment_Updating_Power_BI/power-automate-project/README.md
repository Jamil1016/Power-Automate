# Power Automate Project

## Overview

This project demonstrates how to automate the process of retrieving an Excel file attachment from an email, saving it to OneDrive, refreshing a Power BI report using a Python script, and republishing the updated report to the Power BI service. The automation is achieved using Microsoft Power Automate and Power Automate Desktop, along with a Python script for interacting with the Power BI API.

## Purpose

The main objectives of this project are to:

- Streamline the process of handling Excel file attachments from emails.
- Automate the refresh of Power BI reports based on the latest data.
- Ensure that stakeholders always have access to the most up-to-date reports without manual intervention.

## Project Structure

The project is organized into the following directories and files:

- **src/**: Contains the source files for flows, guides, and scripts.
  - **flows/**: Contains markdown files that provide detailed discussions and guides for creating Power Automate flows.
    - `retrieve_excel_and_refresh_powerbi.md`: A step-by-step guide for creating the flow to retrieve the Excel file and refresh the Power BI report.
  - **guides/**: Contains additional guidance on automating the Power BI refresh process.
    - `powerbi_refresh_automation.md`: Best practices and troubleshooting tips for using Power Automate and Power BI together.
  - **scripts/**: Contains the Python script responsible for refreshing the Power BI report.
    - `refresh_powerbi.py`: The script that connects to the Power BI API and triggers the report refresh.
- **assets/**: Contains sample files used for testing the flow.
  - `sample-email.xlsx`: A sample Excel file that simulates the type of attachment the flow will process.
- `README.md`: This file provides an overview of the project.
- `.gitignore`: Specifies files and directories to be ignored by version control.

## Setup Instructions

1. **Prerequisites**:
   - Ensure you have access to Microsoft Power Automate and Power Automate Desktop.
   - Install Python and the necessary libraries for interacting with the Power BI API.

2. **Clone the Repository**:
   - Clone this repository to your local machine using Git.

3. **Configure Power Automate Flow**:
   - Follow the instructions in `src/flows/retrieve_excel_and_refresh_powerbi.md` to set up the Power Automate flow.

4. **Run the Python Script**:
   - Ensure that the `refresh_powerbi.py` script is configured with the correct Power BI API credentials.

5. **Testing**:
   - Use the `assets/sample-email.xlsx` file to test the flow and ensure that the automation works as expected.

## Usage

Once the setup is complete, the Power Automate flow will automatically trigger based on the defined conditions (e.g., receiving an email with an Excel attachment). The flow will save the attachment to OneDrive, run the Python script to refresh the Power BI report, and republish the updated report to the Power BI service.

## Contribution

Contributions to enhance the functionality or improve the documentation of this project are welcome. Please submit a pull request or open an issue for discussion.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.