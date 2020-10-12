import json
import csv

index_county = 2
index_tiv2011 = 7
index_tiv2012 = 8
counties = dict()


def get_sum(arr):
    sum_of_arr = 0
    for val in arr:
        sum_of_arr += val
    return sum_of_arr


def get_avg(arr):
    result = get_sum(arr)
    return result / len(arr)


def get_data(county, field, value):
    if county in counties:
        if field not in counties[county].keys():
            counties[county][field] = []
        counties[county][field].append(float(value))
    else:
        f = dict()
        f[field] = []
        f[field].append(float(value))
        counties[county.replace("COUNTY", "")] = f


tivs = {
    "tiv_2011": [],
    "tiv_2012": []
}

with open("data_insurance.csv", mode="r+", newline='') as read_file:
    reader = csv.reader(read_file)
    header = next(reader)

    for line_csv in reader:
        tivs["tiv_2011"].append(float(line_csv[7]))
        tivs["tiv_2012"].append(float(line_csv[8]))
        get_data(line_csv[index_county], "tiv_2011", line_csv[index_tiv2011])
        get_data(line_csv[index_county], "tiv_2012", line_csv[index_tiv2012])

total_tiv = {
    "2011": get_sum(tivs["tiv_2011"]),
    "2012": get_sum(tivs["tiv_2012"])
}

avg_total_tiv = {
    "2011": get_avg(tivs["tiv_2011"]) / len(tivs["tiv_2011"]),
    "2012": get_avg(tivs["tiv_2012"]) / len(tivs["tiv_2012"])
}
final_result = {
    "total_tiv": total_tiv,
    "avg_total_tiv": avg_total_tiv,
    "counties": []
}

for key, value in counties.items():
    each_county = {
        "name": key,
        "data": {
            "total_tiv": get_sum(tivs['tiv_2011'] + tivs['tiv_2012']),
            "avg_tiv": get_avg(tivs['tiv_2011'] + tivs['tiv_2012']),
            "years": {
                "2011": {
                    "total_tiv": get_sum(tivs['tiv_2011']),
                    "avg_tiv": get_avg(tivs['tiv_2011']),
                },
                "2012": {
                    "total_tiv": get_sum(tivs['tiv_2012']),
                    "avg_tiv": get_avg(tivs['tiv_2012'])
                }
            }
        }
    }
    final_result["counties"].append(each_county)

with open("result.json", "w") as write_file:
    write_file.write(json.dumps(final_result))