#   The following python script contains a series of transformations on raw dataset 
# in preparation for a machine learning process. However, the author didn't have 
# much regard for good coding practices. Given what you have learned 
# thus far, refactor this script into something more modular and readable.
# 
# Note: This is merely one possible solution, of infinitely many... the primary
#       objective of this exercise is to go through the effort of identifying opportunities
#       to choose better names, and find opportunities to functionalise repeated blocks of code

import pandas as pd

def get_credit_card_data(path):
    data = pd.read_csv(path, index_col='customer_id')
    return(data)

def handle_duplicate_records(data):
    data = data.drop_duplicates()
    return data

def transform_sex(data):
    """Transform Numeric To Categorical Features"""
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

def transform_target_variable(data):
    """Transform Target To Boolean"""
    targets = {'yes':True, 'no':False}
    data['default_oct'] = data['default_oct'].map(targets)
    data['default_oct'] = data['default_oct'].astype('bool')
    return data

def get_transformed_credit_card_data(path_to_data, is_training):
  """Get and transform credit card data into f"""
    data = get_credit_card_data(path_to_data)
    data = handle_duplicate_records(data)
    data = transform_categoical_features(data)
    data = transform_bill_and_pay_amount(data)
    data = generate_total_months_delinqient(data)
    
    if is_training:
        data = transform_target_variable(data)
  
    return data
    
test_data = get_transformed_credit_card_data(path_to_data = "../data/train.csv", is_training = True)
train_data = get_transformed_credit_card_data(path_to_data = "../data/test.csv", is_training = False) 
