import csv
import os


debug = 1
list1 = []
list_link_files = []

def list_csv_files():
    global list_link_files
    folder = "C:\\Users\\Shadow\\Documents\\src-euromillions\\tirages_euromillions"
    liste_files = os.listdir(folder)
    for a in liste_files:
        list_link_files.append(folder +'\\'+ a)

def open_csv(csv_file):
    global list1
    with open(csv_file) as csvfile:
        reader = csv.reader(csvfile, delimiter=';', quotechar='|')
        for row in reader:
            list1.append(row[2:11])


def test_match(list_test):

    for a in list1:
        #print(a[3:])
        #print("AVANT : ", a)
        try:
            b = [int(x) for x in a[2:]]
            b = sorted(b)
            #print("APRES : ", b)
        except:
            try:
                b = [int(x) for x in a[3:]]
                b = sorted(b)
            except:
                if debug == 1:
                    print("Erreur : ", a)
                continue

            if list_test == b:
                print("Combinaison trouvée !")
                print("Date : ", a[1], " Combinaison : ", b)
            #print("Erreur : ", a)

        if list_test == b:
            print("Combinaison trouvée !")
            print("Date : ", a[1], " Combinaison : ", b)

def user_number():
    list_numbers = []
    n = 7
    if debug == 0:
        for i in range(0, n):
            num = int(input("Entrez votre numéro : "))
            list_numbers.append(num)
    if debug == 1:
        list_numbers = [20, 41, 38, 7, 25, 3, 7]
    return (list_numbers)


if __name__ == '__main__':
    list_csv_files()
    for link in list_link_files:
        open_csv(link)
    test_match(sorted(user_number()))
    print("Nombre de tirages en base : ", len(list1))


