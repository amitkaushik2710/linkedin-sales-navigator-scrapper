import csv

def write_to_csv_lead(user_info_list):
    # Define the CSV fieldnames (column headers)
    fieldnames = ['Name', 'Profile Link', 'Designation', 'Company', 'Company Link', 'Location', 'Time in Company and Role', 'About']

    # Write the data to the CSV file in append mode ('a')
    with open("lead.csv", 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, and if so, write the header row
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write user information for each user
        for user_info in user_info_list:
            writer.writerow(user_info)

def write_to_csv_account(company_info_list):
    # Define the CSV fieldnames (column headers)
    fieldnames = ['Image URL', 'URL', 'Name', 'Industry', 'About']

    # Write the data to the CSV file in append mode ('a')
    with open("account.csv", 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        # Check if the file is empty, and if so, write the header row
        if csvfile.tell() == 0:
            writer.writeheader()

        # Write user information for each user
        for company_info in company_info_list:
            writer.writerow(company_info)
