install.packages("arules")
library(arules)#using for building association rules i.e apriori algorithm
#loading the dataset
book_data <- read.csv("C:\\Users\\DELL\\Downloads\\book.csv",colClasses = 'factor')
summary(book_data)

#building  rules using apriori algorithms
arules <- apriori(book_data,parameter = list(minlen = 2,maxlen = 3 ,supp=0.7))
inspect(arules) #showing all the transactions
summary(book_data)

#viewing rules based on lift value
inspect(head(sort(arules, by ="lift")))#to view we use inspect

#overall quality
head(quality(arules))

install.packages("arulesViz")
library(arulesViz) # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

write(arules, file = "a_rules.csv", sep = ",")

getwd()


################################## problem2 ##################################
install.packages("arule")
library(arules)
#loading the dataset

#load the dataset
groc <- read.csv("C:\\Users\\DELL\\Downloads\\groceries.csv",colClasses = "factor")
sum(is.na(groc))
sum(is.null(groc))

#model building using aprori algorithm
arules <- apriori(groc,parameter = list(minlen = 2,maxlen = 3,supp = 0.02,conf = 0.7))
inspect(arules)

#viewing the rules based on lift value
inspect(head(sort(arules, by ="lift")))#to view we use inspect

#overall quality
head(quality(arules))

install.packages("arulesViz")
library(arulesViz) # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

write(arules, file = "a_rules.csv", sep = ",")

getwd()

################################# problem3 ###########################

install.packages("arule")
library(arules)
#loading the dataset

#load the dataset
mov <- read.csv("C:\\Users\\DELL\\Downloads\\my_movies.csv",colClasses = "factor")
sum(is.na(mov))
sum(is.null(mov))

#model building using aprori algorithm
arules <- apriori(mov,parameter = list(minlen = 2,maxlen = 3,supp = 0.8,conf = 0.7))
inspect(arules)

#viewing the rules based on lift value
inspect(head(sort(arules, by ="lift")))#to view we use inspect

#overall quality
head(quality(arules))

install.packages("arulesViz")
library(arulesViz) # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

write(arules, file = "a_rules.csv", sep = ",")

getwd()

####################################### problem4 #####################################
install.packages("arule")
library(arules)
#loading the dataset

#load the dataset
myphn <- read.csv("C:\\Users\\DELL\\Downloads\\myphonedata.csv",colClasses = "factor")
sum(is.na(myphn))
sum(is.null(myphn))

#model building using aprori algorithm
arules <- apriori(myphn,parameter = list(minlen = 2,maxlen = 3,supp = 0.4,conf = 0.9))
inspect(arules)

#viewing the rules based on lift value
inspect(head(sort(arules, by ="lift")))#to view we use inspect

#overall quality
head(quality(arules))

install.packages("arulesViz")
library(arulesViz) # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

write(arules, file = "a_rules.csv", sep = ",")

getwd()

######################################## problem5 ########################################

install.packages("arule")
library(arules)
#loading the dataset

#load the dataset
trans <- read.csv("C:\\Users\\DELL\\Downloads\\transactions_retail1.csv")
sum(is.na(trans))
sum(is.null(trans))
summary(trans)

trans[is.na(trans)] <- ""

#model building using aprori algorithm
arules <- apriori(trans,parameter = list(minlen = 2,maxlen = 3,supp = 0.02,conf = 0.9))
inspect(arules)

#viewing the rules based on lift value
inspect(head(sort(arules, by ="lift")))#to view we use inspect

#overall quality
head(quality(arules))

install.packages("arulesViz")
library(arulesViz) # for visualizing rules

# Different Ways of Visualizing Rules
plot(arules)

windows()
plot(arules, method = "grouped")
plot(arules[1:10], method = "graph") # for good visualization try plotting only few rules

write(arules, file = "a_rules.csv", sep = ",")

getwd()




