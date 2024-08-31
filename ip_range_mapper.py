import ipaddress
import csv
# clear the screen
import os
os.system('cls' if os.name == 'nt' else 'clear')

def generate_ips_csv(cidr_list, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["range", "ip"])
        
        for cidr in cidr_list:
            network = ipaddress.IPv4Network(cidr.strip())
            for ip in network.hosts():
                csv_writer.writerow([cidr.strip(), str(ip)])

def main():
    input_file = input("Enter the name of the CSV file containing the CIDR ranges (including .csv extension): ")
    
    try:
        with open(input_file, 'r') as file:
            csv_reader = csv.DictReader(file)
            cidr_list = [row['cidr'] for row in csv_reader if row['cidr']]
    except FileNotFoundError:
        print(f"File {input_file} not found. Please check the file name and try again.")
        return
    except KeyError:
        print(f"The CSV file is missing the 'cidr' column or is not formatted correctly.")
        return

    output_file = input("Enter the name of the output file (without .csv extension): ") + ".csv"
    generate_ips_csv(cidr_list, output_file)
    print(f"IP addresses have been successfully written to {output_file}")

if __name__ == "__main__":
    main()
