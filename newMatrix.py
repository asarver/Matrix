#!/usr/bin/python

from __future__ import division
from fractions import *

class Matrix:

    def rref(self, pivotRow=0, pivotCol=0):
        if pivotRow >= self.rows:
            return self.rref(0, pivotCol+1)
        if pivotCol >= self.cols:
            return

        digit = Fraction(self.matrix[pivotRow][pivotCol])

        if digit:
            if digit is not 1:
                self.registry = Fraction(self.registry) * Fraction(digit)
                for colCounter in range(0, self.cols):
                    for c in self.matrix[pivotRow]:
                        self.matrix[pivotRow][colCounter] = Fraction(c) / Fraction(digit)
            foundNonPivot = False
            for nonPivotRow in range(0, pivotRow+1):
                if not foundNonPivot or not self.ifPivotRow[nonPivotRow] and nonPivotRow is not pivotRow:
                        tempRow = self.matrix[pivotRow]
                        self.matrix[pivotRow] = self.matrix[nonPivotRow]
                        self.matrix[nonPivotRow] = tempRow
                        self.registry *= -1
                        foundNonPivot = True
                        pivotRow = nonPivotRow
            for numberOfRows in range(0, self.rows):
                numberInPos = Fraction(self.matrix[numberOfRows][pivotCol])
                if numberInPos is not 0 and numberOfRows is not pivotRow:
                    rowToBeAdded = []
                    for c in self.matrix[pivotRow]:
                        rowToBeAdded.append(Fraction(-numberInPos) *
                                Fraction(c))
                    resultOfAdding = []
                    for numberOfCols in range(0, self.cols):
                        resultOfAdding.append(Fraction(c) +
                                Fraction(self.matrix[numberOfRows][numberOfCols]))
                    self.matrix[numberOfRows] = resultOfAdding
            self.rref(pivotRow+1, pivotCol+1)

        else:
            self.rref(pivotRow+1, pivotCol)

    def det(self):
        pass

    def createMatrix(self, matrix_Representation):
       matrix = matrix_Representation.split(', ')
       return [r.split(' ') for r in matrix]

    def displayMatrix(self):
        for r in self.matrix:
            for c in r:
                print c,
            print

    def populatePivotDict(self):
        pass

    def __init__(self, matrix_Representation):
        self.matrix = self.createMatrix(matrix_Representation)
        self.rows = len(self.matrix)
        self.cols = len(self.matrix[0])
        self.ifPivotRow = {}
        self.populatePivotDict()
        self.det = Fraction(1)
        self.registry = Fraction(1)


if __name__ == "__main__":
    print 'Input your matrix by rows, seperated by a comma for every new row.'
    print 'Example input: 1 2 3 4, 3 4 5 5'
    print 'Enter in your matrix: '
    user_input = raw_input()
    matrix = Matrix(user_input)
    matrix.displayMatrix()
    matrix.rref()
    matrix.displayMatrix()
