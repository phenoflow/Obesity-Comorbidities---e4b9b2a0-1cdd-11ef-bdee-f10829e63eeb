# Romi Haas, Ljoudmila Busija, Alexandra Gorelik, Denise A O'Connor, Christopher Pierce, Danielle Mazza, Rochelle Buchbinder, 2024.

import sys, csv, re

codes = [{"code":"27113001","system":"snomedct"},{"code":"161833006","system":"snomedct"},{"code":"388976009","system":"snomedct"},{"code":"224994002","system":"snomedct"},{"code":"363808001","system":"snomedct"},{"code":"301336003","system":"snomedct"},{"code":"238131007","system":"snomedct"},{"code":"262286000","system":"snomedct"},{"code":"162863004","system":"snomedct"},{"code":"388975008","system":"snomedct"},{"code":"8943002","system":"snomedct"},{"code":"83421005","system":"snomedct"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('obesity-comorbidities-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["overweight-obesity-comorbidities---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["overweight-obesity-comorbidities---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["overweight-obesity-comorbidities---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
