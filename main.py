import csv

def bereken_omzet():
    csv_data = []

    # Voer hier de csv file in. Plaats in je working directory
    # als je niet het path wil specificeren.
    with open('naam_csv.csv', mode='r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip the header row
        for row in csv_reader:
            csv_data.append(row)

    activity_dict = dict()
    costs = dict()

    for transaction in csv_data:
        name = get_name(transaction[6])
        if name not in activity_dict:
            activity_dict[name] = 1
            costs[name] = 0
        else:
            activity_dict[name] += 1
        costs[name] += float(transaction[3]) - 0.35

    for activity in costs:
        print(activity + ": " + str(costs[activity]))

    totale_omzet = 0
    for cost in costs.values():
        if cost > 0:
            totale_omzet += cost

    print("--> Totale omzet:", totale_omzet)


def get_name(complete_name: str):
    if len(complete_name.split("-")) == 1:
        return complete_name.split("-")[0]
    return complete_name.split("-")[1]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("--> Dit is de omzet die Mollie heeft ontvangen voor de verschillende activiteiten:\n")
    bereken_omzet()
    print("\n--> Let op, NL omvat de transactiekosten en hoeft niet gesplitst te worden.")
