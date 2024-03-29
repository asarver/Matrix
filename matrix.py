#!/usr/bin/python

from __future__ import division
from fractions import *

class Matrix:
    """A class that has a matrix representation to find the RREF and Det."""
    
    def makeRREF(self, pivotRow=0, pivotCol=0):
        if pivotRow >= self.rows:
            return self.makeRREF(0, pivotCol+1)
        if pivotCol >= self.cols:
            return
        #if pivotRow >= self.rows and pivotCol >= self.cols:
         #   return
        digit = Fraction(self.matrix[pivotRow][pivotCol])
        if digit != 0:
            if digit != 1:
                counter = 0
                self.registry = Fraction(self.registry) * Fraction(digit)
                for c in self.matrix[pivotRow]:
                    self.matrix[pivotRow][counter] = Fraction(c) / Fraction(digit)
                    counter += 1

            counter = 0
            good = False
            while counter <= pivotRow and good == False:
                if self.foundPivot[counter] == False:
                    tempRow = self.matrix[pivotRow]
                    self.matrix[pivotRow] = self.matrix[counter]
                    self.matrix[counter] = tempRow
                    if counter != pivotRow:
                        self.registry = Fraction(self.registry) * -1
                    self.foundPivot[counter] = True
                    good = True
                    pivotRow = counter
                counter += 1
            
            counter = 0
            while counter < self.rows:
                num = Fraction(self.matrix[counter][pivotCol])
                if num != 0 and counter != pivotRow:
                    addRow = []
                    for c in self.matrix[pivotRow]:
                        addRow.append(Fraction(-num)*Fraction(c))
                    colCounter = 0
                    result = []
                    for c in addRow:
                        result.append(Fraction(c +
                                Fraction(self.matrix[counter][colCounter])))
                        colCounter += 1
                    self.matrix[counter] = result
                counter += 1
            self.makeRREF(pivotRow+1, pivotCol+1)
        else:
            self.makeRREF(pivotRow+1, pivotCol)

    def createDet(self):
        if self.rows != self.cols:
            print "Cannot determine a Det for this matrix."
            return
        else:
            counter = 0
            while counter < self.rows:
                self.det = Fraction(self.det) * Fraction(self.matrix[counter][counter])
                counter += 1
        self.det = Fraction(self.det) * Fraction(self.registry)
    
    def displayDet(self):
        print "The Det is ", self.det
    
    def createMatrix(self, matrixRep):
        matrix = matrixRep.split(', ')
        return [r.split(' ') for r in matrix]
    
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
        self.det = Fraction(1);
        self.registry = Fraction(1);


if __name__ == "__main__":
    print 'Input your matrix by rows, seperated by a comma for every new row.'
    print 'Example input: 1 2 3 4, 3 4 5 5'
    print 'Enter in your matrix: '
    matrix = Matrix(raw_input());
    matrix.displayMatrix()
    matrix.makeRREF()
    matrix.displayMatrix()
    matrix.createDet()
    matrix.displayDet()
