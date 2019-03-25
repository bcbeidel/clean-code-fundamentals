#   The following python script contains a series of transformations on raw dataset 
# in preparation for a machine learning process. However, the author didn't have 
# much regard for good coding practices. Given what you have learned 
# thus far, refactor this script into something more modular and readable.

import pandas as pd

trd = pd.read_csv("./data/train.csv", index_col="customer_id")
tstd  = pd.read_csv("./data/test.csv", index_col="customer_id")

trd = trd.drop_duplicates()
tstd  = tstd.drop_duplicates()

# map `sex` to a categorical variable
trd['sex'] = trd['sex'].map({1:'male', 2:'female'})
trd['sex'] = trd['sex'].astype('category')
tstd['sex'] = tstd['sex'].map({1:'male', 2:'female'})
tstd['sex'] = tstd['sex'].astype('category')


# map `marriage` to a categorical variable and handle null values
trd['marriage'] = trd['marriage'].map({1:'single', 2:'married', 3:'other'})
trd['marriage'] = trd['marriage'].fillna('other')
trd['marriage'] = trd['marriage'].astype('category')
tstd['marriage'] = tstd['marriage'].map({1:'single', 2:'married', 3:'other'})
tstd['marriage'] = tstd['marriage'].fillna('other')
tstd['marriage'] = tstd['marriage'].astype('category')

# map `education` back to human readable categorical variables and handle null values
trd['education'] = trd['education'].map({1:'graduate_shool', 2:'university', 3:'high_school', 4:'other'})
trd['education'] = trd['education'].fillna('other')
trd['education'] = trd['education'].astype('category')
tstd['education'] = tstd['education'].map({1:'graduate_shool', 2:'university', 3:'high_school', 4:'other'})
tstd['education'] = tstd['education'].fillna('other')
tstd['education'] = tstd['education'].astype('category')

# restate bill amounts as a fraction of the credit limit
for f in ['bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6']:
    trd[f] = trd[f] / trd['limit_bal']
    tstd[f] = tstd[f] / tstd['limit_bal']

# restate pay amounts as a fraction of the credit limit
for f in ['pay_amt1', 'pay_amt2', 'pay_amt2', 'pay_amt3', 'pay_amt4', 'pay_amt5', 'pay_amt6']:
    trd[f] = trd[f] / trd['limit_bal']
    tstd[f] = tstd[f] / tstd['limit_bal']

# generate new `months_late` feature
trd['months_late'] = trd['pay_1'] + trd['pay_2'] + trd['pay_3'] + trd['pay_4'] + trd['pay_5'] + trd['pay_6']
tstd['months_late'] = tstd['pay_1'] + tstd['pay_2'] + tstd['pay_3'] + tstd['pay_4'] + trd['pay_5'] + trd['pay_6']
