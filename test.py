import ezsheets
import time

start_time = time.time() 
ss = ezsheets.Spreadsheet('152M9yVlljFVDf5Nnd2oBjWfvxf5Sfy2n2H7Sz5__1F4')
end_time = time.time()

print(f"Time taken to connect: {end_time - start_time} seconds")

# start_time = time.time()
def write_to_sheet(ss, sheet_name, row, col, val1, val2, val3, val4, val5, val6, val7, val8, val9):
    sheet = ss[sheet_name]
    sheet.updateRow(row, [val1, val2, val3, val4, val5, val6, val7, val8, val9])

# Example usage
write_to_sheet(ss, 'Login Credentials', 6, 1, 'Value1', 'Value2', 'chutiya', 'Value4', 'Value5', 'Value6', 'Value7', 'Value8', 'Value9')
# end_time = time.time()


# print(f"Time taken to update: {end_time - start_time} seconds")


def read_from_sheet(ss, sheet_name, row):
    sheet = ss[sheet_name]
    return sheet.getRow(row)[0:9]

# Example usage
start_time = time.time()
values = read_from_sheet(ss, 'Login Credentials', 6)
end_time = time.time()

print(f"Retrieved values: {values}")
print(f"Time taken to retrieve: {end_time - start_time} seconds")