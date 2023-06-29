##Program pro Řazení čísel
Tento program umožňuje uživateli zadat řadu celých čísel oddělených čárkou a poté provádí jejich řazení vzestupně pomocí vybraného třídícího algoritmu.

#Třídící algoritmy
Program podporuje následující třídící algoritmy:

#Selection sort
1.Bubble sort
2.Insertion sort
Každý z těchto algoritmů je podrobně popsán v článku, na který je odkazováno v samotném programu. Vyberte si jeden z těchto algoritmů a implementujte ho ve svém programu.

#Použití
Pro spuštění programu zadejte následující příkaz:

python main.py

#Program vás vyzve k zadání řady celých čísel oddělených čárkou. Například:

Zadejte čísla: 0, -2, 10, 1, -8, 18, 3

Poté, co stisknete Enter, program provede třídění a vypíše seřazená čísla oddělená čárkou. V tomto příkladu:

Seřazená čísla: -8, -2, 0, 1, 3, 10, 18

#Ošetření vstupu

Program je navržen tak, aby ošetřil různé formáty vstupu. 
Podporuje zadávání čísel oddělených pouze čárkou (0,-2,10,1,-8...) a také zvládne zpracovat přebytečné mezery mezi zadávanými hodnotami (0, -2, 10, 1, -8...).