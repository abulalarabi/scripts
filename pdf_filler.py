from fillpdf import fillpdfs
import pandas as pd
import os

fields = fillpdfs.get_form_fields("form.pdf")

# Read the data
data = pd.read_csv("info.csv")
d1 = data["name"].to_numpy()
d2 = data["dob"].to_numpy()
d3 = data["sex"].to_numpy()
d4 = data["date"].to_numpy()
info = [d1, d2, d4, d3]

for j in range(len(d1)):
    # copy keys to a new dictionary
    data_dict = {}
    for i,key in enumerate(fields.keys()):
        data_dict[key] = info[i][j]
    print(data_dict)
    fillpdfs.write_fillable_pdf('form.pdf', d1[j]+"tmpfilled.pdf", data_dict)

    # If you want it flattened:
    fillpdfs.flatten_pdf(d1[j]+"tmpfilled.pdf", "output/"+d1[j]+"filled.pdf")

    # If you want to delete the tmp file using os
    os.remove(d1[j]+"tmpfilled.pdf")