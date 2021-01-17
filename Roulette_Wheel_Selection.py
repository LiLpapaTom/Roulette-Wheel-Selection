#Thomas Papaloukas, ICSD14155
import random
from array import *
#Remove comment in onder to plot in Jupyter
#from matplotlib import pyplot as plt

#Function for a 5digit binary number
def rand_binary():
    bin = ""
    for i in range(5):  #Number's length
        tmp = str(random.randint(0,1))  #Since its binary 0,1 and cast it to string
        bin += tmp  #concat it to the previous string
    return bin  #return the string with the 5digit binary number

#Main
population = []
for i in range(10): #Generate 10 random persons using the function above
    population.append(rand_binary())
print("Population :", population)

selection = []
efficiency = []
progressive_sum = []
selection_prob = []
random_n = []
selected_structure = []
removed_persons = []
descendants = []
#Initialize the real descendants array with 0
for x in range(4):
    descendants.append(0);
#print(descendants);

for x in range(5):
    for i in range(4):  #Select 4 random persons from population array
        #Select a person from population in range [0,populations length]
        selection.append(population[random.randint(0,len(population)-1)]);
        population.remove(selection[i]) #Remove the selected person from population, to avoid duplicates
        removed_persons.append(selection[i])    #add them in removed_persons array, to re-add them on the next cycle
        value = int(selection[i],2) #Binary to int, thats our x
        efficiency.append(value*value)  #Calculate efficiency's value, f(x) = x^2
        if i == 0:  #For the 1st step only, the sum[0] is equal to efficiency[0]
            progressive_sum.append(efficiency[i])
        else:  #Else the sum's value is equal to the currents efficiency plus the previous sum, thus progressive
            progressive_sum.append(efficiency[i] + progressive_sum[i-1])

    for i in range(4):
        #Calculate selection's probability for every efficiency element, F(i)/ΣF
        selection_prob.append(efficiency[i]/progressive_sum[3])
        #Generate 4 random n numbers, one for every person in our population in range [0,total efficiency]
        n = random.randint(0,progressive_sum[3])
        random_n.append(n)
        #Search for the 1st progressive_sum element that is greater or equal to the random n, return that "structure"
        # e.g if the 1st element is >= n the returned structure is the value 1
        for j in range(4):
            if progressive_sum[j] >= n:
                selected_structure.append(j+1);
                break;
    #Each descendant element responds to one structure,
    #for example if the 1st structure was chosen 2 times, that means it was 2 descendants
    #therefore the descendants[0] will be equal to 2 (2 times += 1), if the 3rd structure
    #had 3 descendants, the descendants[2] would be equal to 3 (3 times +=1) and so on
    for i in range(4):
        if selected_structure[i] == 1:
            descendants[0] += 1
        elif selected_structure[i] == 2:
            descendants[1] += 1
        elif selected_structure[i] == 3:
            descendants[2] += 1
        elif selected_structure[i] == 4:
            descendants[3] += 1
        else: break;

    for i in range(4):
        #Add the removed persons back in the population, i removed them back then, in order to avoid duplicated selections
        population.append(removed_persons[i])

    print("Selected persons: ",selection);
    print("Efficiency: ", efficiency);
    print("Progressive summary: ",progressive_sum);
    print("Random n number: ",random_n);
    print("Selected structure: ",selected_structure);
    print("Real descendants", descendants)
    print("Selection probability: ",selection_prob)
    print("Total: ",progressive_sum[3]);
    print("\n");
    #Reset arrays for the next iterations
    selection.clear();
    removed_persons.clear();
    efficiency.clear();
    progressive_sum.clear();
    random_n.clear();
    #Add comment to these before plotting the diagramms
    selected_structure.clear();
    selection_prob.clear();


#print(selection_prob, selected_structure)
selected_structure.sort()
selection_prob.sort()

#Commands should be executed when the script is imported in Jupyter notebook (Anaconda installation is mandatory)
#plt.plot(selection_prob, selected_structure)
#plt.ylabel("Selection probability")
#plt.xlabel("Real descendants")
#plt.show()
