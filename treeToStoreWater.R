setwd("/Users/bhaveshshah/Desktop/TreeDataAnalysis")
dataset <- read.csv("finaldata.csv", header=T, colClasses = c("numeric", "numeric", "numeric", "numeric", "numeric", "numeric"))
simple.fit = lm(aggrVolume~trees,data=dataset)
print(summary(simple.fit))

print(with(dataset,plot(trees, aggrVolume)))
print(abline(simple.fit))



