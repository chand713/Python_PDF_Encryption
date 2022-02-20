
import os
import PyPDF2
import pandas
import logging
from datetime import datetime
import tkinter
from tkinter import filedialog
from pandas import DataFrame

root = tkinter.Tk()
root.withdraw()
file_name = filedialog.askopenfilename()
inputpdf = PyPDF2.PdfFileReader(file_name)
pages_no = inputpdf.numPages
print(pages_no)
output = PyPDF2.PdfFileWriter()


#This Method is used to encrypt a file
logging.basicConfig(filename="encryption.log", level=logging.DEBUG)
def file_enc_method(file_name,pages_no):
    for i in range(pages_no):
        inputpdf = PyPDF2.PdfFileReader(file_name)

        output.addPage(inputpdf.getPage(i))
        output.encrypt(password)

    with open(enc_file_name, "wb") as outputStream:
        nn1 = os.path.getsize(outputStream.name)
        output.write(outputStream)
        logging.debug("File Encrypted")
    return enc_file_name
# This method is to find the size of a file
def file_Size(path):
    fsize = os.path.getsize(path)
    fasize = fsize / 1024 ** 2
    logging.debug("File size calculated")
    return fasize

# This method performs writing a data to csv

def write_to_CSV(enc_file_name, size, modified_time):

    if os.path.exists('file_data.csv') == True:
        my_data = {"FileName":[enc_file_name],"Size":[size],"DateModified":[modified_time]}
        my_csv_data = pandas.DataFrame(my_data)
        my_csv_data.to_csv('file_data.csv',mode='a', index=None, header=False)
    else:
        my_data = {"FileName": [enc_file_name], "Size": [size], "DateModified": [modified_time]}
        my_csv_data = pandas.DataFrame(my_data)
        my_csv_data.to_csv('file_data.csv', index=None)
    logging.debug("Data written to csv file")



password = input("Enter Your Password to Encrypt a file:")
enc_file_name = datetime.now().strftime("%Y_%b_%d_%H_%M_%S")+'.pdf' #creating a filename for encrypted one
run_enc = file_enc_method(file_name,pages_no)
size = round(file_Size(run_enc), 2)
modified_time = datetime.now().strftime("%Y/%b/%d %H:%M:%S")
write_to_CSV(enc_file_name, size, modified_time)

# file_name.close()

# --------------------------------------------------------------
