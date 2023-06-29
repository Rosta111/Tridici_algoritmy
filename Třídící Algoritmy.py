def bubbleSort(zadanePole):
    swapped = False
    for n in range(len(zadanePole)-1, 0, -1):
        for i in range(n):
            if zadanePole[i] > zadanePole[i + 1]:
                swapped = True
                zadanePole[i], zadanePole[i + 1] = zadanePole[i + 1], zadanePole[i]       
        if not swapped:
            return

def selectionSort(zadanePole):
     
    for i in range(len(zadanePole) - 1):
        min_index = i 
         
        for j in range(i + 1, len(zadanePole)):
            if (zadanePole[j] < zadanePole[min_index]):
                min_index = j
                 
        zadanePole[i], zadanePole[min_index] = zadanePole[min_index], zadanePole[i] 

def insertionSort(zadanePole):
    i = 0
    klic = 0
    j = 0
    for i in range(1,len(zadanePole),1):
        klic = zadanePole[i]
        j = i - 1
        while (j >= 0 and zadanePole[j] > klic):
            zadanePole[j + 1] = zadanePole[j]
            j = j - 1
        zadanePole[j + 1] = klic

cisla = input("Zadej čísla pro seřazení (oddělená čárkou):")
vstupniPole = [int(n) for n in cisla.split(",")]
#bubbleSort(vstupniPole)
#selectionSort(vstupniPole)
insertionSort(vstupniPole)
print("Seřazená čísla:")
print(*vstupniPole, sep = ', ')





