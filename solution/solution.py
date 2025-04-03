import numpy as np
import matplotlib.pyplot as plt


alternatives = np.array([
    [5, 2],  # A1
    [2, 1],  # A2
    [9, 3],  # A3
    [9, 0],  # A4
    [8, 9],  # A5
    [0, 9],  # A6
    [3, 1],  # A7
    [7, 3],  # A8
    [6, 4],  # A9
    [3, 5],  # A10
    [4, 8],  # A11
    [9, 5],  # A12
    [7, 7],  # A13
    [1, 3],  # A14
    [3, 3],  # A15
    [9, 8],  # A16
    [4, 9],  # A17
    [5, 5],  # A18
    [5, 5],  # A19
    [9, 3]   # A20
])


def find_pareto_info(alternatives):
    n = len(alternatives)
    pareto_status = []
    
    for i, alt_i in enumerate(alternatives):
        is_pareto = True
        dominated_by = None
        
        for j, alt_j in enumerate(alternatives):
            if i != j:
                # Check if alt_j dominates alt_i
                if np.all(alt_j >= alt_i) and np.any(alt_j > alt_i):
                    is_pareto = False
                    dominated_criteria = []
                    if alt_j[0] > alt_i[0]:
                        dominated_criteria.append("Q1")
                    if alt_j[1] > alt_i[1]:
                        dominated_criteria.append("Q2")
                    dominated_by = (j+1, dominated_criteria)
                    break
        
        if is_pareto:
            pareto_status.append(("Оптимальне", None))
        else:
            pareto_status.append(("Неоптимальне", dominated_by))
    
    return pareto_status

#Slater
def find_slater_info(alternatives):
    n = len(alternatives)
    slater_status = []
    
    for i, alt_i in enumerate(alternatives):
        is_slater = True
        dominated_by = None
        
        for j, alt_j in enumerate(alternatives):
            if i != j:
                # Check if alt_j strictly dominates alt_i
                if np.all(alt_j > alt_i):
                    is_slater = False
                    dominated_by = (j+1, ["Q1", "Q2"])
                    break
        
        if is_slater:
            slater_status.append(("Оптимальне", None))
        else:
            slater_status.append(("Неоптимальне", dominated_by))
    
    return slater_status

#Optimal solution
pareto_info = find_pareto_info(alternatives)
slater_info = find_slater_info(alternatives)


print("Парето аналіз:")
for i, (status, info) in enumerate(pareto_info):
    if status == "Оптимальне":
        print(f"A{i+1}: {status}")
    else:
        dominator, criteria = info
        print(f"A{i+1}: {status}, домінується A{dominator} за критеріями {', '.join(criteria)}")

print("\nСлейтер аналіз:")
for i, (status, info) in enumerate(slater_info):
    if status == "Оптимальне":
        print(f"A{i+1}: {status}")
    else:
        dominator, criteria = info
        print(f"A{i+1}: {status}, строго домінується A{dominator}")

#Table
pareto_results = []
for status, info in pareto_info:
    if status == "Оптимальне":
        pareto_results.append("Оптимальне")
    else:
        dominator, criteria = info
        pareto_results.append(f"Домінується за {'+'.join(criteria)}")

slater_results = []
for status, info in slater_info:
    if status == "Оптимальне":
        slater_results.append("Оптимальне")
    else:
        dominator, criteria = info
        slater_results.append(f"Строго домінується")


print("\nРезультати аналізу:")
print("Альтернатива | Парето | Слейтер")
print("-------------|--------|--------")
for i in range(20):
    print(f"A{i+1:<11} | {pareto_results[i]:<6} | {slater_results[i]:<8}")


plt.figure(figsize=(10, 7))
plt.scatter(alternatives[:, 0], alternatives[:, 1], c='blue', label='Всі альтернативи')
for i in range(len(alternatives)):
    plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                 textcoords='offset points')
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.title('Всі альтернативи')
plt.grid(True)
plt.savefig('all_alternatives.png')

#Pareto 
plt.figure(figsize=(10, 7))
pareto_optimal = [i for i, (status, _) in enumerate(pareto_info) if status == "Оптимальне"]
plt.scatter(alternatives[:, 0], alternatives[:, 1], c='blue', alpha=0.3, label='Неоптимальні')
plt.scatter(alternatives[pareto_optimal, 0], alternatives[pareto_optimal, 1], c='red', label='Оптимальні за Парето')
for i in range(len(alternatives)):
    if i in pareto_optimal:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', color='red')
    else:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', alpha=0.5)
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.title('Множина оптимальних за Парето')
plt.grid(True)
plt.legend()
plt.savefig('pareto_set.png')

#Slater
plt.figure(figsize=(10, 7))
slater_optimal = [i for i, (status, _) in enumerate(slater_info) if status == "Оптимальне"]
plt.scatter(alternatives[:, 0], alternatives[:, 1], c='blue', alpha=0.3, label='Неоптимальні')
plt.scatter(alternatives[slater_optimal, 0], alternatives[slater_optimal, 1], c='green', label='Оптимальні за Слейтером')
for i in range(len(alternatives)):
    if i in slater_optimal:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', color='green')
    else:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', alpha=0.5)
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.title('Множина оптимальних за Слейтером')
plt.grid(True)
plt.legend()
plt.savefig('slater_set.png')

#Comparing Pareto and Slater
plt.figure(figsize=(10, 7))
plt.scatter(alternatives[:, 0], alternatives[:, 1], c='lightgray', alpha=0.4, label='Неоптимальні')


slater_not_pareto = [i for i in slater_optimal if i not in pareto_optimal]
if slater_not_pareto:
    plt.scatter(alternatives[slater_not_pareto, 0], alternatives[slater_not_pareto, 1], 
                c='green', label='Тільки Слейтер')


pareto_not_slater = [i for i in pareto_optimal if i not in slater_optimal]
if pareto_not_slater:
    plt.scatter(alternatives[pareto_not_slater, 0], alternatives[pareto_not_slater, 1], 
                c='red', label='Тільки Парето')


both = [i for i in pareto_optimal if i in slater_optimal]
plt.scatter(alternatives[both, 0], alternatives[both, 1], c='purple', label='І Парето, і Слейтер')

for i in range(len(alternatives)):
    if i in both:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', color='purple')
    elif i in pareto_not_slater:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', color='red')
    elif i in slater_not_pareto:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', color='green')
    else:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', alpha=0.5)
                     
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.title('Порівняння оптимальних множин Парето та Слейтера')
plt.grid(True)
plt.legend()
plt.savefig('comparison.png')


plt.figure(figsize=(10, 7))
plt.scatter(alternatives[:, 0], alternatives[:, 1], c='blue', alpha=0.3)


pareto_points = alternatives[pareto_optimal]


idx = np.argsort(-pareto_points[:, 0])
frontier_points = pareto_points[idx]


unique_q1 = np.unique(frontier_points[:, 0])
sorted_frontier = []

for q1 in unique_q1:
    same_q1_points = frontier_points[frontier_points[:, 0] == q1]
   
    same_q1_sorted = same_q1_points[np.argsort(same_q1_points[:, 1])]
    for point in same_q1_sorted:
        sorted_frontier.append(point)

sorted_frontier = np.array(sorted_frontier)


plt.plot(sorted_frontier[:, 0], sorted_frontier[:, 1], 'r--', label='Межа Парето')
plt.scatter(pareto_points[:, 0], pareto_points[:, 1], c='red', label='Оптимальні за Парето')

for i in range(len(alternatives)):
    if i in pareto_optimal:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', color='red')
    else:
        plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                     textcoords='offset points', alpha=0.5)
                     
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.title('Межа Парето')
plt.grid(True)
plt.legend()
plt.savefig('pareto_frontier.png')


plt.figure(figsize=(10, 7))


for i in range(len(alternatives)):
    for j in range(len(alternatives)):
        if i != j:
            # If j dominates i (at least one better, none worse)
            if np.all(alternatives[j] >= alternatives[i]) and np.any(alternatives[j] > alternatives[i]):
                plt.arrow(alternatives[i, 0], alternatives[i, 1], 
                          alternatives[j, 0] - alternatives[i, 0], 
                          alternatives[j, 1] - alternatives[i, 1], 
                          head_width=0.3, head_length=0.3, fc='gray', ec='gray', alpha=0.3)


plt.scatter(alternatives[:, 0], alternatives[:, 1], c='blue', alpha=0.5, label='Всі альтернативи')
plt.scatter(alternatives[pareto_optimal, 0], alternatives[pareto_optimal, 1], 
            c='red', label='Оптимальні за Парето')
plt.scatter(alternatives[slater_optimal, 0], alternatives[slater_optimal, 1], 
            facecolors='none', edgecolors='green', s=100, label='Оптимальні за Слейтером')

for i in range(len(alternatives)):
    plt.annotate(f'A{i+1}', (alternatives[i, 0], alternatives[i, 1]), xytext=(5, 5), 
                 textcoords='offset points')
                 
plt.xlabel('Q1')
plt.ylabel('Q2')
plt.title('Відношення домінування')
plt.grid(True)
plt.legend()
plt.savefig('dominance_relations.png')