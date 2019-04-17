orig_file = open("nasa_prawler.txt", "r") #read original file
lines = orig_file.readlines()

start = False
saved_list = []

#start delete at "AADI" and end delete at "CTD". This removes all AADI data
for rec in lines:
    if "AADI" in rec:
        start = True
    if "CTD" in rec:
        start = False
    if not start:
        saved_list.append(rec)


#export only CTD data to new text file
new_text_file = open("nasa_prawler_ctd.txt", "w")
new_text_file.writelines(saved_list)
new_text_file.close()

#read the new CTD only text file
new_file = open("nasa_prawler_ctd.txt","r")
contents = new_file.readlines()
new_file.close()

new_contents = []

# Get rid of empty lines
for line in contents:
    # Strip whitespace, should leave nothing if empty line was just "\n"
    if not line.strip():
        continue
    # We got something, save it
    else:
        new_contents.append(line)

second_file = open("ctd_nolines.txt", "w")
second_file.writelines(new_contents)
second_file.close()