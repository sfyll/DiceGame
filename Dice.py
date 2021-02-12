#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 20:32:10 2021

@author: santi
"""

import numpy as np
def howMuchWePay(remainingRolls, faceNumber, rollCost = 0):
    """
    Assuming we follow the strategy that maximizes expected value,
    determines the expected outcome of x remaining dicerolls.  
    """
    if remainingRolls == 1:
        
        if rollCost != 0: #ReconstructArray taking into consideration costs for easier computations, long life vectorization
            costArray = np.full((faceNumber), rollCost)
            result = range(1, faceNumber+1) - costArray
            result[result<0] = 0 
            result = np.mean(result)
        else:
            result = np.mean(range(1,faceNumber+1))

    else:   
        if rollCost == 0: #Easier and cleaner logic to separate into two scenarios of rollCost
            probReroll = int(howMuchWePay(remainingRolls-1, faceNumber, rollCost))/faceNumber
            notRerolledOutcomes = range(int(howMuchWePay(remainingRolls-1, faceNumber, rollCost)) + 1, faceNumber+1)
            currExpectationAssumingNoReroll = np.mean(notRerolledOutcomes)
            result = \
                probReroll * howMuchWePay(remainingRolls-1, faceNumber, rollCost) + \
                (1 - probReroll) * currExpectationAssumingNoReroll
        else:
            payOffArray = range(1, faceNumber+1) - np.full((faceNumber), rollCost)
            EV = howMuchWePay(remainingRolls-1, faceNumber, rollCost)
            payOffArray[payOffArray < EV] = 0
            probReroll = 1-len(payOffArray[payOffArray != False])/faceNumber
            notRerolledOutcomes = range(int(EV)+1, payOffArray[-1]+1)
            currExpectationAssumingNoReroll = np.mean(notRerolledOutcomes)
            result = \
                probReroll * EV + \
                (1 - probReroll) * currExpectationAssumingNoReroll
            
    return result







