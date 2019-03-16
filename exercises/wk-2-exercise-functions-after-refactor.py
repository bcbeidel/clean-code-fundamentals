# Conduct a series of data transformations to training and test sets prior to modeling
import pandas as pd

def transform_sex(data):
    """Transform Numeric To Cateogical Features"""
    data['sex'] = data['sex'].map({1:'male', 2:'female'})
    data['sex'] = data['sex'].astype('category')
    return data

def transform_education(data):
    """Handle education factor levels that don't meet expectation, turn to string for interpretation"""
    data['education'] = data['education'].map({1:'graduate_shool', 2:'university', 3:'high_school', 4:'other'})
    data['education'] = data['education'].fillna('other')
    data['education'] = data['education'].astype('category')
    return data

def transform_marriage(data):
    """Handle marriage factor levels that don't meet expectation, turn to string for interpretation"""
    data['marriage'] = data['marriage'].map({1:'single', 2:'married', 3:'other'})
    data['marriage'] = data['marriage'].fillna('other')
    data['marriage'] = data['marriage'].astype('category')
    return data

def transform_categoical_features(data):
    data = transform_sex(data)
    data = transform_education(data)
    data = transform_marriage(data)
    data = data
    return data

def transform_bill_and_pay_amount(data):
    """Express Bill Amount in terms of Percentage of total Credit Limit"""
    for feature in ['bill_amt1', 'bill_amt2', 'bill_amt3', 'bill_amt4', 'bill_amt5', 'bill_amt6']:
        data[feature] = data[feature] / data['limit_bal']
        
    for feature in ['pay_amt1', 'pay_amt2', 'pay_amt2', 'pay_amt3', 'pay_amt4', 'pay_amt5', 'pay_amt6']:
        data[feature] = data[feature] / data['limit_bal']
        
    return data    

def generate_total_months_delinqient(data):
    data['tmd'] = data['pay_1'] + data['pay_2'] + data['pay_3'] + data['pay_4'] + data['pay_5'] + data['pay_6']
    return data

def transform_target(data):
    """Transform Target To Boolean"""
    targets = {'yes':True, 'no':False}
    data['default_oct'] = data['default_oct'].map(targets)
    data['default_oct'] = data['default_oct'].astype('bool')
    return data

def get_transformed_data(path_to_data, is_training):
    data = pd.read_csv(path_to_data, index_col='customer_id')
    
    # Ensure No Duplicated Records
    data = data.drop_duplicates()
    
    # Inital take, drop all with null values, ask further questions why NaN exists
    data = data.dropna(axis=0)
    
    data = transform_categoical_features(data)
    data = transform_bill_and_pay_amount(data)
    data = generate_total_months_delinqient(data)
    
    if is_training:
        data = transform_target(data)
  
    return data
    
test_data = get_transformed_data(path_to_data = "../data/train.csv", is_training = True)
train_data = get_transformed_data(path_to_data = "../data/test.csv", is_training = False) 