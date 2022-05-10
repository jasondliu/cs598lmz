import codecs
codecs.register(lambda name: codecs.lookup('utf-8') if name == 'cp65001' else None)

#PassengerClass
MalePclass = train[['PassengerId', 'Survived', 'Sex', 'Pclass']].query("Sex == 'male'") #Survival rate for men depending on class
MalePclass = MalePclass['Pclass'].value_counts()    
#print(MalePclass)


FemalePclass = train[['PassengerId', 'Survived', 'Sex', 'Pclass']].query("Sex == 'female'") #Survival rate for women depending on class
FemalePclass = FemalePclass['Pclass'].value_counts()
#print(FemalePclass)
    
TotalPclass = train[['PassengerId', 'Survived', 'Sex', 'Pclass']].query("Sex == 'male' or Sex == 'female'") #Survial rate for all depending on class
TotalPclass = TotalPclass['Pclass'].value_counts()
#print(TotalPclass)
    
#print(MalePclass/Female
