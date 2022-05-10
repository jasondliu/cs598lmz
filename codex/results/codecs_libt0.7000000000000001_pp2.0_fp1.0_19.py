import codecs
codecs.open("C:/Users/Muyiwa/Desktop/Courses/DataManagementAnalytics/Python/Python_Scripts/2.csv", "r", "utf-8-sig")

#**********Converting Excel to CSV***********************
# import xlrd
# import csv
# import codecs
# xls_file = xlrd.open_workbook("C:/Users/Muyiwa/Desktop/Courses/DataManagementAnalytics/Python/Python_Scripts/1.xlsx")
# csv_file = open("C:/Users/Muyiwa/Desktop/Courses/DataManagementAnalytics/Python/Python_Scripts/1.csv", "w")
# write_file = csv.writer(csv_file)
# for sheet in xls_file.sheets():
#     row_count = sheet.nrows
#     for current_row in range(row_count):
#         write_file.writerow(sheet.row_values(current_row))
# csv_file.close()

#**********Converting CSV to Excel****************
