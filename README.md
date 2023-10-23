# linkedin-sales-navigator-scrapper

This documentation will guide you through the steps to use the provided **Linkedin Sales Navigator Scrapper** in this repository to gather information from **LinkedIn Sales Navigator Leads and Account**.

## Prerequisites
* Python 3.8+ or higher
* Mozilla Firefox installed on your system
* LinkedIn Premium Account

## Instructions
Follow the steps below to use the provided script:

## Step 1: Clone or Download the Repository
You can clone the repository using the following command or download it as a ZIP file and unzip it to your desired location.

```
git clone https://github.com/amitkaushik2710/linkedin-sales-navigator-scrapper.git
```

## Step 2: Create a Mozilla Profile
To use Mozilla Firefox for scraping LinkedIn, you need to create a dedicated Mozilla Firefox profile. Follow these steps to create one:

1. Open Mozilla Firefox.
2. Type about:profiles in the address bar and press Enter.
3. Click on "Create a New Profile."
4. Follow the on-screen instructions to create a new profile and give it a name. Remember the path to this profile, as you will need it in the command.

## Step 3: Search for the keyword in Linkedin Sales Navigator
Search for the keyword in Linkedin Sales Navigator, and copy the LinkedIn lead URL and account URL you want to scrape.

## Step 4: Open Command Prompt
Open the Command Prompt or terminal on your system.

## Step 5: Run the Script
Navigate to the repository directory in the Command Prompt using the cd command:
```
cd /path/to/repo
```
Replace /path/to/repo with the actual path to the repository directory.

Now, run the Python script using the following command:
```
python main.py --profile_path "<mozilla profile path>" --lead_path "<linkedin lead url>" --account_path "<linkedin account url>"
```
Replace the placeholders with the actual paths and URLs. For example:
```
python main.py --profile_path "C:\Users\YourUsername\AppData\Roaming\Mozilla\Firefox\Profiles\your-profile" --lead_path "https://www.linkedin.com/in/username" --account_path "https://www.linkedin.com/in/username"
```

The script will scrape the desired LinkedIn Lead and Account information and save it in a csv file (lead.csv), (account.csv).


