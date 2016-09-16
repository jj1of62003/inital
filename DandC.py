#!/bin/python3

class node:
	def __init__(self):
		self.right = None
		self.left = None

def msort1(numList):
	msort(numList, 0, len(numList) - 1)


def msort(numList, first, last):
	"""This is the initiator for the Merg sort algorithm"""
	listLen = len(numList)
	if listLen != 1:
		middle = listLen // 2
		msort(numList, first, middle)
		msort(numList, middle + 1, last)
		merg(numList, first, middle, last)

def merg(numList, first, middle last):
	L = numList[first:middle]
	R = numList[middle:last + 1]
	i, j = 0

	for k in range(first, last + 1):
		if L[i] < R[j]:
			numList[k] = L[i]
			i += 1
		else:
			numList[k] = R[j]
			j += 1

	return numList