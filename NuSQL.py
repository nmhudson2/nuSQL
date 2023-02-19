infile = open("input.txt","r")
outfile = open("output.sql", "w")

DEFART = ["a","an","the"]

USERVAR = []

CommandDict =  {
    "Select":"SELECT",
    "all":"*",
    "only":"DISTINCT",
    "copy":"INTO",
    "top":"TOP",
    "nicknamed ":"AS",
    "from":"FROM",
    "where":"WHERE",
    "and":"AND",
    "or":"OR",
    "ranged":"BETWEEN",
    "similar to":"LIKE",
    "with":"LIKE",
    "is-in":"IN",
    "NULL":"NULL",
    "!NULL":"NOT NULL",
    "Make":"CREATE",
    "database":"DATABASE",
    "table":"TABLE",
    "index":"INDEX",
    "Delete":"DROP",
    "update":"UPDATE",
    "remove":"DELETE",
    "alter":"ALTER TABLE",
    "amount-of":"COUNT",
    "sum-of":"SUM",
    "average":"AVG",
    "minimum":"MINI",
    "maximum":"MAX",
    "in-order-of":"ORDER BY",
    "descending":"DESC",
    "offset-by":"OFFSET",
}


fileContents = infile.read().split(" ")
print(fileContents)
infile.close()

for word in fileContents:
    if word not in CommandDict:
        USERVAR.append(word)
        outfile.write(word + " ")
    else:
        outfile.write(CommandDict[word]+" ")