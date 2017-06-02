# Script is indended to open input forex file read lines out of it and then change lines in desired output format
# and then write it into new output file.
inputFile = open("FOREX_input.txt","r")
targetFile = open("forex-watchlist.txt", 'w')
marketPrefix = "FX_IDC:"

inputFileLines = inputFile.readlines()
lastOneLine = len(inputFileLines)

print "Preparing output file...\n"
for idx, line in enumerate(inputFileLines):
	currencyPair = line.split(",")[0]
	prefixedCurrencyPair = marketPrefix + currencyPair
	print str(idx) + " - " + str(prefixedCurrencyPair)
	targetFile.write(prefixedCurrencyPair)
	if idx != lastOneLine - 1:
		targetFile.write(",")

targetFile.close()
print "\nDone, mister!"


