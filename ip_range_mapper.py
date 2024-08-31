import ipaddress
import csv
import concurrent.futures
import os
import time

def generate_ips_for_cidr(cidr):
    network = ipaddress.IPv4Network(cidr.strip())
    return [(cidr.strip(), str(ip)) for ip in network.hosts()]

def process_cidrs_in_parallel(cidr_list, output_file, max_workers=None):
    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        with open(output_file, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(["range", "ip"])
            
            for result in executor.map(generate_ips_for_cidr, cidr_list):
                csv_writer.writerows(result)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
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

    start_time = time.time()
    process_cidrs_in_parallel(cidr_list, output_file, max_workers=os.cpu_count())
    end_time = time.time()

    print(f"IP addresses have been successfully written to {output_file}")
    print(f"Processing completed in {end_time - start_time:.2f} seconds.")

if __name__ == "__main__":
    main()
