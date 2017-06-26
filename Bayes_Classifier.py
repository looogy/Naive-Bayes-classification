import csv
filename = 'D:\\PyProject\\NoSQL\\pima-indians-diabetes.csv'


def loadCsv(filename):
	'''读入csv文件，并转化为集合，参数为文件名'''
	with open(filename) as f:
		lines = csv.reader(f)
		dataset = list(lines)
	for i in range(len(dataset)):
		dataset[i] = [float(x) for x in dataset[i]]
	return dataset


import random
def splitDataset(dataset,splitRatio):
	'''划分训练集与测试集，参数为一个集合，一个划分比例'''
	trainSize = int(len(dataset) * splitRatio)
	trainSet = []
	copy = list(dataset)
	while len(trainSet) <= testSize:
		index = random.randrange(len(copy))
		trainSet.append(copy.pop(index))
	testSet = copy
	return trainSet, testSet


def separateByClass(dataset):
	'''按最后一个元素（是否患糖尿病）划分数据，参数为一个集合'''
	separated = {}
	for i in range(len(dataset)):
		vector = dataset[i]
		if vector[-1] not in separated:
			separated[vector[-1]] = []
		separated[vector[-1]].append(vector)
	return separated


import math
def mean(numbers):
	'''求平均值，参数为list'''
	return sum(numbers) / (len(numbers))
def stdev(numbers):
	'''求标准差，参数为list(和求平均值的参数保持一致)'''
	avg = mean(numbers)
	variance = sum(pow(x - avg, 2) for x in numbers) / (len(numbers) - 1)
	return math.sqrt(variance)


def summarize(dataset):
	'''将样本按属性分组求取均值、标准差，参数为集合'''
	summarizes = [(mean(attribute), stdev(attribute)) for attribute in zip(*dataset)]
	del summarizes[-1]
	return summarizes


def summarizeByClass(dataset):
	separated = separateByClass(dataset)
	summarizes = {}
	for classValue, instances in iter(separated.items()):
		print(classValue, instances)
		summarizes[classValue] = summarizes(instances)
	return summarizes


dataset = [[1, 10, 0], [2, 20, 1], [3, 30, 1]]
summary = summarizeByClass(dataset)




