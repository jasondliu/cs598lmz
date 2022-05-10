import codecs
# Test codecs.register_error('strict', codecs.strict_erro)
f = codecs.open('/home/daryln/Documents/Labs/CSC362/Labs/Lab2/2_2/data/grades.csv', encoding = 'utf-8')
grade_data = np.genfromtxt(f, delimiter = ',', names = True, dtype = None, encoding = 'utf-8')

# Create an ordered dictionary of the grade data.
grade_dict = OrderedDict()
for row in grade_data:
    grade_dict[row['student_id']] = row['grade']

# Create a dictionary of student data with their ID as the key.
student_dict = OrderedDict()
for row in student_data:
    student_dict[row['student_id']] = row

# Print out the student information for the student with ID 0000000014.
print(student_dict['0000000014'])

# Print out the student information for the student with ID 0000000001.
print(student_dict['0000000001'])

# Print out the student information for the
