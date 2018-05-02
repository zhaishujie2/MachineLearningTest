#!/usr/bin/python
import  math
def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ages = ages.reshape(1,len(ages))[0]
    predictions = predictions.reshape(1,len(predictions))[0]
    net_worths = net_worths.reshape(1,len(net_worths))[0]
    cleaned_data = zip(ages,net_worths,abs(net_worths-predictions))
    cleaned_data = sorted(cleaned_data,key=lambda x: x[2])
    cleaned_num = int(-1*math.ceil(len(cleaned_data)*0.1))
    cleaned_data = cleaned_data[:cleaned_num]

    ### your code goes here

    
    return cleaned_data

