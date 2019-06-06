#put code here and copy it into word_frequency.py

# need to (import?) the EP file and convert it into a string?
# probably using the "open" command/function

eman_proc = open("emancipation_proclamation.txt", "r")

#do i need another variable here? do i need to convert this into a string? i am getting a object no attribute error in line 10

eman_proc.split()
#split up the file into individual words
eman_proc.lowercase()
print(eman_proc)

# now the text file is split into individual words, all lowercase

# need to declare an empty dictionary, this is ultimately where the results will go


# assign keys and values to the dictionary? i.e. words and number of times they appear
# syntax is mydict[key] = "value"

# need to figure out what "pass a list" means

# have to use key to sort by the number of times word appears