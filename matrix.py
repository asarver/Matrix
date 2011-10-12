#!/usr/bin/python

from __future__ import division
from fractions import Fraction

class Matrix:
    """A class that has a matrix representation to find the RREF and Det."""
    
    def makeRREF(self, pivotRow, pivotCol):
        if pivotRow >= self.rows:
            return self.makeRREF(0, pivotCol+1)
        digit = int(self.matrix[pivotRow][pivotCol])
        if digit != 0:
            if digit != 1:
                counter = 0
                for c in self.matrix[pivotRow]:
                    self.matrix[pivotRow][counter] = Fraction(int(c), digit)
                    counter += 1

            if pivotRow >= pivotCol:
                counter = 0
                good = False
                while counter <= pivotRow and good == False:
                    if self.foundPivot[counter] == False:
                        tempRow = self.matrix[pivotRow]
                        self.matrix[pivotRow] = self.matrix[counter]
                        self.matrix[counter] = tempRow
                        self.foundPivot[counter] = True
                        good = True
                    counter += 1

        else:
            return self.makeRREF(pivotRow+1, pivotCol)

    def createMatrix(self, matrixRep):
        matrix = matrixRep.split(', ')
        newMatrix = []
        for r in matrix:
            newMatrix.append(r.split(' '))
        return newMatrix
    
    def displayMatrix(self):
        for r in self.matrix:
            for c in r:
                print c,
            print

    def populatePivot(self):
        counter = 0
        while(counter < self.rows):
            self.foundPivot[counter] = False
            counter += 1

    def __init__(self, matrixRep):
        self.matrix = self.createMatrix(matrixRep);
        self.rows = len(self.matrix);
        self.cols = len(self.matrix[0]);
        self.foundPivot = {}
        self.populatePivot()
        self.det = 0;
        self.registry = 1;


if __name__ == "__main__":
    print 'Input your matrix by rows, seperated by a comma for every new row.'
    print 'Example input: 1 2 3 4, 3 4 5 5'
    print 'Enter in your matrix: '
    matrix = Matrix(raw_input());
    matrix.displayMatrix()
    matrix.makeRREF(0, 0)
    matrix.displayMatrix()
