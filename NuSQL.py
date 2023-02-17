CommandDict =  {
    "Select":"SELECT",
    "All":"*",
    "Only":"SELECT DISTINCT",
    "Copy":"INTO",
    "Top":"TOP",
    "Nicknamed ":"AS"
}

stmt = input("Enter NuSQL statement: ")

stmt = stmt.split(" ")
for word in stmt:
    print(CommandDict[word])
    if word == "Create":
