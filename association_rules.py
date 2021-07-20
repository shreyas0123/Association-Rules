######################## problem1 #######################
import pandas as pd
5+4
from mlxtend.frequent_patterns import apriori,association_rules
import matplotlib.pyplot as plt
#load the dataset
books = pd.read_csv("C:/Users/DELL/Downloads/book.csv")
books.info
books.columns
books.count
books.describe

#apriori algorithms
frequent_itemsets = apriori(books,min_support = 0.0075,max_len = 4,use_colnames = True)
#most frequent item based on support
frequent_itemsets.sort_values('support',ascending = False, inplace =True)

#barplot of top 10
plt.bar(x = list(range(0,11)), height = frequent_itemsets.support[0:11],color ='rgmyk')
plt.xticks(list(range(0, 11)),frequent_itemsets.itemsets[0:11], rotation =20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = 'lift', min_threshold = 1)
rules.head(20)
rules.sort_values('lift',ascending = False).head(10)
########################## extra part #########################
def to_list(i):
    return (sorted(list(i)))
ma_x = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)
ma_x = ma_x.apply(sorted)
rules_sets = list(ma_x)
unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]
index_rules =[]
for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

#getting rules without any redundancy
rules_no_redundancy = rules.iloc[index_rules,:]

#sorting them with respect to list and getting top 10 rules
rules_no_redundancy.sort_values('lift',ascending = False).head(10)

########################### problem2 ######################################
import pandas as pd
#conda install mlxtend
from mlxtend.frequent_patterns import apriori, association_rules

groceries = []
with open("C:\\Users\\DELL\\Downloads\\groceries.csv") as f:
    groceries = f.read()
#splitting the data into separate  transactions using separator as"/n"
groceries = groceries.split("\n")
groceries_list = []
for i in groceries:
    groceries_list.append(i.split(","))
all_groceries_list = [i for item in groceries_list for i in item]    

from collections import Counter #ordered dictionary
item_frequencies = Counter(all_groceries_list)    

#after sorting
item_frequencies = sorted(item_frequencies.items(),key = lambda x:x[1])    

#storing frequencies and items in separate variables
frequencies =list(reversed([i[1] for i in item_frequencies]))   
items = list(reversed([i[0] for i in item_frequencies ]))    

#creating dataframe
groceries_series = pd.Dataframe(pd.series(groceries_list))

#barplot of top 10
import matplotlib.pylab as plt 

plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), items[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()


# Creating Data Frame for the transactions data
groceries_series = pd.DataFrame(pd.Series(groceries_list))
groceries_series = groceries_series.iloc[:9835, :] # removing the last empty transaction

groceries_series.columns = ["transactions"]

# creating a dummy columns for the each item in each transactions ... Using column names as item name
X = groceries_series['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')

frequent_itemsets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

################################# Extra part ###################################
def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

################################## problem3 #########################
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
movies_data = pd.read_csv("C:\\Users\\DELL\\Downloads\\my_movies.csv")
movies_data.columns
movies_data.isna().sum()
movies_data.isnull().sum()
movies_drop = movies_data.drop(["V1","V2","V3","V4","V5"],axis = 1)

frequent_itemsets = apriori(movies_drop, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

################################# Extra part ###################################
def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

############################ problem4 ###################
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
my_ph_data = pd.read_csv("C:\\Users\\DELL\\Downloads\\myphonedata.csv")
my_ph_data.columns
my_ph_data.isna().sum()
my_ph_data.isnull().sum()
my_ph_data_drop = movies_data.drop(["V1","V2","V3"],axis = 1)

frequent_itemsets = apriori(my_ph_data_drop, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

################################# Extra part ###################################
def to_list(i):
    return (sorted(list(i)))

ma_X = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

ma_X = ma_X.apply(sorted)

rules_sets = list(ma_X)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))

# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

##########################Problem 5######################################################

import pandas as pd
import matplotlib.pyplot as plt
from mlxtend.frequent_patterns import association_rules,apriori

retails = []
with open("C://Users//DELL//Downloads//transactions_retail1.csv") as f:
    retails = f.read()

retails = retails.split("\n")

retails = retails[:100]

retails_list = []
for i in retails:
    retails_list.append(i.split(","))


all_retails_list = [i for item in retails_list for i in item]

new_all_retails_list =[]
for i in all_retails_list:
    if i != "NA":
        new_all_retails_list.append(i)
        
from collections import Counter # ,OrderedDict 

item_frequencies = Counter(new_all_retails_list)

# after sorting
item_frequencies = sorted(item_frequencies.items(), key = lambda x:x[1])

# Storing frequencies and items in separate variables 
frequencies = list(reversed([i[1] for i in item_frequencies]))
items = list(reversed([i[0] for i in item_frequencies]))

# barplot of top 10 
plt.bar(height = frequencies[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), items[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

# Creating Data Frame for the transactions data
retail_series = pd.DataFrame(pd.Series(retails_list))

retail_series.columns = ["transactions"]

X = retail_series['transactions'].str.join(sep = '*').str.get_dummies(sep = '*')
X = X.drop(['NA'] , axis =1)

frequent_itemsets = apriori(X, min_support = 0.0075, max_len = 4, use_colnames = True)

# Most Frequent item sets based on support 
frequent_itemsets.sort_values('support', ascending = False, inplace = True)

plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation=20)
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()

rules = association_rules(frequent_itemsets, metric = "lift", min_threshold = 1)
rules.head(20)
rules.sort_values('lift', ascending = False).head(10)

def to_list(i):
    return (sorted(list(i)))

new_rules = rules.antecedents.apply(to_list) + rules.consequents.apply(to_list)

new_rules = new_rules.apply(sorted)

rules_sets = list(new_rules)

unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_sets)]

index_rules = []

for i in unique_rules_sets:
    index_rules.append(rules_sets.index(i))
    
# getting rules without any redudancy 
rules_no_redudancy = rules.iloc[index_rules, :]

# Sorting them with respect to list and getting top 10 rules 
rules_no_redudancy.sort_values('lift', ascending = False).head(10)

################################END#####################################################

    
    
    
    








