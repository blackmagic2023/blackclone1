import subprocess
import os

def run_nmap(ip):
    try:
        # Change directory to /usr/share/nmap/scripts/
        os.chdir("/usr/share/nmap/scripts/")
        
        # Run nmap with options to detect vulnerabilities without pinging (-Pn) and append the results to a file
        command = f"sudo nmap -script vuln {ip} -Pn >> scan_results.txt"
        subprocess.run(command, shell=True, check=True)
        print("Scan completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e}")
    except Exception as ex:
        print(f"An unexpected error occurred: {ex}")

def main():
    try:
        # Read IP addresses from the online_ips.txt file in the /hollowpoint directory
        file_path = "/hollowpoint/online_ips.txt"
        if not os.path.exists(file_path):
            print(f"Error: {file_path} not found.")
            return
        
        with open(file_path, "r") as file:
            for line in file:
                ip_info = line.strip().split(", ")
                if len(ip_info) >= 2:
                    ip = ip_info[0]
                    print(f"Scanning IP: {ip}")
                    run_nmap(ip)
                else:
                    print(f"Invalid format found in line: {line}")
    except KeyboardInterrupt:
        print("\nScan aborted by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScript terminated by user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
