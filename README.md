# Phishing Email Scanner

Phishing Email Scanner is a Python application that allows users to fetch emails from their Gmail account, scan them for phishing URLs using the VirusTotal API, and store insecure emails in a SQLite database for further analysis.

## Features

- **Email Fetching**: Fetch emails from Gmail using the IMAP protocol.
- **Phishing URL Detection**: Scan emails for phishing URLs using the VirusTotal API.
- **Database Storage**: Store insecure emails in a SQLite database for future reference.
- **User-Friendly Interface**: GUI built with Tkinter for ease of use.

## Prerequisites

Before using Phishing Email Scanner, ensure you have the following installed:

- Python 3.x
- Tkinter (`tkinter` package)
- `tkcalendar` package
- `imaplib` package
- `email` package
- `bs4` (BeautifulSoup) package
- `quopri` package
- `virustotal_python` package
- `sqlite3` package

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/phishing-email-scanner.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:

    ```bash
    python main.py
    ```
**(Note: Enter your Gmail credentials)**
   - Ensure that two-factor authentication is disabled for your Gmail account, as the application currently does not support it.
   - If you have two-factor authentication enabled, you can create an "App Password" to use instead:
     1. Go to your Google Account settings.
     2. Under "Security," select "App passwords."
     3. Generate an App Password for the application.
     4. Use this App Password instead of your regular Gmail password in the application.
        
## Contributing

Contributions are welcome! If you find any bugs or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Credit
**VirusTotal API Attribution:**

This project utilizes the VirusTotal API for scanning URLs in Email. For more information about the VirusTotal API and its terms of use, please visit [VirusTotal](https://www.virustotal.com/).

