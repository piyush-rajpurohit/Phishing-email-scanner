import re
import sys
import virustotal_python
from base64 import urlsafe_b64encode
from pprint import pprint

def extract_urls_from_text(text):
    # Modified regex to capture URLs with only allowed characters
    return re.findall(r'https?://[\w./:-]+', text)

def scan_urls_with_virustotal(urls, api_key):
    for url in urls:
        with virustotal_python.Virustotal(api_key, API_VERSION=3, TIMEOUT=10.0) as vtotal:
            try:
                resp = vtotal.request("urls", data={"url": url}, method="POST")
                # Safe encode URL in base64 format
                url_id = urlsafe_b64encode(url.encode()).decode().strip("=")
                report = vtotal.request(f"urls/{url_id}")
                
                # Accessing scan results
                if 'attributes' in report.data and 'last_analysis_stats' in report.data['attributes']:
                    scan_results = report.data['attributes']['last_analysis_stats']
                    pprint("Scan Results:")
                    pprint(scan_results)

                    # Check if there are malicious or suspicious detections
                    if scan_results.get('malicious', 0) > 0:
                        print(f"The URL {url} is a phishing")
                    else:
                        print(f"The URL {url} is not a phishing")

            except virustotal_python.VirustotalError as err:
                print(f"Failed to send URL: {url} for analysis and get the report: {err}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python phishing_scanner.py <sender> <subject> <body>")
        sys.exit(1)

    sender = sys.argv[1]
    subject = sys.argv[2]
    body = sys.argv[3]

    try:
        # Extract URLs from email text
        email_text = f"{subject} {body}"
        urls = extract_urls_from_text(email_text)

        # If no URLs found, return "Nothing to scan"
        if not urls:
            print("No URLs found in the email.")
            sys.exit(0)

        # Remove duplicate URLs
        unique_urls = list(set(urls))

        # Debugging: Print unique URLs for debugging
        #print("Unique URLs:", unique_urls)

        # Scan URLs using VirusTotal
        VirusTotal_API_Key = "215118761695b8e59f718a5296aaa3340066c595b123b73102b93454ac88e89c"
        scan_urls_with_virustotal(unique_urls, VirusTotal_API_Key)

    except Exception as e:
        print(f"An error occurred: {e}")