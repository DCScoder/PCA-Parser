###################################################################################
#
#    Script:    pca_parser.py
#    Version:   1.0
#    Author:    Dan Saunders
#    Contact:   dcscoder@gmail.com
#    Purpose:   Parse Program Compatibility Assistant (PCA) Log Files
#    Usage:     python pca_parser.py <source_directory>
#    Reference: https://aboutdfir.com/new-windows-11-pro-22h2-evidence-of-execution-artifact/
#
#    This program is free software: you can redistribute it and / or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program. If not, see <https://www.gnu.org/licenses/>.
#
###################################################################################

import sys
import os
import json

__version__ = 'v1.0'
__author__ = 'Dan Saunders'
__email__ = 'dcscoder@gmail.com'

# Arguments
SOURCE = sys.argv[1]
# Source Files
APP_LAUNCH = 'PcaAppLaunchDic.txt'
DB0 = 'PcaGeneralDb0.txt'
DB1 = 'PcaGeneralDb1.txt'
# Keys
LAUNCH_DIC_KEYS = ['file_path', 'runtime']
DB_KEYS = ['runtime', 'run_status', 'file_path', 'description', 'software_vendor', 'file_version', 'program_id', 'exit_code']

# Main
def main():
    print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("pca_parser.py " + __version__ + " Author: " + __author__ + " " + __email__)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    try:
        print('\nProcessing:', APP_LAUNCH)
        with open(os.path.join(SOURCE, APP_LAUNCH), "r") as f:
            records = f.readlines()
            ld_count = len(records)
            print('Records found:', ld_count)
            with open("PCA_App_Launch_Records.json", "w") as JSON:
                for entry in records:
                    record = entry.strip().split("|")
                    final_records = dict(zip(LAUNCH_DIC_KEYS, record))
                    json.dump(final_records, JSON, indent=4)
    except IOError as e:
        print('Operation failed: %s' % e.strerror)

    try:
        print('\nProcessing:', DB0)
        with open(os.path.join(SOURCE, DB0), "r") as f:
            records = f.readlines()
            db_count = len(records)
            print('Records found:', db_count)
            with open("PCA_Database_Records_0.json", "w") as JSON:
                for entry in records:
                    record = entry.strip().split("|")
                    final_records = dict(zip(DB_KEYS, record))
                    json.dump(final_records, JSON, indent=4)
    except IOError as e:
        print('Operation failed: %s' % e.strerror)

    try:
        print('\nProcessing:', DB1)
        with open(os.path.join(SOURCE, DB1), "r") as f:
            records = f.readlines()
            db_count = len(records)
            print('Records found:', db_count)
            with open("PCA_Database_Records_1.json", "w") as JSON:
                for entry in records:
                    record = entry.strip().split("|")
                    final_records = dict(zip(DB_KEYS, record))
                    json.dump(final_records, JSON, indent=4)
    except IOError as e:
        print('Operation failed: %s' % e.strerror)

    print('\nProcessing Completed!')

if __name__ == "__main__":
    main()