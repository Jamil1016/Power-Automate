# Power Automate Training

## Overview

This training provides a comprehensive introduction to Microsoft Power Automate, a cloud-based service that enables users to create automated workflows between apps and services. Participants will learn how to streamline repetitive tasks, integrate data across Microsoft 365 and other platforms, and improve productivity through automation. The course covers key concepts, practical examples, and hands-on exercises to help users design, build, and manage flows efficiently regardless of technical background. By the end of the training, attendees will be equipped to automate business processes, reduce manual effort, and drive digital transformation.

## Requirements

* **Power Automate**  
  The primary platform for building, managing, and running automated workflows.

* **On-premises gateway**  
  Enables secure data transfer between on-premises data sources (such as SQL Server or file shares) and Power Automate in the cloud.

* **Chat-GPT / Copilot**  
  Used for integrating AI-powered conversational experiences or automating responses within flows.

* **Microsoft 365 Apps**  
  Essential for demonstrating automation scenarios across the Microsoft ecosystem:
    * **Excel** – Automate data processing, reporting, and integration tasks.
    * **Power BI** – Trigger data refreshes and automate report distribution.
    * **Outlook** – Automate email notifications, calendar events, and task management.

* **SharePoint**  
  Used for automating document management, approvals, and collaboration workflows.

* **A sample data source (e.g., SQL Server, SharePoint List, or Excel file)**  
  Provides real-world data for hands-on exercises and flow demonstrations.

* **A Microsoft account with appropriate permissions**  
  Required to access Power Automate, Microsoft 365 apps, and other


## Preparation

Before starting the training, please complete the following steps to ensure a smooth experience:

* **Power Automate**  
  Access Power Automate via your web browser at [https://flow.microsoft.com](https://flow.microsoft.com). Sign in with your Microsoft account. No installation is required for the cloud service.

* **On-premises Data Gateway**  
  If you plan to connect Power Automate to on-premises data sources (such as SQL Server or local file shares), download and install the On-premises Data Gateway from [Microsoft’s official site](https://aka.ms/onpremgateway). Follow the installation wizard and sign in with your organizational account to register the gateway.

* **Sample Files**  
  Download the required sample files for hands-on exercises from [this link](https://pragmaticworks.com/power-automate-beginner-to-pro-student-files?utm_campaign=lwtn-power-automate-beginner-to-pro&utm_source=youtube&utm_medium=organic). These files include sample Excel sheets, SharePoint lists, and other data sources used during the training.

Make sure you have the required permissions to install software and access the necessary data sources before the training begins.

---

## Power Automate Cheatsheet

| Action                | Description                                      |
|-----------------------|--------------------------------------------------|
| **Create a Flow**     | Click "Create" > Choose flow type                |
| **Add a Trigger**     | Select an event that starts your flow            |
| **Add an Action**     | Choose what happens after the trigger            |
| **Test a Flow**       | Click "Test" to run and debug your flow          |
| **View Run History**  | Check flow runs and troubleshoot errors          |
| **Connectors**        | Integrate with 3rd-party or Microsoft services   |
| **Dynamic Content**   | Use data from previous steps in your flow        |
| **Conditions**        | Add logic to control flow execution              |
| **Loops**             | Repeat actions for each item in a list           |
| **Approvals**         | Automate approval processes                      |

For more tips, visit the [Official Power Automate documentation](https://learn.microsoft.com/power-automate/)

[View Cheatsheet (PDF)](./Pragmatic%20Works%20Power%20Automate%20Cheat%20%20Sheet.pdf)


# Activity 1: Power Automate Cloud - Send Email for Device Request with Approval

## Description
This Power Automate flow automates the approval process for newly created items in a SharePoint list. It checks if the item value is greater than 200 and routes it through a manager approval process, sending appropriate notifications based on the decision.

---

## Workflow Steps
1. **Trigger:**
   - Flow starts **when a new item is created** in the SharePoint list.

2. **Initial Notification:**
   - Sends an email notification confirming that a new item has been created.

3. **Condition – Check if Value > 200:**
   - If **Yes (True)**:
     - Retrieves the manager of the requester.
     - Sends the manager an approval request email with options.
     - **Manager Selection Condition:**
       - If **Approved**:
         - Updates the item status to “Approved” in SharePoint.
         - Sends a notification email to the requester confirming approval.
       - If **Rejected**:
         - Updates the item status to “Rejected” in SharePoint.
         - Sends a rejection notification to the requester.
   - If **No (False)**:
     - Sends an email notification stating the value is less than 200, bypassing approval.

---

## Flow chart

![alt text](./Youtube%20-%20Pragmatic%20Works/Activities/1_New_Device_Reuqest_with_Approval/PowerAutomate_RequestNewDevice.png)
---
## Purpose
This automation reduces manual approval work by:
- Automatically detecting high-value items (> 200).
- Routing them to the right manager for review.
- Updating the SharePoint list status based on the decision.
- Sending timely notifications to both managers and requesters.

# Activity 2: Power Automate Cloud - Weekly Device Request List Email

## Description
This Power Automate flow sends a weekly email containing a list of all device requests retrieved from a SharePoint list. It is scheduled to run automatically based on a set recurrence and formats the data into an HTML table for easy viewing in the email.

---

## Workflow Steps
1. **Trigger – Recurrence:**
   - The flow runs on a scheduled recurrence (weekly).

2. **Get Items from SharePoint:**
   - Retrieves all items from the SharePoint list containing device requests.

3. **Create HTML Table:**
   - Converts the retrieved SharePoint list data into an HTML table format.

   ```html
    <style>
    table {
      border: 1px solid #1C6EA4;
      background-color: #EEEEEE;
      width: 75%;
      text-align: center;
      border-collapse: collapse;
    }
    table td, table th {
      border: 1px solid #AAAAAA;
      padding: 3px 2px;
    }
    table tbody td {
      font-size: 13px;
    }
    table thead {
      background: #1C6EA4;
      border-bottom: 2px solid #444444;
    }
    table thead th {
      font-size: 15px;
      font-weight: bold;
      color: #FFFFFF;
      border-left: 2px solid #D0E4F5;
    }
    table thead th:first-child {
      border-left: none;
    }
    </style>
   ```

4. **Compose:**
   - Prepares the HTML table data for embedding into the email body.

5. **Send an Email (V2):**
   - Sends an email to the target recipients with the HTML table included, displaying all device requests for the week.

---
## Flow chart
![2_Sending_email_List_of_Request_Device_20250808073412](./Youtube%20-%20Pragmatic%20Works/Activities/2_Sending_email_List_of_Request_Device/Screenshot%202025-08-08%20153226.png)

---
## Purpose
This automation streamlines reporting by:
- Automatically pulling the latest device request data every week.
- Formatting the data into a clear HTML table.
- Sending it directly to stakeholders via email without manual intervention.
 ---

# Activity 3: Power Automate Cloud - Auto-Save Device Request Excel from Email to SharePoint

## Description
This Power Automate flow automatically saves a specific Excel file from incoming emails into a SharePoint document library. It triggers when an email with a specific subject arrives, checks for an Excel attachment, saves it to SharePoint with a timestamped file name, and sends a confirmation email upon success.


## Workflow Steps

### 1. Trigger — When a new email arrives (V3)
- **Folder:** Inbox
- **Include Attachments:** Yes
- **Only with Attachments:** Yes
- **Subject Filter:** `Device Request`

### 2. Condition — Subject Contains Keyword
- Checks if the email subject contains `Device Request`.

### 3. Process Attachments
- **Apply to each:** Loops through all attachments.
- Condition: Proceeds only if the file name ends with `.xlsx`.

### 4. Add Timestamp to File Name
- **Compose step** with the following expression:
  ```html
  concat(formatDateTime(utcNow(),'yyyy-MM-dd_HHmmss'), '_', items('Apply_to_each')?['Name'])
  ````
- This ensures each saved file name is unique, e.g., `2025-08-09_142300_Device_Request.xlsx`.

### 5. Create File in SharePoint
- **Site Address:** Your SharePoint site URL
- **Folder Path:** Destination document library folder
- **File Name:** Output of the Compose step above
- **File Content:** `ContentBytes` from the attachment

### 6. Send Confirmation Email
- Sends an email notification to confirm the file was saved successfully.
- **To:** Your email
- **Subject:** `Device Request Excel saved to SharePoint`
- **Body:**
  ```html
  The following file was saved to SharePoint:<br>
  <strong>@{outputs('Compose')}</strong>
  ```
---
# Flow chart
![Save_Specific_Email_Attachment_to_Sharepoint](./Youtube%20-%20Pragmatic%20Works/Activities/3_Save_Specific_Email_Attachment_to_SharePoint/Save_Specific_Email_Attachment_to_Sharepoint.png)

## Purpose
- Detects incoming emails containing device request Excel files.
- Saves them to SharePoint with a timestamp to avoid overwriting.
- Sends a confirmation email to ensure you are notified of the action.

