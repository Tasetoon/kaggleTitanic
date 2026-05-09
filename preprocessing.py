import pandas as pd

def prepare_data(path: str):
    train = pd.read_csv(path, on_bad_lines='skip', na_values='?')

    train['Title'] = train['Name'].str.extract(r' ([A-Za-z]+)\.')
    train['Title'] = train['Title'].replace(['Lady','Countess','Capt','Col','Don','Dr','Major','Rev','Sir','Jonkheer','Dona'], 'Rare')
    train['Title'] = train['Title'].replace('Mlle', 'Miss')
    train['Title'] = train['Title'].replace('Ms', 'Miss')
    train['Title'] = train['Title'].replace('Mme', 'Mrs')

    train = train.drop(columns=['PassengerId'])
    train = train.drop(columns=['Name'])
    train = train.drop(columns=['Cabin'])
    train = train.drop(columns=['Ticket'])

    train['Embarked'] = train['Embarked'].fillna(train['Embarked'].mode()[0])
    train['Age'] = train['Age'].fillna(train['Age'].mean())
    train['Relatives'] = train['SibSp'] + train['Parch']
    train['IsChild'] = (train['Age'] < 12).astype(int)
    train['IsAlone'] = (train['Relatives'] == 0).astype(int)

    sex_categorical_values = {'female': 0, 'male': 1}
    train['Sex'] = train['Sex'].apply(lambda x: sex_categorical_values[x])
    train = pd.get_dummies(train, columns=['Embarked', 'Title'], drop_first=True, dtype=int)

    return train
