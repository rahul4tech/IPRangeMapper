
# IPRangeMapper

IPRangeMapper is a Python script designed to generate a list of IP addresses from a given range of CIDR notations provided in a CSV file. The resulting IP addresses are saved to a new CSV file, where each row contains the CIDR range and the corresponding IP address.

## Features

- Supports input of multiple CIDR ranges from a CSV file.
- Generates all IP addresses within the specified ranges.
- Outputs the results in a new CSV file with two columns: `range` and `ip`.
- User-friendly prompts for specifying input and output files.

## Prerequisites

- Python 3.8 or higher.

## Installation

1. **Clone the repository** (or download the script):

   ```bash
   git clone https://github.com/rahul4tech/IPRangeMapper.git
   cd IPRangeMapper
   ```

2. **Install the required packages** (if necessary):

   Although the script only uses Python's standard library, you can still create a virtual environment and install dependencies:

   ```bash
    pip install -r requirements.txt
   ```

   No external packages are required.

## How to Run

1. **Prepare your CIDR Ranges CSV file**:

   - Create a CSV file (e.g., `cidr.csv`) with a single column named `cidr`, listing each CIDR range on a new line.

   Example:

   ```csv
   cidr
   192.168.1.0/24
   10.0.0.0/31
   172.16.0.0/16
   ```

2. **Run the script**:

   ```bash
   python ip_range_mapper.py
   ```

3. **Follow the prompts**:

   - Enter the name of the CSV file containing the CIDR ranges (including `.csv` extension), e.g., `cidr.csv`.
   - Enter the desired name for the output file (without the `.csv` extension), e.g., `output_ips`.

4. **Check the output**:

   The script will generate a new CSV file with the specified name, containing all the IP addresses within the provided ranges.

   Example output:

   ```csv
   range,ip
   192.168.1.0/24,192.168.1.1
   192.168.1.0/24,192.168.1.2
   192.168.1.0/24,192.168.1.3
   10.0.0.0/31,10.0.0.1
   ```

## Example

Given the following `cidr.csv` file:

```csv
cidr
192.168.1.0/30
10.0.0.0/31
```

Running the script and specifying `output_ips` as the output file name would generate `output_ips.csv`:

```csv
range,ip
192.168.1.0/30,192.168.1.1
192.168.1.0/30,192.168.1.2
192.168.1.0/30,192.168.1.3
10.0.0.0/31,10.0.0.1
```

## CSV File Format

The input CSV file should be formatted as follows:

- The CSV file should have a single column with the header `cidr`.
- Each row under the `cidr` header should contain a valid CIDR notation representing an IP range.

Example `cidr.csv`:

```csv
cidr
192.168.1.0/24
10.0.0.0/31
172.16.0.0/16
```

## Contributing

Feel free to fork this repository, make enhancements, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
