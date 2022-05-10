import types
types.ObjectType

# reading in a dataset
sal = pd.read_csv('/Users/a/Python_Data_Science/Iris_Data_Set/Salaries.csv')

# checking out variable contents
sal.head()

# what columns do we have?
sal.columns

# checking out one variable
sal['BasePay'].describe()

# what is the average total pay
sal['TotalPay'].mean()

# what employee has the highest salary?
sal[sal['TotalPayBenefits']== max(sal['TotalPayBenefits'])]['EmployeeName']

# what employee has lowest salary?
sal[sal['TotalPayBenefits']== min(sal['TotalPayBenefits'])]['EmployeeName']


# barplot
import seaborn as sns
sns.barplot(data= sal,x='Year',y='BasePay')

# adding titles
plt.title('Average Base Pay by Year')
plt.show()

# historgram
sns.distplot(sal['OvertimePay'])


