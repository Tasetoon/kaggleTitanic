import pandas as pd

def prepare_train(path: str):
    train = pd.read_csv(path, on_bad_lines='skip', na_values='?')

    train = train.drop(columns=['PassengerId'])
    train = train.drop(columns=['Name'])
    train = train.drop(columns=['Cabin'])
    train = train.drop(columns=['Ticket'])

    train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])
    train['Age'] = train['Age'].fillna(train['Age'].mean())
    train['Relatives'] = train['SibSp'] + train['Parch']
    train['Relatives'] = train['SibSp'] + train['Parch']


    sex_categorical_values = {'female': 0, 'male': 1}
    embarked_categorical_values = {'S': 0, 'Q':1, 'C':2}
    train['Sex'] = train['Sex'].apply(lambda x: sex_categorical_values[x])
    train['Embarked'] = train['Embarked'].apply(lambda x: embarked_categorical_values[x])

    return train
